

## Django Database Configuration (Persistent Connections)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'app_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
        'CONN_MAX_AGE': 60,          # Close connection after 60 seconds of inactivity
        'CONN_HEALTH_CHECKS': True,  # Reconnect automatically if the connection is broken
    }
}
```

### What this configuration does

* Django keeps one database connection **per worker process**
* The connection is reused for multiple requests
* After 60 seconds of inactivity, the connection is closed
* Health checks ensure stale or broken connections are recreated

This improves performance compared to opening a new connection per request.

---

## Important clarification: Django does NOT provide a real connection pool

Django’s connection handling is **not a true connection pool**.

* Each worker process maintains its **own database connection**
* Connections are **not shared across workers**
* There is no centralized control, queueing, or global limit

In a real pool, connections are shared across all workers and requests.

---

## Why PgBouncer is required for real pooling

PgBouncer provides a **true, shared connection pool** by running outside Django.

### Architecture

```
Django workers → PgBouncer → PostgreSQL
```

### What PgBouncer does

* Maintains a real pool of database connections
* Reuses connections efficiently
* Queues requests when the pool is exhausted
* Reduces the total number of connections seen by PostgreSQL

### Typical setup

```
Django (20 client connections) → PgBouncer (5 real DB connections)
```

PostgreSQL only sees 5 connections instead of 20.

---

## How Django gets true pooling with PgBouncer

PgBouncer sits between Django and PostgreSQL and handles:

* Connection pooling
* Connection reuse
* Queueing
* Timeouts
* Load control

Django connections become lightweight client connections.

---

## Production-oriented guide: PgBouncer with Django

This setup reflects how PgBouncer is used in real production systems.

---

## 1. Why PgBouncer with Django

PgBouncer provides Django with a **true connection pool** and protects PostgreSQL from excessive connections.

---

## 2. Install PgBouncer (Ubuntu / Debian)

```bash
sudo apt update
sudo apt install pgbouncer
```

Verify installation:

```bash
pgbouncer --version
```

---

## 3. PgBouncer configuration (`pgbouncer.ini`)

Location:

```
/etc/pgbouncer/pgbouncer.ini
```

### Minimal and safe production configuration

```ini
[databases]
mydb = host=127.0.0.1 port=5432 dbname=mydb

[pgbouncer]
listen_addr = 127.0.0.1
listen_port = 6432

auth_type = md5
auth_file = /etc/pgbouncer/userlist.txt

pool_mode = transaction

max_client_conn = 200
default_pool_size = 20
reserve_pool_size = 5
reserve_pool_timeout = 5

server_idle_timeout = 60
server_lifetime = 300

log_connections = 1
log_disconnections = 1
```

### Key settings explained

| Setting                   | Description                           |
| ------------------------- | ------------------------------------- |
| `pool_mode = transaction` | Required for Django                   |
| `listen_port = 6432`      | Port Django connects to               |
| `default_pool_size`       | Actual PostgreSQL connections         |
| `max_client_conn`         | Max Django + other client connections |

---

## 4. Create PgBouncer users

Create the user list file:

```bash
sudo nano /etc/pgbouncer/userlist.txt
```

Format:

```
"dbuser" "md5<md5(password+username)>"
```

Generate the MD5 password hash:

```sql
SELECT 'md5' || md5('password' || 'dbuser');
```

Example:

```
"django_user" "md5e99a18c428cb38d5f260853678922e03"
```

---

## 5. PostgreSQL user permissions

```sql
CREATE USER django_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE mydb TO django_user;
```

---

## 6. Django settings when using PgBouncer (Critical)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'django_user',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '6432',      # PgBouncer port
        'CONN_MAX_AGE': 0,   # Important
    }
}
```

### Why `CONN_MAX_AGE = 0`

* PgBouncer manages pooling
* Django must release connections after each request
* Prevents transaction state conflicts

---

## 7. Transaction handling in Django (Very important)

PgBouncer runs in **transaction pooling mode**.

### Do not use

* Server-side cursors
* Persistent transactions across requests
* `ATOMIC_REQUESTS = True`

### Correct usage

```python
from django.db import transaction

def view():
    with transaction.atomic():
        ...
```

---

## 8. Start and enable PgBouncer

```bash
sudo systemctl restart pgbouncer
sudo systemctl enable pgbouncer
```

Check status:

```bash
sudo systemctl status pgbouncer
```

---

## 9. Verify PgBouncer

Connect via PgBouncer:

```bash
psql -h 127.0.0.1 -p 6432 -U django_user mydb
```

PgBouncer admin console:

```bash
psql -h 127.0.0.1 -p 6432 -U django_user pgbouncer
```

Useful commands:

```sql
SHOW POOLS;
SHOW CLIENTS;
SHOW SERVERS;
```

---

## 10. Common mistakes to avoid

* Using `pool_mode = session`
* Forgetting to change Django’s port to PgBouncer
* Setting `CONN_MAX_AGE > 0`
* Using long-running transactions
* Incorrect MD5 format in `userlist.txt`

---

## 11. Recommended starting values

| Component                  | Value   |
| -------------------------- | ------- |
| Gunicorn workers           | CPU × 2 |
| PgBouncer pool size        | 10–20   |
| PostgreSQL max_connections | 100     |
| Django `CONN_MAX_AGE`      | 0       |

---

## 12. Mental model

```
Django → PgBouncer (real pool) → PostgreSQL
```

* Django: no real pooling
* PgBouncer: true pooling, queueing, protection

---

## Final takeaway

**When using PgBouncer, Django must not manage persistent database connections.**
