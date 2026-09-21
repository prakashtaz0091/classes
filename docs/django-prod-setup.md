# Django Production Setup & Deployment Guide

**A teaching example: from `manage.py runserver` to a real production deployment**

Stack covered: Django · Celery · Celery Beat · Redis · PostgreSQL · RustFS (S3-compatible storage) · Gunicorn · Nginx · Docker / Docker Compose

---

## How to use this guide

This is not a "copy these files and go" document. Every stage answers five questions before showing any configuration:

> **What problem are we solving? Why do we need this component? What changes in the architecture? What configuration do we need? How do we verify it works?**

We start from a plain local Django project and *evolve* it, one architectural change at a time, into a hardened production system. By the end, you will be able to explain what every moving part does, why it exists, and how to fix it when it breaks — not just how to paste a `docker-compose.yml`.

Throughout the guide, placeholders look like `CHANGE_ME`, `your-domain.com`, `your-secure-password`. **Never** put real secrets in files that get committed to Git.

---

## Table of Contents

0. [Stage 0 — Inspect the Existing Project First](#stage-0)
1. [Stage 1 — Understand the Existing Development Setup](#stage-1)
2. [Stage 2 — Containerize Django](#stage-2)
3. [Stage 3 — Introduce PostgreSQL](#stage-3)
4. [Stage 4 — Introduce Gunicorn](#stage-4)
5. [Stage 5 — Introduce Nginx](#stage-5)
6. [Stage 6 — Redis, Celery Worker, Celery Beat](#stage-6)
7. [Stage 7 — RustFS / S3-Compatible Object Storage](#stage-7)
8. [Stage 8 — Split Development and Production Settings](#stage-8)
9. [Stage 9 — Environment Variables and Secrets](#stage-9)
10. [Stage 10 — Production Security / Django Hardening](#stage-10)
11. [Stage 11 — Real Server / VPS Deployment](#stage-11)
12. [Stage 12 — Domain and HTTPS](#stage-12)
13. [Stage 13 — Database Backups](#stage-13)
14. [Stage 14 — Logs and Monitoring](#stage-14)
15. [Stage 15 — Health Checks and Restart Policies](#stage-15)
16. [Stage 16 — Deployment Process](#stage-16)
17. [Stage 17 — CI/CD](#stage-17)
18. [Final Architecture](#final-architecture)
19. [Docker Compose Structure](#compose-structure)
20. [Production Dockerfile](#dockerfile)
21. [Entrypoint / Startup Scripts](#entrypoint)
22. [Static and Media Files](#static-media)
23. [Networking Reference](#networking)
24. [Troubleshooting](#troubleshooting)
25. [Verification Checklist](#checklist)
26. [Additional Recommendations](#additional)

---

<a id="stage-0"></a>
## Stage 0 — Inspect the Existing Project First

**What problem are we solving?**
You cannot safely "productionize" a project you don't understand. Blindly imposing a textbook architecture on top of an unknown codebase causes broken imports, wrong paths, duplicate configuration, and silent bugs. Before writing a single Dockerfile, spend 30–60 minutes reading the project.

**Why do we need this step?**
Every Django project organizes settings, apps, Celery config, and static/media paths slightly differently. The "correct" production setup is the one that fits *your* project's actual structure — not a generic template.

**What to inspect, and why:**

| Area | What to look for | Why it matters |
|---|---|---|
| Project layout | Is it `myproject/myproject/settings.py` (single project) or `config/settings/` (split settings already)? | Determines whether Stage 8 is a refactor or a from-scratch split. |
| `manage.py` | Which `DJANGO_SETTINGS_MODULE` does it default to? | You must not silently change the entry point. |
| Settings file(s) | `INSTALLED_APPS`, `MIDDLEWARE`, `DATABASES`, `STATIC_URL`, `MEDIA_URL`, `SECRET_KEY` source | Tells you what's currently hardcoded vs. environment-driven. |
| WSGI/ASGI | `wsgi.py` / `asgi.py` — does the project use only WSGI, or also Channels/ASGI? | Gunicorn needs the exact WSGI application path (`myproject.wsgi:application`). If ASGI is used for websockets, Gunicorn+Uvicorn workers or a separate ASGI server may be needed — flag this as a decision point rather than assuming. |
| Celery config | Is there a `celery.py` next to `settings.py`? How is the Celery app created (`app = Celery(...)`)? What's the broker URL currently set to? | You need the exact module path for `celery -A <path> worker` commands. |
| Celery Beat | Is the schedule defined in code (`CELERYBEAT_SCHEDULE` / `beat_schedule`) or in the database (`django-celery-beat`)? | Database-backed schedules need the `django_celery_beat` app + migrations; file-based schedules need a writable `celerybeat-schedule` file location. |
| Redis usage | Is Redis used only as the Celery broker, or also as Django's cache backend / session backend? | Affects whether you need one Redis service or logically separate Redis databases (`redis://redis:6379/0` for broker, `/1` for cache, etc.). |
| Static files config | `STATIC_URL`, `STATIC_ROOT`, `STATICFILES_DIRS`, `STATICFILES_STORAGE` | You need `STATIC_ROOT` to run `collectstatic` in Docker. |
| Media/upload config | `MEDIA_URL`, `MEDIA_ROOT`, any `FileField`/`ImageField` usage, existing storage backend | Determines whether user uploads currently live on local disk (a production risk we'll fix in Stage 7). |
| Existing database config | SQLite file? Local PostgreSQL? Hardcoded credentials? | Determines the migration path to containerized PostgreSQL. |
| Installed packages | `requirements.txt` / `pyproject.toml` — is `gunicorn`, `psycopg2`/`psycopg`, `django-storages`, `boto3`, `django-celery-beat`, `whitenoise` already present? | Avoids installing duplicate or conflicting packages. |
| Environment variables | Is there already a `.env`, `python-decouple`, `django-environ`, or `os.environ.get(...)` usage? | Determines whether Stage 9 is "introduce" or "extend." |
| Existing Docker config | Any `Dockerfile`, `docker-compose.yml`, `.dockerignore` already present? | Adapt instead of overwrite — don't destroy working configuration. |

**Unknowns and defaults**

Because this guide is written generically for a class of projects rather than one specific codebase, several things are *unknown by design*. Where they matter, this guide states a reasonable default explicitly:

- **Unknown: exact app name.** Default used throughout: `config` as the settings package, `myproject` as the Django project name, `myapp` as the WSGI/Celery import path. Replace with your real project name everywhere you see `myproject`/`config`.
- **Unknown: WSGI vs ASGI.** Default: WSGI + Gunicorn (most common for classic Django). If your project uses Channels/websockets, that is called out as a variant in Stage 4.
- **Unknown: whether Celery Beat schedule is DB-backed.** Default: `django-celery-beat` (database-backed), because it's easier to operate and change without redeploying.
- **Unknown: current package manager.** Default: `pip` + `requirements.txt`. If you use Poetry/uv/Pipenv, the same reasoning applies — only the Dockerfile's dependency-install layer changes.

**Verification**

Before moving on, you (or your students) should be able to answer, from memory, without opening the code again:

```text
[ ] What module does manage.py point DJANGO_SETTINGS_MODULE to?
[ ] What is the exact import path used by `celery -A <path>`?
[ ] Is the Celery Beat schedule file-based or DB-based?
[ ] What is STATIC_ROOT currently set to (or unset)?
[ ] Where do uploaded files currently go?
[ ] What database engine is currently configured?
[ ] Does a Dockerfile or docker-compose.yml already exist?
```

If you can't answer one of these, go back and look — do not guess when writing real configuration for a real project.


---

<a id="stage-1"></a>
## Stage 1 — Understand the Existing Development Setup

**What problem are we solving?**
Before changing anything, we need a shared mental model of what "development mode" actually does — so that later, every production change can be explained as "we're replacing *this specific thing* because of *this specific limitation*."

**Architecture (development)**

```text
Browser
   |
   v
Django development server (manage.py runserver)
   |
   v
SQLite / local Postgres (DEBUG=True)
   |
   +--> static files served by Django itself (django.contrib.staticfiles)
   +--> media files written to local disk (MEDIA_ROOT)

Celery worker  -->  Redis (broker)  <--  Celery Beat
   (all running as plain local processes, started manually, no supervision)
```

**Why this setup exists**

- `runserver` auto-reloads on code changes and gives readable tracebacks — great for iteration, useless (and dangerous) under real traffic.
- `DEBUG=True` makes Django print full stack traces, local variables, and settings values on error pages. This is essential for debugging locally and a severe information leak in production.
- SQLite (or a local, unauthenticated Postgres) is fine when only you touch the database. It is not built for concurrent writes from multiple worker processes.
- Django serving static/media files itself is simple, but Django/WSGI workers are not optimized for high-throughput file serving — every static file request occupies an application worker that could be handling real requests.
- Redis and Celery running as ad-hoc local processes (`redis-server`, `celery -A myproject worker`) have no restart policy: if your terminal closes, they die, and nothing brings them back.

**Why this is not sufficient for production**

| Dev component | Production problem |
|---|---|
| `runserver` | Single-threaded (or naive threading), not designed to survive crashes, not designed for concurrent load, and it warns on every startup: "do not use this in production." |
| `DEBUG=True` | Leaks secrets, source paths, settings, and internals to anyone who can trigger a 500 error. |
| SQLite/local DB | No real concurrency control, no network access control, easy to lose on redeploy. |
| Local static/media serving | Slow under load, and *media files stored on local disk disappear or become inconsistent* the moment you run more than one app container or redeploy. |
| Manually started Celery/Redis | No auto-restart, no isolation, no reproducibility across machines. |

**Verification**

```bash
python manage.py runserver 0.0.0.0:8000
# visit http://localhost:8000 — should load
# trigger a 500 error (e.g. undefined variable in a view) and note the
# full traceback page — this is what DEBUG=True exposes
```

```text
[ ] I can explain why runserver is unsuitable for production
[ ] I can explain why DEBUG=True is dangerous in production
[ ] I can explain why local-disk media files are a problem once there's more than one app instance
[ ] I understand Celery worker / Beat / Redis run as three independent processes today
```

We now rebuild this system piece by piece.


---

<a id="stage-2"></a>
## Stage 2 — Containerize Django

### Why?

**Problem:** "It works on my machine" is not a deployment strategy. Different Python versions, missing system libraries, and OS differences between your laptop and a server cause subtle, hard-to-reproduce bugs. We need a way to package the application, its exact Python version, and its system dependencies into one reproducible unit that runs identically everywhere.

**Solution:** Docker packages the app + its runtime environment into an **image** (a read-only template) that becomes a running **container** (an isolated process with its own filesystem view, network namespace, and process tree). Docker Compose then lets us describe *multiple* containers (app, database, cache, etc.) and how they connect, as one declarative file.

At this stage we containerize **only Django itself**, and we deliberately keep `runserver` for now — the goal is to learn Docker mechanics first, without also changing the web server at the same time. We replace `runserver` with Gunicorn in Stage 4.

### Core concepts

- **Image vs. container**: an image is like a class; a container is an instance of it. You can run many containers from one image.
- **Dockerfile**: a recipe describing how to build an image — base OS/language image, dependencies, code, default command.
- **Build context**: the directory sent to the Docker daemon when building (`docker build .`) — everything Docker is *allowed* to `COPY` from. Kept small via `.dockerignore`.
- **Volumes**: a way to persist or share data outside a container's writable layer, or to mount your local source code into the container (useful for development, dangerous for production images — see Stage 3 for why persistence matters).
- **Ports**: `-p HOST:CONTAINER` maps a host machine port to a port inside the container's network namespace.
- **Networks**: Compose creates a private network per project; containers on the same network reach each other **by service name**, not `localhost`. This single fact resolves 80% of "my container can't connect" bugs later in this guide.
- **Environment variables**: how we inject configuration (DB host, secret key, debug flag) into a container without baking it into the image.
- **Container lifecycle**: `docker compose up` (create+start), `stop`, `down` (stop+remove containers, keep volumes by default), `restart`.

### Configuration

`Dockerfile` (development-oriented version — we harden this in the [Production Dockerfile](#dockerfile) section):

```dockerfile
# Dockerfile
FROM python:3.12-slim

# Prevents Python from writing .pyc files and buffers stdout/stderr,
# so logs appear immediately in `docker compose logs`.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System dependencies needed to build Python packages that have C extensions
# (e.g. psycopg2). Kept minimal on purpose.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

`.dockerignore`:

```text
.git
.gitignore
__pycache__/
*.pyc
*.pyo
.venv/
venv/
env/
.env
*.sqlite3
node_modules/
.pytest_cache/
.DS_Store
staticfiles/
mediafiles/
```

`docker-compose.yml` (Stage 2 version — one service):

```yaml
services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    environment:
      - DEBUG=True
      - DJANGO_SETTINGS_MODULE=myproject.settings
```

### Explanation

- `FROM python:3.12-slim`: a small base image with Python preinstalled. `slim` over `alpine` because `alpine`'s musl libc frequently breaks binary Python wheels (e.g. psycopg2), causing longer, more fragile builds.
- `libpq-dev` / `build-essential`: needed to compile `psycopg2` from source if a prebuilt wheel isn't used. (If you use `psycopg2-binary` instead, these can be dropped — but `psycopg2-binary` is officially discouraged for production.)
- `COPY requirements.txt .` **before** `COPY . .`: Docker caches layers. If only your application code changes (not dependencies), this ordering means `pip install` is *not* re-run, making rebuilds much faster.
- `volumes: - .:/app`: mounts your local source code into the container, so code edits appear immediately without rebuilding the image. This is a **development convenience** — we remove it in the production Compose file, because production should run the exact code baked into the image, not whatever happens to be on the host filesystem.
- `ports: "8000:8000"`: exposes the container's port 8000 to your host machine at `localhost:8000`.

### Run

```bash
docker compose build
docker compose up
# or combined:
docker compose up --build
```

### Verify

```bash
curl -I http://localhost:8000
# expect HTTP/1.1 200 OK (or a Django response, not "connection refused")

docker compose ps        # container should show as "running"
docker compose logs web  # should show Django's runserver startup banner
```

```text
[ ] Django container builds without error
[ ] Django container starts and stays running (not restarting in a loop)
[ ] http://localhost:8000 responds
[ ] Editing a Python file locally is reflected after a page refresh (volume mount working)
```

### Common problems

- **`docker: command not found`** — Docker isn't installed, or your shell needs a new session after install.
- **Build fails installing psycopg2** — missing `libpq-dev`/`build-essential`, or using an incompatible Alpine base.
- **Port already in use** — something else (maybe a local `runserver`) is bound to 8000; stop it or change the host-side port mapping.
- **Code changes not reflected** — the volume mount is missing, or Docker Desktop's file-sharing settings exclude the project directory.


---

<a id="stage-3"></a>
## Stage 3 — Introduce PostgreSQL

### Why?

**Problem:** SQLite (or an ad-hoc local Postgres) isn't designed for concurrent, networked, multi-process access — which is exactly what a production app with multiple Gunicorn workers and Celery workers needs. We need a real, networked, concurrency-safe database.

**Why PostgreSQL specifically:** mature transactional guarantees (ACID), excellent concurrent-write handling, rich indexing/JSON support, first-class Django support (`django.db.backends.postgresql`), and it is the de facto standard for production Django.

### Architecture

```text
Django container
      |
      | TCP, port 5432, host = "db" (the Compose service name)
      v
PostgreSQL container
      |
      v
Named Docker volume (persists across container restarts/rebuilds)
```

### Configuration

`docker-compose.yml`:

```yaml
services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    environment:
      - DEBUG=True
      - DJANGO_SETTINGS_MODULE=myproject.settings
      - POSTGRES_HOST=db
      - POSTGRES_PORT=5432
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    depends_on:
      - db

  db:
    image: postgres:16-alpine
    environment:
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"   # optional: only for local debugging with a DB client; remove in production

volumes:
  postgres_data:
```

Django `settings.py`:

```python
import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "myproject"),
        "USER": os.environ.get("POSTGRES_USER", "myproject"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}
```

`requirements.txt` addition:

```text
psycopg2-binary==2.9.9   # or psycopg2==2.9.9 if you keep build-essential/libpq-dev
```

### Explanation

- **`HOST=db`, not `localhost`.** This is the single most important networking lesson in this whole guide: inside Docker Compose, `localhost` refers to *the container itself*, not "the machine running Docker" and not "another container." Compose creates a private DNS-like network where **each service is reachable by its service name** (`db`, `redis`, `rustfs`, etc.). Django asking for `localhost:5432` inside the `web` container will always fail, because nothing is listening on port 5432 *inside the web container*.
- **`depends_on: - db`** starts `db` before `web`, but — critically — it does **not** wait for Postgres to be *ready to accept connections*, only for the container process to have *started*. We revisit this precisely in Stage 15.
- **Named volume `postgres_data`**: Docker containers are meant to be disposable — you can delete and recreate the `db` container any time. But the *data* must outlive the container. A named volume is storage managed by Docker, independent of any specific container's lifecycle, mounted at Postgres's data directory (`/var/lib/postgresql/data`).
- **`ports: "5432:5432"` on `db`** is only useful so you (a human, on your laptop) can connect with a local DB GUI. It is **not** needed for `web` to talk to `db` — that happens over the internal Compose network regardless of published ports. This line should be removed in production (see Stage 10/11).

> **Containers can be disposable, but application data must be persistent.** You should be comfortable running `docker compose down` and `docker compose up --build` at any time without fear of losing rows in your database — because the data lives in the named volume, not in the container's writable layer.

### Run

```bash
docker compose up --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

### Verify

```bash
docker compose exec db psql -U $POSTGRES_USER -d $POSTGRES_DB -c '\dt'
# should list Django's tables (django_migrations, auth_user, etc.) after migrate

docker compose exec web python manage.py dbshell
# should drop you into a psql prompt talking to the "db" container, not fail
```

```text
[ ] `web` and `db` containers both start
[ ] `python manage.py migrate` completes without connection errors
[ ] Data survives `docker compose down && docker compose up` (not `-v`)
[ ] Data is GONE only if you explicitly run `docker compose down -v` (expected — volumes were explicitly removed)
```

### Common connection errors

| Error | Likely cause |
|---|---|
| `could not translate host name "db" to address` | `web` isn't on the same Compose network as `db` (rare if using one compose file), or a typo in `POSTGRES_HOST`. |
| `connection refused` on `db:5432` | Postgres hasn't finished starting yet (race condition — see Stage 15), or wrong port. |
| `password authentication failed` | `POSTGRES_PASSWORD` mismatch between `db` service env and Django's `DATABASES` config — usually caused by changing `.env` *after* the volume already initialized Postgres with the old password (Postgres only applies `POSTGRES_PASSWORD` on **first** container creation with an empty volume). |
| `FATAL: database "X" does not exist` | `POSTGRES_DB` changed after the volume was already created; the old volume still has the old database name. |


---

<a id="stage-4"></a>
## Stage 4 — Introduce Gunicorn

### Why?

**Problem:** Django's development server is explicitly not built for production: it's not hardened against slow clients, doesn't manage multiple worker processes efficiently, and prints a startup warning telling you so. We need a WSGI application server designed to run untrusted, concurrent, production traffic.

**Solution: Gunicorn** ("Green Unicorn") is a mature, pre-fork WSGI HTTP server. It starts multiple **worker processes**, each capable of handling requests independently, and manages their lifecycle (restarting crashed workers, etc.).

> Note on WSGI vs ASGI: this guide assumes a standard Django app (WSGI). If your project uses Django Channels / websockets / long-lived async connections, Gunicorn+Uvicorn workers (`gunicorn -k uvicorn.workers.UvicornWorker`) or a separate ASGI server is the correct variant — flagged here as a decision point since it depends on your actual project (Stage 0).

### Architecture

```text
Browser
   |
   v
Gunicorn (multiple worker processes)
   |
   v
Django application code
   |
   v
PostgreSQL
```

### Configuration

`requirements.txt` addition:

```text
gunicorn==22.0.0
```

`docker-compose.yml` — change the `web` service command:

```yaml
services:
  web:
    build: .
    command: gunicorn myproject.wsgi:application --bind 0.0.0.0:8000 --workers 3
    ports:
      - "8000:8000"
    environment:
      - DEBUG=True
      - DJANGO_SETTINGS_MODULE=myproject.settings
      - POSTGRES_HOST=db
      # ...
    depends_on:
      - db
```

A dedicated Gunicorn config file is preferable to a long command line once you add logging/timeouts:

`gunicorn.conf.py`:

```python
bind = "0.0.0.0:8000"
workers = 3          # rule of thumb: (2 x CPU cores) + 1
worker_class = "sync"
timeout = 30
graceful_timeout = 30
keepalive = 5
accesslog = "-"       # "-" = stdout, picked up by `docker compose logs`
errorlog = "-"
loglevel = "info"
```

```yaml
command: gunicorn myproject.wsgi:application -c gunicorn.conf.py
```

### Explanation

- `myproject.wsgi:application` — the Python import path to your `wsgi.py` module's `application` callable. **This must match your actual project's WSGI module path** (verify in Stage 0).
- `--bind 0.0.0.0:8000` (not `127.0.0.1:8000`): inside a container, `127.0.0.1` only accepts connections from *within that same container's network namespace*. Docker's port mapping / Nginx (in the next stage) connects from *outside* the container's loopback, so Gunicorn must bind to `0.0.0.0` (all interfaces) to be reachable.
- `--workers 3`: each worker is a separate OS process that can handle one request at a time (with the default `sync` worker class). More workers = more concurrent requests, at the cost of more memory. A common starting point is `(2 × CPU cores) + 1`.
- Gunicorn does **not** serve static files efficiently and is not meant to be the internet-facing server — that's what Nginx is for (next stage). At this stage, Gunicorn is still directly published to the host via `ports:`, purely as an intermediate teaching step.

### Run

```bash
docker compose up --build
```

### Verify

```bash
curl -I http://localhost:8000
docker compose logs web
# should show Gunicorn's "Booting worker with pid ..." lines, not the runserver banner
```

```text
[ ] Gunicorn starts the configured number of workers
[ ] The app responds identically to how it did under runserver
[ ] Killing one worker process (docker compose exec web kill <pid>) results in Gunicorn respawning it
```

### Common problems

- **`ModuleNotFoundError: No module named 'myproject'`** — wrong WSGI import path; must match Stage 0's findings exactly.
- **App works via `curl` inside the container but not from the host** — Gunicorn is bound to `127.0.0.1` instead of `0.0.0.0`.
- **Static files 404 / broken CSS** — expected at this stage; Gunicorn isn't meant to serve static assets well. Fixed in Stage 5.


---

<a id="stage-5"></a>
## Stage 5 — Introduce Nginx

### Why?

**Problem:** Gunicorn is an *application* server, not a general-purpose web server. It's not optimized for serving static files efficiently, doesn't handle TLS termination gracefully at scale, and shouldn't be the thing directly exposed to the open internet (its request-parsing and connection-handling are optimized for trusted upstream traffic, not hostile/slow clients).

**Solution: Nginx** sits in front of Gunicorn as a **reverse proxy**: it receives all internet traffic, serves static/media files directly (bypassing Django entirely), and forwards everything else to Gunicorn.

### Architecture

```text
Internet
   |
   v
Nginx  (public entry point, serves static/media, terminates TLS later)
   |  (proxies dynamic requests over the internal Docker network)
   v
Gunicorn
   |
   v
Django
```

### Configuration

`nginx/nginx.conf`:

```nginx
upstream django {
    server web:8000;
}

server {
    listen 80;
    server_name your-domain.com;

    client_max_body_size 20M;

    location /static/ {
        alias /app/staticfiles/;
    }

    location /media/ {
        alias /app/mediafiles/;
    }

    location / {
        proxy_pass http://django;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

`docker-compose.yml` additions:

```yaml
services:
  web:
    build: .
    command: gunicorn myproject.wsgi:application -c gunicorn.conf.py
    expose:
      - "8000"          # only reachable by other containers, not the host
    volumes:
      - static_volume:/app/staticfiles
      - media_volume:/app/mediafiles
    environment:
      - DEBUG=True
      - DJANGO_SETTINGS_MODULE=myproject.settings
    depends_on:
      - db

  nginx:
    image: nginx:1.27-alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf:ro
      - static_volume:/app/staticfiles:ro
      - media_volume:/app/mediafiles:ro
    depends_on:
      - web

volumes:
  static_volume:
  media_volume:
  postgres_data:
```

`settings.py`:

```python
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"   # revisited in Stage 7 (RustFS replaces this)
```

### Explanation

- `upstream django { server web:8000; }` — again, `web` is the **Compose service name**, resolved over the internal Docker network, not `localhost`.
- `web`'s `ports:` changed to `expose: "8000"`: `expose` documents the port for other containers on the same network without publishing it to the host machine. The **only** container that should have a `ports:` mapping to the host now is `nginx` (port 80). This is the first concrete instance of "don't expose internal services unnecessarily," a principle we return to repeatedly.
- `proxy_set_header X-Forwarded-Proto $scheme` / `X-Forwarded-For` / `X-Real-IP`: without these, Django has no way to know the original client IP or whether the original request was HTTPS — it only sees the internal proxy_pass connection from Nginx. Stage 10 uses `X-Forwarded-Proto` together with `SECURE_PROXY_SSL_HEADER`.
- `location /static/ { alias /app/staticfiles/; }`: Nginx serves these files **directly from disk**, without ever invoking Django/Gunicorn — dramatically faster and doesn't consume an application worker slot.
- **Why static files bypass Django/Gunicorn**: static files don't change per-request and don't need Python logic — they're the textbook case for a dedicated, highly optimized static file server. Using Django to serve them at scale wastes application capacity that should be handling real business logic.
- `static_volume` / `media_volume` are shared between `web` and `nginx`: Django (via Gunicorn) writes collected static files and uploaded media into these volumes; Nginx reads from the same volumes, read-only (`:ro`), to serve them.

### Run

```bash
docker compose exec web python manage.py collectstatic --noinput
docker compose up --build
```

### Verify

```bash
curl -I http://localhost/            # via Nginx now, not :8000 directly
curl -I http://localhost/static/admin/css/base.css   # Django admin CSS should load
```

```text
[ ] Nginx responds on port 80
[ ] Static files load correctly (check the Django admin's styling)
[ ] Dynamic pages still work (Nginx correctly proxies to Gunicorn)
[ ] Gunicorn/web is no longer reachable directly from the host on 8000
```

### Common problems

- **502 Bad Gateway** — Gunicorn isn't running, or the `upstream` hostname/port doesn't match the Compose service name/port.
- **CSS/JS 404 after collectstatic** — `STATIC_ROOT` path in Django doesn't match the volume mount path in the Nginx config, or `collectstatic` wasn't run.
- **Nginx starts before `web`'s static files exist** — cosmetic only (fixed after the first `collectstatic`), but illustrates why start *order* isn't the same as *readiness* (Stage 15).


---

<a id="stage-6"></a>
## Stage 6 — Configure Redis, Celery Worker and Celery Beat

### Why?

**Problem:** Some work shouldn't happen inside the request/response cycle — sending emails, generating reports, calling slow third-party APIs, running scheduled jobs at 3am. Doing this synchronously inside a Django view makes the user wait, and doing it "in the background" with an ad-hoc thread doesn't survive a process restart and doesn't scale across machines.

**Solution:**
- **Redis** acts as a fast, in-memory **message broker**: Django pushes a "task" description onto a Redis queue and immediately returns a response to the user.
- **Celery Worker** is a separate long-running process that watches the Redis queue, pulls tasks off it, and executes them.
- **Celery Beat** is a separate scheduler process that doesn't execute tasks itself — it periodically pushes *scheduled* tasks onto the same Redis queue, which workers then pick up like any other task.

### Architecture

```text
                 +--------------+
                 |    Django    |
                 +------+-------+
                        |  (task.delay(...) enqueues a message)
                        v
                     Redis
                        |
              +---------+---------+
              v                   v
        Celery Worker        Celery Beat
     (pulls & executes     (pushes scheduled
        tasks from the        tasks onto the
        queue)                 same queue)
```

**Why Beat and Worker are separate processes:** Beat's only job is to know *when* something should run and enqueue it on time — it does not execute business logic and must not be scaled beyond a single instance (two Beat instances would double-schedule everything). Workers execute tasks and *can* be scaled to many instances/replicas for throughput. Coupling them into one process would force you to choose one scaling strategy for two fundamentally different responsibilities.

### Configuration

`requirements.txt` additions:

```text
celery==5.4.0
redis==5.0.4
django-celery-beat==2.6.0   # only if using DB-backed schedules (Stage 0 decision)
```

`myproject/celery.py` (adjust the import path to match Stage 0's findings):

```python
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

app = Celery("myproject")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
```

`settings.py`:

```python
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://redis:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis://redis:6379/1")
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE   # keep in sync with Django's TIME_ZONE — a common Beat bug

# If using django-celery-beat (DB-backed schedule):
INSTALLED_APPS += ["django_celery_beat"]
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
```

`docker-compose.yml` additions:

```yaml
services:
  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  celery-worker:
    build: .
    command: celery -A myproject worker --loglevel=info
    volumes:
      - .:/app
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0
      - CELERY_RESULT_BACKEND=redis://redis:6379/1
      - POSTGRES_HOST=db
    depends_on:
      - redis
      - db
    restart: unless-stopped

  celery-beat:
    build: .
    command: celery -A myproject beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler
    volumes:
      - .:/app
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0
      - POSTGRES_HOST=db
    depends_on:
      - redis
      - db
    restart: unless-stopped

volumes:
  redis_data:
```

### Explanation

- `redis://redis:6379/0` — `redis` is again the **service name**; `6379` is Redis's default port; `/0` and `/1` select different logical Redis "databases" within the same Redis instance so the Celery broker and result backend don't collide with each other or with Django's cache (if Redis is also used for caching — commonly `/2`).
- **`redis_data` volume**: by default Redis is often treated as ephemeral (pure cache/broker), but without persistence, an unexpected restart loses any *queued-but-not-yet-executed* tasks and any cached data. Whether you need `appendonly yes` (AOF persistence) depends on whether losing a few seconds of queued tasks on a crash is acceptable for your application — flag this as a decision, not a given.
- `celery-worker` and `celery-beat` are **separate Compose services**, each its own container, both built from the *same image* as `web` (same Dockerfile, same code) but with different `command:` — a very common and correct pattern: one image, multiple roles.
- `restart: unless-stopped`: if the worker crashes (e.g. an unhandled exception in a task consuming the whole process, or an OOM kill), Docker restarts it automatically. This does **not** replace proper task-level error handling (see below).

**What happens if…**

| Failure | Effect |
|---|---|
| Redis is unavailable | `.delay()` calls raise a connection error (or silently retry, depending on `CELERY_TASK_ALWAYS_EAGER`/broker retry settings) — tasks can't be enqueued at all. Django requests that don't depend on Celery keep working normally. |
| Worker is unavailable | Tasks pile up in the Redis queue, unexecuted, but not lost — they'll be processed once a worker comes back (Redis persistence permitting). |
| Beat is unavailable | No new *scheduled* tasks are enqueued; on-demand tasks (`.delay()` from views) are unaffected. |
| A task fails (raises an exception) | Depends on `CELERY_TASK_ACKS_LATE` / retry configuration. By default, an unhandled exception marks the task as `FAILURE` in the result backend and it is **not** automatically retried unless the task explicitly defines `autoretry_for` / `max_retries`, or you call `self.retry()`. |

### Run

```bash
docker compose up --build
docker compose exec web python manage.py migrate   # creates django_celery_beat tables
```

### Verify

```bash
docker compose exec web python manage.py shell -c "
from myproject.celery import app
result = app.send_task('myapp.tasks.some_task')
print(result.id)
"
docker compose logs celery-worker   # should show the task being received and executed
docker compose logs celery-beat     # should show scheduled tasks being sent, on schedule
```

```text
[ ] Redis container is healthy (`docker compose exec redis redis-cli ping` -> PONG)
[ ] Celery worker logs show "ready" / connected to broker
[ ] A manually triggered task executes and appears in the worker log
[ ] Celery Beat logs show tasks being scheduled at the expected times
[ ] Only one celery-beat instance is running (never scale this service)
```

### Common problems

- **Worker can't connect to broker** — wrong `CELERY_BROKER_URL` host (must be `redis`, not `localhost` or `127.0.0.1`).
- **Tasks silently never run** — worker isn't subscribed to the queue the task was sent to (queue name mismatch), or the worker container isn't running at all.
- **Beat schedules the same task twice per interval** — two `celery-beat` containers/replicas running simultaneously; Beat must be a singleton.
- **Timezone-looking bugs ("task ran an hour off")** — `CELERY_TIMEZONE` not matching Django's `TIME_ZONE`, or `USE_TZ` mismatches.


---

<a id="stage-7"></a>
## Stage 7 — Introduce RustFS / S3-Compatible Object Storage

### Why?

**Problem:** So far, uploaded media files (`MEDIA_ROOT`) live on the `web` container's local filesystem (or a Docker volume attached to it). This breaks down as soon as:
- You run more than one `web`/Gunicorn container (a common horizontal-scaling step) — a file uploaded via one container isn't visible from another.
- You redeploy by replacing the container — anything not in a *named volume* is lost, and even named volumes tie your media data to one specific Docker host, complicating backups and migration to another server.

**Solution:** Move media storage out of the application container entirely, into a dedicated **object storage** service speaking the **S3 API** — an industry-standard protocol for storing and retrieving files by key, over HTTP, that decouples "where files live" from "which container is currently running the app." Here we use **RustFS**, a self-hosted, S3-API-compatible object storage server, as an alternative to a managed cloud provider.

### Architecture

```text
Django
   |
   | S3-compatible API (HTTP, signed requests)
   v
RustFS
   |
   v
Object storage (bucket -> keys -> file bytes)
```

### Core concepts

- **Object storage**: files are stored as opaque "objects" identified by a key (roughly, a path string) inside a **bucket** (a namespace), accessed over HTTP — not a traditional filesystem.
- **S3 API**: the de facto standard protocol for object storage, originally Amazon S3's API, now implemented by many self-hosted systems (RustFS, MinIO, etc.) and supported by client libraries like `boto3` and Django's `django-storages`.
- **Access key / secret key**: credential pair used to sign requests to the S3 API — conceptually a username+password for programmatic access.
- **Endpoint**: the URL of the S3-compatible server (for RustFS, your self-hosted URL, e.g. `http://rustfs:9000`, rather than AWS's default endpoint).
- **`django-storages`**: a Django library providing storage backends (including S3-compatible) that plug into Django's `DEFAULT_FILE_STORAGE` / `STORAGES` setting, so `FileField`/`ImageField` transparently read/write to the object store instead of local disk.

### Configuration

`requirements.txt` additions:

```text
django-storages==1.14.4
boto3==1.34.144
```

`docker-compose.yml`:

```yaml
services:
  rustfs:
    image: rustfs/rustfs:latest   # verify the current official image/tag before use
    environment:
      - RUSTFS_ACCESS_KEY=${RUSTFS_ACCESS_KEY}
      - RUSTFS_SECRET_KEY=${RUSTFS_SECRET_KEY}
    volumes:
      - rustfs_data:/data
    expose:
      - "9000"
    restart: unless-stopped

volumes:
  rustfs_data:
```

`settings.py` (Django 5+ `STORAGES` setting):

```python
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]
AWS_S3_ENDPOINT_URL = os.environ["S3_ENDPOINT_URL"]   # e.g. http://rustfs:9000 internally
AWS_S3_ADDRESSING_STYLE = "path"                       # most self-hosted S3-compatible servers need path-style
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_AUTH = True          # signed, expiring URLs for media by default
```

### Explanation

- **Static vs. media stay separate on purpose.** Static files (CSS/JS/admin assets) are still served by Nginx directly from the `static_volume` (Stage 5) — they're part of the *application deployment*, not user data, and Nginx serving them locally is faster than round-tripping through an S3 API. Only `MEDIA` (user uploads) moves to RustFS. Mixing the two — e.g. routing static files through S3 as well "for consistency" — adds latency and complexity with no real benefit for assets that ship with your code.
- `AWS_S3_ENDPOINT_URL` uses the **internal** Compose network address (`http://rustfs:9000`) when Django itself talks to RustFS — but if you generate *public* media URLs shown to browsers, those need a URL the browser can actually reach (a public hostname/reverse-proxy path for RustFS, or Nginx proxying `/media/` requests through to RustFS — a decision to make explicitly based on whether media should be public or signed/private).
- `AWS_DEFAULT_ACL = None` and `AWS_QUERYSTRING_AUTH = True`: by default, treat uploaded files as **not publicly readable by a guessable URL** — Django/`django-storages` generates a signed URL with an expiry instead. Whether your app needs public, unsigned media URLs (e.g. a public image gallery) is an application-specific decision; don't default to fully public storage without deciding this deliberately.

**RustFS itself is not "production-safe" just because it's running in Docker.** Running the container is necessary but not sufficient. You are now operationally responsible for:

- **Persistent storage**: the `rustfs_data` volume must live on durable disk and be included in your backup strategy (Stage 13) — object storage data is exactly as vulnerable to disk failure as PostgreSQL's data.
- **Backup strategy**: object storage needs its own backup/replication plan; it is not automatically redundant just because it "feels like the cloud."
- **Access control**: access/secret keys must be treated as production secrets (Stage 9), rotated periodically, and never reused across environments.
- **Operational security**: RustFS should **not** be exposed on a public port (`expose`, not `ports`, exactly like PostgreSQL and Redis) — only `web`/`nginx` should reach it, over the internal Docker network.
- **Disaster recovery**: if the disk hosting `rustfs_data` fails and there's no backup, uploaded user files are permanently lost — plan for this exactly as seriously as you plan for database loss.

### Run

```bash
docker compose exec web python manage.py shell -c "
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
default_storage.save('test.txt', ContentFile(b'hello from RustFS'))
print(default_storage.exists('test.txt'))
"
```

### Verify

```text
[ ] RustFS container starts and is reachable from `web` on the internal network
[ ] Uploading a file via Django's admin/a form actually appears in RustFS's bucket, not on local disk
[ ] The saved file's URL is reachable (directly or via a signed URL) from a browser
[ ] RustFS is NOT reachable from the public internet (no `ports:` mapping)
```

### Common problems

- **`SignatureDoesNotMatch` / auth errors** — access/secret key mismatch, or `AWS_S3_ADDRESSING_STYLE` not set to `path` for a self-hosted server expecting path-style requests instead of virtual-hosted-style.
- **Bucket doesn't exist** — the bucket must usually be created explicitly (via RustFS's own admin tooling/CLI) before Django can write to it; `django-storages` does not create buckets for you.
- **Uploads work from `web` but the resulting URL 404s in a browser** — the endpoint used to *write* (internal `rustfs:9000`) differs from what's needed to *read* from a browser (a public-facing URL); these are two different concerns and often need two different settings (an internal endpoint for API calls, and a public URL/custom domain for serving).


---

<a id="stage-8"></a>
## Stage 8 — Split Development and Production Settings

### Why?

**Problem:** So far, all environment differences (`DEBUG`, database host, storage backend) have been jammed into one `settings.py`, read from environment variables with fallback defaults. This works, but as the number of settings grows, it becomes hard to see, at a glance, what's actually different between development and production — and it's easy to accidentally ship a production container with a development default.

**Solution:** Split settings into a shared base plus environment-specific overrides, selected via `DJANGO_SETTINGS_MODULE`.

### Configuration

Recommended structure (adapt to your existing layout from Stage 0 — if your project already has `config/settings.py`, this is a straightforward split, not a rewrite):

```text
config/
    settings/
        __init__.py
        base.py     # shared by all environments
        dev.py      # local development
        prod.py     # production
```

`config/settings/base.py` — everything that's identical everywhere: `INSTALLED_APPS`, `MIDDLEWARE`, templates, `AUTH_PASSWORD_VALIDATORS`, Celery app config shape, `STORAGES` shape, etc. Values that differ per-environment are still read from `os.environ`, but the *defaults* differ between `dev.py` and `prod.py`.

`config/settings/dev.py`:

```python
from .base import *  # noqa

DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "myproject_dev"),
        "USER": os.environ.get("POSTGRES_USER", "myproject"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "devpassword"),
        "HOST": os.environ.get("POSTGRES_HOST", "db"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}

# In dev, it's often convenient to skip S3/RustFS and just write to local disk:
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
}
```

`config/settings/prod.py`:

```python
import os
from .base import *  # noqa

DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]                       # no fallback — fail loudly if missing
ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"].split(",")
CSRF_TRUSTED_ORIGINS = os.environ["CSRF_TRUSTED_ORIGINS"].split(",")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
        "CONN_MAX_AGE": 60,
    }
}

STORAGES = {
    "default": {"BACKEND": "storages.backends.s3.S3Storage"},
    "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
}
# ... security settings (Stage 10)
```

`manage.py` / `wsgi.py`: change the default:

```python
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
```

Selecting the environment via Compose:

```yaml
services:
  web:
    environment:
      - DJANGO_SETTINGS_MODULE=config.settings.prod
```

### Explanation

- **Fail loudly, not silently, in production.** Notice `dev.py` uses `os.environ.get("X", "safe-dev-default")`, while `prod.py` uses `os.environ["X"]` (a plain dict lookup, which raises `KeyError` if unset). This is deliberate: a missing `SECRET_KEY` in production should crash immediately on startup, not silently fall back to an insecure default and serve traffic.
- `DJANGO_SETTINGS_MODULE` is how Django decides *which* settings module to import — set once per environment as an environment variable, never hardcoded differently across `manage.py`/`wsgi.py`/Celery.
- The alternative to file-based splitting is a single `settings.py` fully driven by an `ENV=dev`/`ENV=prod` variable with `if ENV == "prod": ...` branches. Both are valid; the file-split approach is preferred here because it makes the *set of differences* explicit and reviewable in a diff, rather than scattered through conditionals.

### Verify

```bash
DJANGO_SETTINGS_MODULE=config.settings.prod python manage.py check --deploy
DJANGO_SETTINGS_MODULE=config.settings.dev python manage.py check
```

```text
[ ] Production settings load only from environment variables, no hardcoded secrets
[ ] Missing a required production env var causes an immediate, clear startup failure
[ ] `manage.py`, `wsgi.py`, `celery.py`, and Compose all agree on which settings module to use per environment
```


---

<a id="stage-9"></a>
## Stage 9 — Environment Variables and Secrets

### Why?

**Problem:** Stage 8 assumes environment variables exist. We need a consistent, safe way to define, distribute, and *not leak* them.

### Configuration

`.env.example` (committed to Git — documents what's needed, contains no real values):

```env
# Django
SECRET_KEY=CHANGE_ME
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
CSRF_TRUSTED_ORIGINS=https://your-domain.com,https://www.your-domain.com

# PostgreSQL
POSTGRES_DB=myproject
POSTGRES_USER=myproject
POSTGRES_PASSWORD=your-secure-password
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Redis / Celery
REDIS_URL=redis://redis:6379/2
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/1

# RustFS / S3
S3_ENDPOINT_URL=http://rustfs:9000
AWS_ACCESS_KEY_ID=CHANGE_ME
AWS_SECRET_ACCESS_KEY=CHANGE_ME
AWS_STORAGE_BUCKET_NAME=myproject-media
```

`.env` (real values, **never committed**):

```gitignore
# .gitignore
.env
*.env
!.env.example
```

`docker-compose.yml`:

```yaml
services:
  web:
    env_file:
      - .env
```

### Explanation

- **`.env.example` vs `.env`**: `.env.example` is documentation — a checklist of every variable a new environment needs, with placeholder values, safe to commit. `.env` holds the real values for one specific environment (your laptop, or one specific server) and must never reach Git history.
- **Why `.env` must never be committed**: Git history is effectively permanent and often shared widely (teammates, CI logs, public forks). A secret committed once remains recoverable from history even after being "removed" in a later commit, unless the entire history is rewritten and all clones are invalidated — assume any committed secret is compromised and must be rotated, not just deleted.
- **Secret rotation**: periodically (and immediately after any suspected leak or when an employee/collaborator with access leaves), regenerate `SECRET_KEY`, database passwords, and S3 access/secret keys, and redeploy. Rotating `SECRET_KEY` invalidates existing signed sessions/cookies — plan for a controlled rollout, not a surprise mid-day rotation.
- **Production secret management beyond `.env`**: a plain `.env` file on a single VPS is a reasonable starting point for a small/teaching deployment, but larger setups typically graduate to a dedicated secrets manager (e.g. Docker Swarm/Kubernetes secrets, HashiCorp Vault, or your cloud provider's secret store) so secrets are encrypted at rest, access-controlled, and audited — flagged here as a natural next step, not a requirement for this guide's scope.

### Verify

```bash
git log --all --full-history -- .env
# should return NOTHING — if it returns commits, .env was committed at some point and
# every secret it ever contained must be treated as compromised and rotated

docker compose config
# prints the fully resolved compose config with env vars substituted — use this to
# sanity-check values without printing your actual .env file to a shared screen
```

```text
[ ] .env is in .gitignore and has never been committed
[ ] .env.example exists and lists every variable the app needs, with placeholders only
[ ] No real secret exists anywhere else in the repository (grep for obvious leaks)
[ ] Rotating a secret is a documented, repeatable action, not a one-off improvisation
```


---

<a id="stage-10"></a>
## Stage 10 — Production Security / Django Hardening

### Why?

**Problem:** Everything built so far is *functional*, not *hardened*. A functional-but-unhardened production deployment is a common cause of real breaches: verbose error pages, unencrypted cookies, unrestricted hosts, and unnecessarily exposed internal services.

### Django settings, explained one by one

```python
# config/settings/prod.py

DEBUG = False
```
Turns off Django's detailed error pages (which leak source code, local variables, installed packages, and settings) in favor of a generic error page. This is the single highest-impact production setting.

```python
ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"].split(",")
```
Django rejects any HTTP request whose `Host` header isn't in this list, preventing HTTP Host header attacks (e.g. cache poisoning, password-reset-link poisoning that embeds an attacker-controlled host).

```python
CSRF_TRUSTED_ORIGINS = os.environ["CSRF_TRUSTED_ORIGINS"].split(",")
```
Required (Django 4+) for any HTTPS origin submitting cross-origin POSTs Django should trust (e.g. an admin panel accessed via `www.` and the bare domain, or an API consumed by a separate frontend origin).

```python
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```
Cookies are only ever sent over HTTPS connections, never accidentally over plain HTTP (which could be intercepted on the network).

```python
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
```
Because Nginx terminates TLS and Gunicorn only ever sees plain HTTP *inside* the Docker network (Stage 5's `proxy_set_header X-Forwarded-Proto $scheme`), Django needs to be told to trust that header to correctly know "this request was actually HTTPS" — otherwise Django thinks every request is insecure and `SESSION_COOKIE_SECURE`/redirects misbehave. **This setting is only safe because Nginx, not the client, sets this header** — never enable it if untrusted clients can reach Django directly and set arbitrary headers.

```python
SECURE_SSL_REDIRECT = True
```
Django-level redirect from HTTP to HTTPS. Often handled by Nginx instead (Stage 12) — pick one place to do this, not both ambiguously.

```python
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```
HTTP Strict Transport Security: tells browsers "always use HTTPS for this domain for the next year, even if the user types `http://`." Only enable once you're confident HTTPS is fully and permanently working — a broken HSTS rollout can lock out users' browsers from an accidentally-HTTP-only domain for the configured duration.

```python
SECRET_KEY = os.environ["SECRET_KEY"]
```
Used for cryptographic signing (sessions, password reset tokens, CSRF). Must be long, random, unique per environment, and never reused between dev and prod.

**Database password security**: never commit it, rotate it periodically (Stage 9), and ensure Postgres isn't reachable from outside the Docker network (see below).

**Redis exposure / RustFS exposure / unnecessary public ports**: as established in Stages 3, 6, and 7 — only Nginx should have a `ports:` mapping to the host. `db`, `redis`, `rustfs`, and `web` (Gunicorn) should use `expose:` (internal-only) or no port declaration at all in production Compose files.

**Firewall**: even with Docker's internal networking correctly restricting *application-level* access, the host's own firewall (e.g. `ufw`, `nftables`, or your cloud provider's security group) should independently block all inbound ports except 22 (SSH, ideally restricted further), 80, and 443 — defense in depth, not reliance on Docker networking alone.

**SSH security**: disable password authentication in favor of key-based auth, disable root login, and consider changing the default port or adding `fail2ban` to blunt automated brute-force attempts.

**Container privileges**: don't run application containers as root unless required. In the Dockerfile:

```dockerfile
RUN useradd --create-home appuser
USER appuser
```

Running as a non-root user limits the blast radius if the application process is ever compromised (it can't, for instance, modify other users' files or install system packages inside the container).

### Django's built-in deployment checklist

```bash
DJANGO_SETTINGS_MODULE=config.settings.prod python manage.py check --deploy
```

This runs Django's own security checklist against your settings and reports specific warnings (e.g. "`SECURE_HSTS_SECONDS` not set", "`DEBUG` is True") — run this as a required step before every production deploy, not just once.

### Verify

```bash
python manage.py check --deploy
# should report zero warnings once this stage is complete

curl -I http://your-domain.com
# should redirect to https:// (once Stage 12 / SECURE_SSL_REDIRECT is active)

docker compose config | grep -A3 "db:\|redis:\|rustfs:"
# confirm none of these services have a host `ports:` mapping in production
```

```text
[ ] DEBUG=False in production
[ ] ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS set explicitly, no wildcards
[ ] Session/CSRF cookies marked Secure
[ ] SECURE_PROXY_SSL_HEADER set and trusted only because Nginx controls that header
[ ] `manage.py check --deploy` passes clean
[ ] db / redis / rustfs have no public port mappings
[ ] Host firewall independently restricts inbound ports
[ ] SSH uses key-based auth only
[ ] Application container runs as a non-root user
```


---

<a id="stage-11"></a>
## Stage 11 — Real Server / VPS Deployment

### Why?

**Problem:** Everything so far has run on a development laptop. Production means a real Linux server reachable from the internet, with its own OS, networking, and operational constraints.

### Configuration / flow

```text
Developer
    |
    v
Git repository (GitHub/GitLab/etc.)
    |
    v
VPS (Ubuntu/Debian, provisioned with a public IP)
    |
    v
Docker + Docker Compose installed
    |
    v
Production services (this guide's Compose stack)
```

**Provisioning steps, explained:**

1. **VPS/server**: rent a Linux VM from a hosting provider (DigitalOcean, Hetzner, Linode, AWS EC2, etc.). A modest 2 vCPU / 4 GB RAM instance is enough for a small teaching deployment.
2. **SSH**: your primary access method — set up key-based auth immediately (Stage 10), disable password login.
3. **DNS**: point your domain at the server's IP (covered in detail in Stage 12).
4. **Firewall**: configure `ufw` (or provider security groups) to allow only 22/80/443 inbound.

   ```bash
   sudo ufw allow OpenSSH
   sudo ufw allow 80/tcp
   sudo ufw allow 443/tcp
   sudo ufw enable
   ```
5. **Docker installation**:

   ```bash
   curl -fsSL https://get.docker.com | sudo sh
   sudo usermod -aG docker $USER
   # log out/in for the group change to apply
   docker compose version   # Compose v2 ships as a Docker plugin on modern installs
   ```
6. **Git**: install and use to pull your repository onto the server.
7. **Deployment directory**: a consistent, predictable path, e.g. `/srv/myproject/`, owned by a dedicated deploy user (not root) with correct permissions.
8. **Environment files**: create the server's real `.env` directly on the server (via `scp`, a secrets manager, or typed manually over SSH) — **never** `git push` a real `.env`.
9. **File permissions**: `.env` should be readable only by the deploy user (`chmod 600 .env`), and the deploy user should not have unnecessary sudo rights for routine deployment tasks.

```bash
sudo mkdir -p /srv/myproject
sudo chown deploy:deploy /srv/myproject
cd /srv/myproject
git clone git@github.com:you/myproject.git .
cp .env.example .env
nano .env   # fill in real production values
chmod 600 .env
docker compose -f docker-compose.prod.yml up -d --build
```

### What should and should not be publicly exposed

```text
Public (host `ports:` mapping, reachable from the internet):
  80/443 -> Nginx only

Internal-only (Compose `expose:` or no port declaration — reachable only
by other containers on the same Compose network):
  PostgreSQL
  Redis
  RustFS
  Gunicorn (web)
  Celery worker
  Celery Beat
```

This is the culmination of the networking principle established since Stage 5: **the only thing the internet should ever be able to reach directly is Nginx.** Every other service communicates exclusively over the internal Docker network by service name.

### Verify

```bash
# from your local machine, not the server:
nmap your-server-ip   # or: for p in 22 80 443 5432 6379 9000; do nc -zv your-server-ip $p; done
# expect: 22, 80, 443 open; 5432, 6379, 9000 closed/filtered
```

```text
[ ] SSH access works with key-based auth
[ ] Firewall allows only 22/80/443 inbound
[ ] Docker and Docker Compose installed and working
[ ] Deployment directory owned by a non-root deploy user
[ ] .env exists on the server only, with restrictive permissions, never in Git
[ ] Only Nginx's ports are reachable from outside the server
```


---

<a id="stage-12"></a>
## Stage 12 — Domain and HTTPS

### Why?

**Problem:** Users need a memorable, trusted address (not a raw IP), and traffic must be encrypted so credentials, session cookies, and application data aren't sent in plaintext over the network.

### DNS

Point your domain at the server:

```text
Type    Name    Value              TTL
A       @       203.0.113.10       3600
A       www     203.0.113.10       3600
# AAAA records instead/additionally if the server has an IPv6 address
```

`server_name` in Nginx must match:

```nginx
server_name your-domain.com www.your-domain.com;
```

### HTTPS: Let's Encrypt is one option among several

There is no single mandatory way to get a TLS certificate. Pick based on your constraints:

**1. Certbot + Let's Encrypt** (free, widely used, auto-renewing)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com -d www.your-domain.com
```
Certbot obtains a certificate and can automatically edit the Nginx config to use it, plus sets up auto-renewal via a systemd timer/cron job. Good default for a self-managed server with a plain A record pointing directly at it.

**2. A certificate from another trusted CA, installed manually**

Some organizations require a specific commercial CA (procurement policy, EV certificates, internal trust requirements). You install the provided certificate/key files and reference them directly in `nginx.conf`. More manual, but avoids dependency on Let's Encrypt's infrastructure/rate limits.

**3. A reverse proxy/CDN (e.g. Cloudflare) terminating TLS in front of your server**

The CDN handles the public TLS certificate; traffic is forwarded to your Nginx over HTTP or a separate CDN-to-origin TLS connection (an "origin certificate"). This changes your architecture:

```text
Browser --HTTPS--> Cloudflare --(HTTP or origin-TLS)--> Your Nginx --> Gunicorn --> Django
```
Trade-offs: you gain DDoS protection, caching, and don't manage renewal yourself — but you now trust a third party with your traffic, must configure `ALLOWED_HOSTS`/`CSRF_TRUSTED_ORIGINS`/`SECURE_PROXY_SSL_HEADER` around *their* proxy headers (which may differ from a direct-to-origin setup), and must restrict your origin server to only accept connections from the CDN's IP ranges (or its origin certificate) to prevent people bypassing the CDN entirely.

**4. A managed load balancer / hosting provider that terminates TLS**

Common on platforms like AWS (ALB + ACM), GCP, or managed container hosting — the load balancer holds the certificate, and your server only ever receives already-decrypted HTTP. Similar architectural implications to option 3: your `SECURE_PROXY_SSL_HEADER` trust boundary is the load balancer, not your own Nginx.

None of these four is universally "correct" — the right choice depends on who controls your DNS, whether you want a third party in the traffic path, and organizational certificate requirements.

### Example Nginx HTTPS configuration (certificate-agnostic)

```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name your-domain.com www.your-domain.com;

    # Certificate paths depend on which option above you chose —
    # Certbot, a manually installed cert, or none at all if a CDN/LB
    # terminates TLS before traffic reaches this server.
    ssl_certificate     /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;

    location /static/ { alias /app/staticfiles/; }
    location /media/  { alias /app/mediafiles/; }

    location / {
        proxy_pass http://django;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Verify

```bash
dig +short your-domain.com          # should return your server's IP
curl -I http://your-domain.com      # should 301 redirect to https://
curl -I https://your-domain.com     # should return 200, valid certificate
openssl s_client -connect your-domain.com:443 -servername your-domain.com </dev/null 2>/dev/null | openssl x509 -noout -dates
```

```text
[ ] DNS A/AAAA records point to the correct server IP
[ ] HTTP requests redirect to HTTPS
[ ] HTTPS certificate is valid and matches the domain
[ ] Certificate renewal is automated (or a manual renewal process is documented) for the chosen option
[ ] If using a CDN/proxy, origin server access is restricted to the CDN's traffic only
```


---

<a id="stage-13"></a>
## Stage 13 — Database Backups

### Why?

**Problem:** A production deployment without backups isn't finished — it's a single hardware failure or `rm -rf` away from total, permanent data loss.

### Configuration

Manual/scripted `pg_dump`:

```bash
docker compose exec -T db pg_dump -U $POSTGRES_USER -d $POSTGRES_DB -F c -f /tmp/backup.dump
docker compose cp db:/tmp/backup.dump ./backups/myproject-$(date +%Y%m%d-%H%M%S).dump
```

Automated daily backup (cron on the host):

```cron
# /etc/cron.d/myproject-backup
0 3 * * * deploy /srv/myproject/scripts/backup.sh >> /var/log/myproject-backup.log 2>&1
```

`scripts/backup.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail

BACKUP_DIR="/srv/myproject/backups"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
FILE="$BACKUP_DIR/db-$TIMESTAMP.dump"

mkdir -p "$BACKUP_DIR"
docker compose -f /srv/myproject/docker-compose.prod.yml exec -T db \
    pg_dump -U "$POSTGRES_USER" -d "$POSTGRES_DB" -F c -f /tmp/backup.dump
docker compose -f /srv/myproject/docker-compose.prod.yml cp db:/tmp/backup.dump "$FILE"

# retention: keep the last 14 daily backups
find "$BACKUP_DIR" -name "db-*.dump" -mtime +14 -delete

# off-server copy — adjust to your storage target (could also target RustFS itself,
# a separate bucket, or a different provider entirely to avoid a single point of failure)
rclone copy "$FILE" remote:myproject-backups/
```

Restoring:

```bash
docker compose exec -T db pg_restore -U $POSTGRES_USER -d $POSTGRES_DB --clean --if-exists /tmp/backup.dump
```

### Explanation

- **`-F c`** (custom format) rather than plain SQL: compressed, supports selective/parallel restore, and is the format `pg_restore` expects.
- **Backup retention**: unlimited backups eventually fill your disk; a rolling window (e.g. 14 daily + a handful of weekly/monthly snapshots) balances recovery flexibility against storage cost.
- **Off-server backups**: a backup stored only on the same server it protects doesn't protect against server loss, disk failure, or a compromised host wiping everything. Copy backups to a separate location — another server, a separate object storage bucket/provider, or a managed backup service.
- **Testing restoration**: restoring should be rehearsed on a *separate* environment (a staging DB, or a throwaway container), not assumed to work.

> A backup that has never been restored/tested should not be assumed to be reliable. Schedule periodic restore drills — quarterly is a reasonable minimum for a small project.

**RustFS/object storage backups**: object storage is not automatically redundant. Depending on RustFS's configuration, consider periodic `rclone`/`mc mirror`-style syncs of the bucket to a separate location, and confirm whether RustFS itself supports any built-in replication — don't assume durability you haven't verified.

### Verify

```bash
ls -la /srv/myproject/backups/
docker compose exec -T db pg_restore --list /tmp/backup.dump | head
# on a throwaway/staging container:
docker compose exec -T db pg_restore -U test -d test_restore --clean --if-exists /tmp/backup.dump
```

```text
[ ] Automated backups run on a schedule (cron/systemd timer)
[ ] Backups are copied off the server, not just kept locally
[ ] Old backups are pruned according to a retention policy
[ ] A restore has actually been performed and verified against a test database, not just assumed to work
[ ] Object storage (RustFS) has its own backup/replication plan, separate from PostgreSQL's
```


---

<a id="stage-14"></a>
## Stage 14 — Logs and Monitoring

### Why?

**Problem:** When something breaks in production, logs are usually the only evidence of what happened. Knowing where to look, and having logs available long enough to look, matters as much as the deployment itself.

### Inspecting logs per component

```bash
docker compose logs nginx           # access/error logs, upstream connection failures
docker compose logs web             # Gunicorn access/error + Django logging output
docker compose logs celery-worker   # task execution, tracebacks
docker compose logs celery-beat     # scheduling activity
docker compose logs db              # Postgres startup, slow queries (if enabled), connection errors
docker compose logs redis           # Redis startup, memory warnings
docker compose logs rustfs          # object storage request/errors

docker compose logs -f --tail=100 web       # follow live, last 100 lines
docker compose logs --since=1h              # last hour across all services
```

### Log rotation

Docker's default `json-file` log driver grows unbounded unless configured. Set limits in Compose:

```yaml
services:
  web:
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "5"
```

Apply the same block to every service — an unbounded log file on a small VPS can fill the disk and take down the entire stack.

### Health checks and service status

```bash
docker compose ps                 # per-service state, including healthcheck status
docker compose exec db pg_isready -U $POSTGRES_USER
docker compose exec redis redis-cli ping
curl -I http://localhost/          # via Nginx, end-to-end
```

### Basic monitoring and alerts

For a small/teaching deployment, "basic" monitoring is enough to start with:

- **Uptime checks**: an external service (or a simple cron + `curl` + alert script) polling `https://your-domain.com/health/` periodically and alerting (email/Slack/etc.) on failure.
- **Disk space**: `df -h` monitored via cron; running out of disk silently breaks Postgres, Docker, and logging simultaneously.
- **Container restart counts**: `docker compose ps` showing a service repeatedly restarting indicates a crash loop worth investigating immediately, not after a user complains.

Growing beyond this typically means adopting a dedicated stack (Prometheus + Grafana, or a hosted APM/monitoring service) — a reasonable next step once the manual approach becomes tedious, and out of scope for this guide's teaching goals.

### Verify

```text
[ ] You know the exact command to view logs for each of the 7 services
[ ] Log files are size/count limited (won't fill the disk over months of operation)
[ ] `docker compose ps` is checked as part of routine operations, not just when something looks broken
[ ] Some form of external uptime check exists (even a simple cron script)
[ ] Disk usage is monitored, not just assumed to be fine
```


---

<a id="stage-15"></a>
## Stage 15 — Health Checks and Restart Policies

### Why?

**Problem:** `depends_on` in Compose controls **start order**, not **readiness**. This distinction causes a very common class of bug: `web` starts *after* `db`'s container process starts, but Postgres may still be initializing internally (running WAL recovery, applying its own startup sequence) and not yet accepting connections — so Django's first connection attempt fails, even though `db` "started first."

### The three distinct states

```text
1. Container started   — the process began running (e.g. `postgres` binary launched)
2. Service ready       — the process finished its own startup and can accept work
                          (e.g. Postgres is now accepting TCP connections)
3. Application ready   — the *dependent* service has successfully connected and
                          confirmed the dependency works (e.g. Django has run migrate
                          successfully against the database)
```

`depends_on` alone only guarantees state 1 relative to `web` starting. Getting to state 2 reliably requires a **healthcheck**; getting to state 3 requires your application/entrypoint logic to actually retry the connection.

### Configuration

```yaml
services:
  db:
    image: postgres:16-alpine
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $$POSTGRES_USER -d $$POSTGRES_DB"]
      interval: 5s
      timeout: 5s
      retries: 5
      start_period: 10s
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  web:
    build: .
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    restart: unless-stopped
```

### Explanation

- `depends_on: db: condition: service_healthy` (Compose's healthcheck-aware form) makes `web` wait until `db`'s **healthcheck** passes, not merely until the container process starts — a meaningful improvement over plain `depends_on: - db`.
- This still isn't a complete guarantee at the application layer under every failure mode (e.g. Postgres becomes healthy, then briefly drops connections during a failover in a more complex setup) — which is why a robust `entrypoint.sh` (see below) should *also* retry the actual connection with backoff, rather than assuming Compose's healthcheck alone is sufficient.
- `restart: unless-stopped`: automatically restarts a crashed container, except when you've deliberately stopped it (`docker compose stop`) — the right default for long-running production services.

### Verify

```bash
docker compose up
docker compose ps
# STATUS column should show "healthy" for db/redis before web transitions to "running"

docker compose logs web | head -20
# should NOT show repeated "connection refused" retries at startup if healthchecks are working
```

```text
[ ] db and redis define real healthchecks, not just depends_on
[ ] web waits for service_healthy, not just container-started
[ ] Application-level connection retry exists as a second layer of defense (see Entrypoint section)
[ ] restart: unless-stopped set on every long-running service
```


---

<a id="stage-16"></a>
## Stage 16 — Deployment Process

### Why?

**Problem:** Ad-hoc deployment ("SSH in and run some commands you remember") is error-prone and unrepeatable. A written, repeatable procedure prevents skipped steps.

### Procedure

```text
1. Pull latest code
2. Update environment if necessary
3. Build images
4. Start/update services
5. Run migrations
6. Run collectstatic
7. Restart/reload required services
8. Verify health
9. Check logs
```

```bash
cd /srv/myproject
git pull origin main

# 2 — only if .env.example changed; compare and update the real .env manually
diff .env.example .env || true

docker compose -f docker-compose.prod.yml build

docker compose -f docker-compose.prod.yml up -d

docker compose -f docker-compose.prod.yml exec -T web python manage.py migrate --noinput

docker compose -f docker-compose.prod.yml exec -T web python manage.py collectstatic --noinput

docker compose -f docker-compose.prod.yml restart nginx

curl -I https://your-domain.com

docker compose -f docker-compose.prod.yml logs --tail=50 web
```

### Explanation of ordering

- **Migrations run *before* the new code fully takes over traffic**, but *after* the new image is built — running them against the *old* running containers with the *new* image's migration files (via `exec` into a freshly built container, or as a dedicated one-off `run` step) avoids a window where new code expects a schema that doesn't exist yet.
- **`collectstatic` after migrate, before restarting Nginx**: new static assets need to exist in the shared volume before Nginx (which only serves what's already on disk) is asked to serve them.
- **Deliberately not running migrations automatically inside the `web` container's normal startup command** (see Entrypoint section) — with more than one `web` replica, every container restart would race to run `migrate` simultaneously, which is unsafe for some migration types (and simply wasteful even when safe). Treat `migrate` as an explicit, single, deliberate deployment step.

### What if a migration fails?

- Django wraps most migrations in a transaction (per migration, engine-dependent) — a failed migration part-way through, on a transactional-DDL-supporting database like PostgreSQL, generally rolls back cleanly, leaving the schema as it was before the attempt.
- Regardless, **do not proceed to restart application services on top of a failed migration**. Stop, inspect the error, fix the migration (or roll back the code deploy entirely), and re-run.
- For genuinely risky schema changes (large table rewrites, `NOT NULL` additions to large existing tables, renames), consider multi-step, backward-compatible migrations (add nullable column → backfill → make required in a later deploy) rather than one large migration that can fail or lock the table for an extended period under load.

### Verify

```text
[ ] Deployment is a documented, written sequence — not "whatever I remember to run"
[ ] Migrations run as a distinct, single step, not automatically on every container start
[ ] collectstatic runs after migrate, before serving new static assets
[ ] A failed migration halts the deployment rather than silently continuing
[ ] Post-deploy verification (curl + logs) is part of the routine, not skipped under time pressure
```


---

<a id="stage-17"></a>
## Stage 17 — CI/CD

### Why?

**Problem:** Manual deployment (Stage 16) is fine at small scale but doesn't catch broken code before it reaches production, and depends entirely on a human remembering every step correctly, every time.

> CI/CD is introduced **last**, deliberately — it automates the manual process from Stage 16. Understanding what's being automated matters more than the automation itself; don't treat CI/CD as a prerequisite for understanding deployment.

### A basic pipeline

```text
Git push
   |
   v
CI (e.g. GitHub Actions, GitLab CI)
   |
   +-- tests   (pytest / manage.py test)
   +-- lint    (ruff/flake8, black --check)
   +-- build   (docker build, catches Dockerfile-level breakage early)
   |
   v
Deploy   (only on merge to main/production branch, often with manual approval)
   |
   v
Production server
```

Minimal example (GitHub Actions):

```yaml
# .github/workflows/ci.yml
name: CI
on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_PASSWORD: test
          POSTGRES_DB: test
        ports: ["5432:5432"]
        options: >-
          --health-cmd pg_isready --health-interval 5s --health-retries 5
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: python manage.py test
      - run: docker build -t myproject:ci .
```

Deployment step (simplified — many real setups instead build+push an image to a registry and have the server pull it, rather than SSHing in to `git pull`):

```yaml
  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.DEPLOY_HOST }}
          username: deploy
          key: ${{ secrets.DEPLOY_SSH_KEY }}
          script: |
            cd /srv/myproject
            git pull origin main
            docker compose -f docker-compose.prod.yml build
            docker compose -f docker-compose.prod.yml up -d
            docker compose -f docker-compose.prod.yml exec -T web python manage.py migrate --noinput
            docker compose -f docker-compose.prod.yml exec -T web python manage.py collectstatic --noinput
```

### Explanation

- CI secrets (`DEPLOY_SSH_KEY`, etc.) live in the CI platform's own encrypted secrets store — the same discipline from Stage 9 applies: never commit them, rotate them if exposed.
- This pipeline is intentionally the *same steps* as Stage 16's manual procedure, just triggered automatically — which is exactly the point: automation should encode a process you already trust, not invent a new one.

### Verify

```text
[ ] Tests run automatically on every push/PR
[ ] A broken build/test fails the pipeline before it can reach production
[ ] Deployment only runs after tests pass, and only from the intended branch
[ ] CI secrets are stored in the CI platform's secret store, not in the repository
```


---

<a id="final-architecture"></a>
## Final Architecture

```text
                         Internet
                            |
                         HTTPS
                            |
                            v
                    +--------------+
                    |    Nginx     |
                    | TLS / Proxy  |
                    | Static files |
                    +------+-------+
                           |
                           v
                    +--------------+
                    |   Gunicorn   |
                    |    Django    |
                    +--+----+---+--+
                       |    |   |
          +------------+    |   +--------------+
          v                 v                  v
   +------------+     +------------+    +------------+
   | PostgreSQL |     |   Redis    |    |   RustFS   |
   |            |     |            |    | S3 Storage |
   +------------+     +-----+------+    +------------+
                             |
                     +-------+-------+
                     v               v
              +------------+  +------------+
              |   Celery   |  |   Celery   |
              |   Worker   |  |    Beat    |
              +------------+  +------------+
```

| Component | Role |
|---|---|
| **Nginx** | Public entry point. Terminates TLS, serves static/media files directly, reverse-proxies everything else to Gunicorn. Only component with a public port. |
| **Gunicorn** | WSGI application server running multiple worker processes of the Django application. |
| **Django** | The application itself — business logic, ORM, admin, views. |
| **PostgreSQL** | Primary relational datastore. Persistent volume, internal-only network access. |
| **Redis** | Message broker for Celery (and optionally Django's cache backend). Internal-only. |
| **Celery Worker** | Executes background/async tasks pulled from Redis. Horizontally scalable. |
| **Celery Beat** | Schedules periodic tasks onto Redis. Must run as exactly one instance. |
| **RustFS** | S3-compatible object storage for user-uploaded media files. Internal-only, decoupled from any single app container. |

Every arrow in this diagram is a network connection **by Compose service name**, not `localhost` — the central lesson threaded through every stage of this guide.

---

<a id="compose-structure"></a>
## Docker Compose Structure

### Services

Adapt names to your project if it already has established conventions (Stage 0); a reasonable default set:

```text
web            Django + Gunicorn
nginx          reverse proxy / static file server
db             PostgreSQL
redis          broker/cache
celery-worker  task execution
celery-beat    task scheduling
rustfs         object storage
```

### One Compose file, or several?

**Recommended approach: a base file plus environment-specific overrides**, using Compose's built-in override mechanism:

```text
docker-compose.yml          # shared service definitions (build context, networks, volume names)
docker-compose.override.yml # auto-applied in development (bind mounts, runserver, exposed DB port)
docker-compose.prod.yml     # explicit production overrides (Gunicorn command, no bind mounts, no exposed internal ports, restart policies, resource limits)
```

Development usage (override applied automatically):

```bash
docker compose up
```

Production usage (explicit file selection, override intentionally *not* auto-applied):

```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

**Why not one giant file with `environment`-conditional logic?** Compose files don't support real conditionals cleanly, and a single file trying to serve both environments tends to accumulate commented-out lines and fragile assumptions about which env vars are set. Two files that are each *fully honest* about one environment are easier to read, review, and trust than one file trying to be both.

**Why not entirely separate, non-overlapping files per environment?** That duplicates shared definitions (image names, volumes, networks), so a change to the base image or a volume name has to be made twice and can silently drift out of sync. The base + override pattern keeps shared structure in one place while making the differences explicit and small.

**Profiles** (Compose's `profiles:` key) are a good fit if you have *optional* services that not every environment needs (e.g. a local mail-catcher like MailHog only in dev) — less relevant to the dev/prod split itself, but worth knowing about for exactly that use case.


---

<a id="dockerfile"></a>
## Production Dockerfile

```dockerfile
# ---- Build stage: install dependencies with build tools available ----
FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ---- Final stage: slim runtime image, no build tools ----
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH=/root/.local/bin:$PATH

# libpq5 (runtime client lib) is needed even without build tools, for psycopg2 to work
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home --uid 1000 appuser
WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY --chown=appuser:appuser . .

USER appuser

RUN python manage.py collectstatic --noinput --settings=config.settings.prod || true
# ^ "|| true" only if collectstatic can safely run without DB/secret access at build time;
#   if it requires real secrets/DB, run it as a deploy-time step instead (Stage 16), not at build time.

EXPOSE 8000

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "myproject.wsgi:application", "-c", "gunicorn.conf.py"]
```

### Explanation

- **Multi-stage build, and why it's used here**: the `builder` stage has `build-essential`/`libpq-dev` (compilers, headers) needed only to *install* Python packages with C extensions. The final stage copies just the installed packages (`/root/.local`) and drops the build tools entirely — a meaningfully smaller, lower-attack-surface final image. If your project has no C-extension dependencies at all, a single-stage build is simpler and this complexity isn't justified — introduce multi-stage only once you've confirmed you need it.
- **Non-root user (`appuser`)**: matches Stage 10's hardening — the running process can't modify files it doesn't own or perform host-level actions requiring root, limiting damage from a compromised process.
- **`collectstatic` at build time**: reasonable *if* it doesn't require database access or runtime secrets — bakes static files directly into the image, so no extra deploy step is needed for them. If your project's `collectstatic` process depends on settings that require a live DB connection or real secrets unavailable at build time, move this to the Stage 16 deploy sequence instead, and don't try to force it into the image build.
- **`ENTRYPOINT` + `CMD`**: the entrypoint script (next section) runs first for every container using this image (startup checks), then executes whatever `CMD` was specified — which differs between `web`, `celery-worker`, and `celery-beat` even though they share this exact image.


---

<a id="entrypoint"></a>
## Entrypoint / Startup Scripts

`entrypoint.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail

# Wait for the database to actually accept connections — a second layer of
# defense beyond Compose's `condition: service_healthy` (Stage 15), because
# entrypoint scripts run inside the container and shouldn't assume the outer
# orchestration layer's healthcheck timing is perfectly synchronized.
echo "Waiting for database..."
until python - <<'PYEOF'
import os, sys, time
import psycopg2
try:
    psycopg2.connect(
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        host=os.environ["POSTGRES_HOST"],
        port=os.environ.get("POSTGRES_PORT", "5432"),
    ).close()
except Exception:
    sys.exit(1)
PYEOF
do
  echo "Database unavailable, retrying in 2s..."
  sleep 2
done
echo "Database is up."

exec "$@"
```

### What belongs here, and what does NOT

**Belongs in the entrypoint:**
- Waiting/retrying for genuinely required dependencies (database reachability) before starting the main process.
- Anything that must happen identically, every single time this specific container starts (e.g. validating a required env var is set).

**Does NOT belong in the entrypoint:**
- **`python manage.py migrate`** — if every container using this image (potentially several `web` replicas, plus `celery-worker`, plus `celery-beat`, all sharing this entrypoint) ran migrations on every startup, you'd get multiple concurrent `migrate` invocations racing against each other. Some Django migrations are safe under concurrent execution; others (certain schema changes, especially on databases without strong DDL transactional guarantees) are not, and even when technically safe, running `migrate` several times simultaneously is wasteful and makes deploy timing unpredictable. **Migrations are a deliberate, single, explicit deployment step** (Stage 16), run once, by a human or CI pipeline — never automatically inside routine container startup.
- **`collectstatic`** — same reasoning; either bake it into the image at build time (previous section) or run it once as a deploy step, not on every container start.
- Long-running side effects that aren't idempotent.

Compose usage — the same entrypoint, different final commands:

```yaml
services:
  web:
    entrypoint: ["/entrypoint.sh"]
    command: ["gunicorn", "myproject.wsgi:application", "-c", "gunicorn.conf.py"]

  celery-worker:
    entrypoint: ["/entrypoint.sh"]
    command: ["celery", "-A", "myproject", "worker", "--loglevel=info"]

  celery-beat:
    entrypoint: ["/entrypoint.sh"]
    command: ["celery", "-A", "myproject", "beat", "--loglevel=info",
               "--scheduler", "django_celery_beat.schedulers:DatabaseScheduler"]
```

### Verify

```text
[ ] Entrypoint waits for the database before starting the main process
[ ] Entrypoint does NOT run migrate or collectstatic automatically
[ ] The same entrypoint script is reused across web/worker/beat, with only `command` differing
[ ] A deliberately-stopped database causes the entrypoint to retry visibly in logs, not crash-loop silently
```


---

<a id="static-media"></a>
## Static and Media Files

### Static files

```text
CSS
JavaScript
Images shipped with the application (icons, logos)
Django admin's built-in static files
```

- Don't change per deployment except when you ship new code.
- Collected via `collectstatic` into `STATIC_ROOT`, served directly by Nginx from the `static_volume` — never touches Django/Gunicorn at request time.
- Safe to treat as fully public, cacheable, and versioned alongside your code.

### Media files

```text
User-uploaded content — profile pictures, documents, attachments, generated reports, etc.
```

- Change constantly, at runtime, independent of deployments.
- Must survive container replacement and (ideally) work correctly with more than one `web` replica simultaneously — which is exactly why Stage 7 moved these to RustFS instead of local disk/a Docker volume tied to one container.
- May need access control (signed URLs, private buckets) depending on the application — don't assume all media should be public just because static assets are.

### Why the distinction matters operationally

| | Static | Media |
|---|---|---|
| Changes | On deploy only | Continuously, at runtime |
| Ownership | Part of the codebase | User-generated data |
| Storage | Local volume, served by Nginx | RustFS (S3-compatible), decoupled from any one container |
| Backup | Implicit (it's in Git/the image) | Explicit backup required (Stage 13) — this is real, irreplaceable user data |
| Public/private | Almost always public | Application-specific decision |

Mixing the two — for example, routing static assets through the S3 API "to keep things consistent," or leaving media files on local disk "because it's simpler for now" — trades away either performance (static via S3 adds needless latency) or durability/scalability (media on local disk breaks under multiple replicas and redeploys). Keep the distinction explicit in both configuration and in how you reason about backups.


---

<a id="networking"></a>
## Networking Reference

```text
web     -> db:5432          (Django ORM queries)
web     -> redis:6379       (enqueuing Celery tasks / cache reads-writes, if used)
web     -> rustfs:9000      (reading/writing media via the S3 API)
nginx   -> web:8000         (proxying dynamic requests to Gunicorn)
celery-worker -> redis:6379 (consuming tasks from the queue)
celery-worker -> db:5432    (task code that touches the ORM)
celery-worker -> rustfs:9000 (task code that reads/writes media, e.g. generating a report file)
celery-beat   -> redis:6379 (enqueuing scheduled tasks)
```

**Why service names instead of `localhost`:** Docker Compose creates a private network per project and registers each service's name as a resolvable hostname *on that network*, pointing to that service's container. `localhost`/`127.0.0.1` inside any container refers only to that container's own loopback interface — never to another container, and not to the host machine either (from inside a container, without special configuration). This is true regardless of how many services you add: the resolution mechanism is Docker's internal DNS, keyed by service name, not by any port mapping to the host.

A useful mental model: **"Am I talking to something in the same container as me? Use `localhost`. Am I talking to a different service? Use its Compose service name."** Port mappings to the host (`ports: "80:80"`) exist only for things *outside* Docker (your browser, `curl` from the host) to reach a container — they are irrelevant to container-to-container communication.


---

<a id="troubleshooting"></a>
## Troubleshooting

### Django cannot connect to PostgreSQL

Possible causes:
- Wrong hostname — using `localhost` instead of the Compose service name (`db`).
- Wrong port — mismatched `POSTGRES_PORT` between Django's settings and the `db` service.
- Credentials — `POSTGRES_USER`/`POSTGRES_PASSWORD` mismatch, especially after changing `.env` without recreating the Postgres volume (Postgres only applies these on first initialization of an empty volume).
- Database not ready yet — missing or misconfigured healthcheck (Stage 15).
- Docker network problem — `web` and `db` not on the same Compose network (rare with a single `docker-compose.yml`, more likely with manually customized networks).

```bash
docker compose exec web python -c "import socket; socket.create_connection(('db', 5432), timeout=3)"
docker compose exec db pg_isready -U $POSTGRES_USER
```

### Nginx returns 502

Possible causes:
- Gunicorn/`web` isn't running (crashed, still starting, or failed healthcheck).
- Wrong `upstream` hostname/port in `nginx.conf` (doesn't match the Compose service name/port).
- Docker networking problem — `nginx` and `web` not on the same network.

```bash
docker compose ps web
docker compose logs web
docker compose exec nginx wget -qO- http://web:8000 || echo "cannot reach web from nginx"
```

### Static files return 404

Possible causes:
- `collectstatic` was never run (or ran before the volume existed).
- `STATIC_ROOT` in Django doesn't match the path Nginx's `alias` points to.
- Nginx config wasn't reloaded after a change.
- Volume mismatch — `web` and `nginx` mounting *different* volumes instead of the same `static_volume`.

```bash
docker compose exec web python manage.py collectstatic --noinput
docker compose exec nginx ls /app/staticfiles | head
```

### Celery tasks don't execute

Possible causes:
- Worker container isn't running.
- Wrong `CELERY_BROKER_URL` (host mismatch, wrong Redis DB index).
- Broker connection issue — Redis unreachable or requires auth not configured.
- Task import/configuration issue — task not discovered (`autodiscover_tasks()` not finding it, or a typo in the task's dotted path).

```bash
docker compose logs celery-worker
docker compose exec web python manage.py shell -c "
from myproject.celery import app
print(app.control.inspect().active())
"
```

### Celery Beat doesn't schedule tasks

Possible causes:
- Beat container isn't running.
- Timezone/configuration issue — `CELERY_TIMEZONE` not matching Django's `TIME_ZONE`.
- Wrong schedule — cron-style expression or interval misconfigured.
- **Multiple Beat instances running simultaneously** — causes duplicate/erratic scheduling; Beat must be a singleton.

```bash
docker compose logs celery-beat
docker compose ps celery-beat   # confirm exactly one instance
```

### Uploaded files fail

Possible causes:
- Incorrect S3 endpoint (internal vs. public URL confusion — see Stage 7).
- Wrong access/secret key.
- Bucket doesn't exist (must be created explicitly in RustFS).
- RustFS container unavailable/unhealthy.
- Incorrect Django storage configuration (`STORAGES`/`AWS_*` settings).

```bash
docker compose logs rustfs
docker compose exec web python manage.py shell -c "
from django.core.files.storage import default_storage
print(default_storage.exists('some/known/file.txt'))
"
```

### HTTPS problems

Possible causes:
- DNS incorrect — A/AAAA record doesn't point at the server, or hasn't propagated yet.
- Certificate issue — expired, wrong domain, chain incomplete.
- Nginx configuration — `server_name` mismatch, wrong certificate paths.
- Proxy/CDN configuration — origin/edge certificate mismatch if using Cloudflare or similar.
- HTTP/HTTPS mismatch — mixed content, or `SECURE_SSL_REDIRECT`/`SECURE_PROXY_SSL_HEADER` misconfigured relative to where TLS is actually terminated.

```bash
dig +short your-domain.com
openssl s_client -connect your-domain.com:443 -servername your-domain.com </dev/null 2>/dev/null | openssl x509 -noout -dates -subject
docker compose exec nginx nginx -t   # validates nginx config syntax
```


---

<a id="checklist"></a>
## Verification Checklist

Use this as a final pre-launch and post-deploy sanity pass. Each item traces back to a specific stage above — if something fails, revisit that stage's "Common Problems" section.

```text
[ ] Django container starts                                (Stage 2)
[ ] PostgreSQL accepts connections                          (Stage 3)
[ ] Migrations work                                          (Stage 3, 16)
[ ] Gunicorn responds                                        (Stage 4)
[ ] Nginx proxies correctly                                  (Stage 5)
[ ] Static files work                                        (Stage 5)
[ ] Celery worker executes a task                            (Stage 6)
[ ] Celery Beat schedules a task                              (Stage 6)
[ ] RustFS accepts uploads                                   (Stage 7)
[ ] Production settings load                                 (Stage 8)
[ ] DEBUG=False                                               (Stage 10)
[ ] Domain resolves                                           (Stage 12)
[ ] HTTPS works                                                (Stage 12)
[ ] Database backup works                                     (Stage 13)
[ ] Backup restoration has been tested                        (Stage 13)
[ ] Only Nginx has a public port; db/redis/rustfs/web are internal-only  (Stage 10, 11)
[ ] Log rotation configured for every service                 (Stage 14)
[ ] Healthchecks + service_healthy conditions in place        (Stage 15)
[ ] Deployment procedure is written down and repeatable       (Stage 16)
[ ] `manage.py check --deploy` passes clean                   (Stage 10)
```


---

<a id="additional"></a>
## Additional Recommendations

The staged architecture above covers a complete, working, reasonably secure deployment — but production operation raises a few more concerns worth knowing about, even if some are beyond this guide's immediate teaching scope.

**Docker secrets / secrets manager beyond `.env`.** A plain `.env` file on one VPS is fine for a small/teaching deployment, but it's a single unencrypted file readable by anyone with host access. Larger or more sensitive deployments benefit from Docker Swarm/Kubernetes secrets, or a dedicated secrets manager (Vault, cloud provider secret stores) — encrypted at rest, access-audited, and rotatable without editing a file by hand.

**Resource limits on containers.** Without limits, one runaway process (a memory leak in a Celery task, an inefficient query flooding Postgres) can starve every other service on the same host. Compose supports basic limits:
```yaml
services:
  celery-worker:
    deploy:
      resources:
        limits:
          memory: 512M
```
This matters because a single misbehaving container shouldn't be able to take down the database or Nginx by exhausting shared host memory.

**Database connection pooling.** Django opens a new connection per request by default unless `CONN_MAX_AGE` (already set in Stage 8's `prod.py`) is used, or a dedicated pooler (PgBouncer) sits in front of Postgres. Under real concurrent load, connection pooling meaningfully reduces Postgres's connection overhead — worth introducing once you observe connection-count pressure, not necessarily on day one.

**Redis persistence, precisely.** Stage 6 flagged this as a decision point; explicitly deciding between no persistence (pure cache/ephemeral broker, accept losing queued-but-unexecuted tasks on crash), RDB snapshots, or AOF (append-only file, more durable but higher I/O) matters more than it might seem, because the default behavior differs by Redis image/config and silently assuming "it's probably persisted" is a common gap.

**Celery task retry policies.** By default, a task that raises an exception simply fails — it does not automatically retry. For tasks where transient failure is expected (a flaky third-party API call), define `autoretry_for` / `retry_backoff` explicitly rather than assuming Celery retries by default.

**Graceful shutdown.** Gunicorn and Celery workers should be given time to finish in-flight requests/tasks before being killed during a deploy or restart (`graceful_timeout` in `gunicorn.conf.py`, `--time-limit`/warm shutdown handling in Celery). Without this, a deploy can silently kill a task or request mid-execution, leaving partial work behind.

**Deployment rollback strategy.** Stage 16 covers forward deployment; it's equally important to know, in advance, how to roll back — reverting to a previous Docker image tag and, if a migration was involved, whether it has a safe reverse migration or requires a restore from backup. Decide this *before* you need it under pressure, not during an incident.

**Zero/minimal-downtime deployment.** The Stage 16 procedure has a brief window where `nginx restart` (or `web` container replacement) interrupts traffic. For a teaching deployment this is usually acceptable; for a real service, blue-green deployment or rolling container replacement (starting new containers, health-checking them, then routing traffic away from old ones before stopping them) removes even that brief interruption — a natural next step once the basic deploy is solid.

**Image versioning and dependency pinning.** `requirements.txt` entries in this guide are pinned to specific versions deliberately — an unpinned `django` or `celery` dependency can silently pull in a breaking change on the next `pip install`/rebuild. Similarly, tag your own built images with a specific version/commit SHA rather than only `latest`, so you can always identify and roll back to exactly what was previously running.

**Vulnerability scanning / Docker image security.** Periodically scan images for known CVEs (`docker scout`, Trivy, or your registry's built-in scanning) — base images and dependencies accumulate known vulnerabilities over time even if your own code never changes.

**Nginx security headers.** Beyond TLS itself, headers like `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY` (or `Content-Security-Policy: frame-ancestors 'none'`), and a reasonable `Content-Security-Policy` reduce the impact of certain client-side attack classes (clickjacking, MIME-sniffing exploits). Worth adding once the core deployment is stable.

**CORS and CSRF, if the app is consumed by a separate frontend origin.** If a JavaScript frontend on a different domain calls this Django app's API, `django-cors-headers` and `CSRF_TRUSTED_ORIGINS` need explicit, deliberate configuration — an overly permissive CORS policy (`*` with credentials) is a common, serious misconfiguration.

**File upload restrictions.** Beyond `client_max_body_size` in Nginx (Stage 5), consider validating file type/size at the Django layer too (don't trust the client-supplied `Content-Type`), and be deliberate about whether uploaded files are ever executed or served in a way that could allow stored XSS via an uploaded HTML/SVG file.

**Server resource monitoring and disaster recovery, tied together.** Stage 14 covers basic monitoring; the other half of that story is having an actual, written disaster recovery plan — if the entire VPS is lost, what's the concrete sequence of steps (provision a new server, restore from off-server backups, reconfigure DNS) to bring the service back, and roughly how long would that realistically take? Knowing the answer before an incident, rather than during one, is the actual point of Stage 13's backups.

Not every item above needs to be implemented on day one of a teaching deployment — but a student who can explain *why* each one matters, and consciously choose to defer it, has a genuinely production-aware understanding of the system, which was the goal of this guide from the start.
