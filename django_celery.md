# Celery with Django 6 - Quick Start Guide

## Overview

While Django 6 includes a built-in tasks framework, **Celery remains the production-grade solution** for complex background task processing. This guide shows you how to integrate Celery with Django 6.

## Why Use Celery?

- ✅ **Production-ready**: Battle-tested at massive scale
- ✅ **Advanced features**: Task chains, groups, chords
- ✅ **Periodic tasks**: Built-in scheduler (Celery Beat)
- ✅ **Monitoring**: Flower web interface
- ✅ **Retry logic**: Automatic with backoff
- ✅ **Rate limiting**: Control task execution rates
- ✅ **Multiple brokers**: Redis, RabbitMQ, SQS

## Quick Setup (5 Steps)

### Step 1: Install Dependencies

```bash
# Install Django 6 and Celery with Redis
pip install django>=6.0
pip install celery[redis]
pip install redis

# Optional: Store results in Django database
pip install django-celery-results
```

### Step 2: Create Celery App

Create `proj/celery.py` (replace `proj` with your project name):

```python
import os
from celery import Celery

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

# Create Celery app
app = Celery('proj')

# Load config from Django settings (prefix: CELERY_)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks from all installed apps
app.autodiscover_tasks()
```

### Step 3: Make Celery Importable

Edit `proj/__init__.py`:

```python
from .celery import app as celery_app

__all__ = ('celery_app',)
```

### Step 4: Configure Django Settings

Add to `settings.py`:

```python
# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60  # 30 minutes
```

### Step 5: Define Your First Task

Create `myapp/tasks.py`:

```python
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email, username):
    send_mail(
        subject=f"Welcome, {username}!",
        message="Thanks for joining!",
        from_email="noreply@example.com",
        recipient_list=[user_email],
    )
    return f"Email sent to {user_email}"
```

## Running Celery

### Start Redis (message broker)

```bash
# Using Docker
docker run -d -p 6379:6379 redis:7-alpine

# Or install Redis locally
# macOS: brew install redis && redis-server
# Ubuntu: sudo apt install redis-server && redis-server
```

### Start Celery Worker

```bash
# Terminal 1: Django server
python manage.py runserver

# Terminal 2: Celery worker
celery -A proj worker --loglevel=info

# Development with auto-reload
celery -A proj worker --loglevel=info --pool=solo --reload
```

You should see:

```
-------------- celery@hostname v5.x.x
--- ***** -----
-- ******* ---- [config]
- *** --- * --- broker: redis://localhost:6379/0
- ** ---------- result: redis://localhost:6379/0
- ** ---------- [tasks]
- ** ----------   myapp.tasks.send_welcome_email
```

## Using Tasks in Views

```python
# views.py
from django.http import JsonResponse
from .tasks import send_welcome_email

def register(request):
    email = request.POST['email']
    username = request.POST['username']
    
    # Queue the task
    task = send_welcome_email.delay(email, username)
    
    return JsonResponse({
        'task_id': task.id,
        'status': 'queued'
    })
```

## Checking Task Status

```python
from celery.result import AsyncResult

def check_task(request, task_id):
    task = AsyncResult(task_id)
    
    return JsonResponse({
        'state': task.state,  # PENDING, STARTED, SUCCESS, FAILURE
        'ready': task.ready(),
        'result': task.result if task.successful() else None,
        'error': str(task.info) if task.failed() else None,
    })
```

## Common Task Patterns

### 1. Task with Retry

```python
@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def send_notification(self, user_id, message):
    try:
        # Send notification
        user = User.objects.get(id=user_id)
        send_mail(...)
        return "Success"
    except Exception as exc:
        # Retry after 60 seconds
        raise self.retry(exc=exc)
```

### 2. Task with Exponential Backoff

```python
@shared_task(bind=True, max_retries=5)
def process_payment(self, payment_id):
    try:
        # Process payment
        payment = Payment.objects.get(id=payment_id)
        process(payment)
        return "Success"
    except Exception as exc:
        # Retry with exponential backoff: 5s, 25s, 125s...
        countdown = 5 ** self.request.retries
        raise self.retry(exc=exc, countdown=countdown)
```

### 3. Task with Progress Updates

```python
@shared_task(bind=True)
def generate_report(self, report_id):
    report = Report.objects.get(id=report_id)
    
    for i in range(1, 11):
        # Update progress
        self.update_state(
            state='PROGRESS',
            meta={'current': i, 'total': 10}
        )
        # Do work
        time.sleep(1)
    
    return {'report_id': report_id, 'status': 'complete'}
```

Check progress:

```python
def check_progress(request, task_id):
    task = AsyncResult(task_id)
    
    if task.state == 'PROGRESS':
        return JsonResponse({
            'state': 'PROGRESS',
            'progress': task.info  # {'current': 5, 'total': 10}
        })
    elif task.ready():
        return JsonResponse({
            'state': 'COMPLETE',
            'result': task.result
        })
```

### 4. Rate Limited Task

```python
@shared_task(rate_limit='10/m')  # Max 10 per minute
def send_sms(phone, message):
    # Send SMS
    return f"SMS sent to {phone}"
```

## Advanced Features

### Task Chains (Sequential)

```python
from celery import chain

# Execute tasks in sequence
workflow = chain(
    process_step1.s(data),
    process_step2.s(),  # Gets result from step1
    process_step3.s(),  # Gets result from step2
)
result = workflow.apply_async()
```

### Task Groups (Parallel)

```python
from celery import group

# Execute tasks in parallel
job = group(
    process_item.s(item1),
    process_item.s(item2),
    process_item.s(item3),
)
result = job.apply_async()

# Wait for all to complete
results = result.get()
```

### Chord (Group + Callback)

```python
from celery import chord

# Process items in parallel, then run callback
workflow = chord(
    (process_item.s(item) for item in items),
    send_summary_email.s()  # Called with all results
)
result = workflow.apply_async()
```

## Periodic Tasks (Celery Beat)

### Install Celery Beat

```bash
pip install celery[beat]
```

### Configure Periodic Tasks

```python
# settings.py
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    # Run daily at midnight
    'cleanup-old-data': {
        'task': 'myapp.tasks.cleanup_old_data',
        'schedule': crontab(hour=0, minute=0),
    },
    
    # Run every 10 minutes
    'health-check': {
        'task': 'myapp.tasks.check_health',
        'schedule': 600.0,  # seconds
    },
    
    # Run every Monday at 9 AM
    'weekly-report': {
        'task': 'myapp.tasks.generate_weekly_report',
        'schedule': crontab(hour=9, minute=0, day_of_week=1),
    },
}
```

### Define Periodic Task

```python
# tasks.py
@shared_task
def cleanup_old_data():
    """Runs daily at midnight"""
    from datetime import timedelta
    cutoff = timezone.now() - timedelta(days=30)
    deleted = OldData.objects.filter(created__lt=cutoff).delete()
    return f"Deleted {deleted[0]} records"
```

### Start Celery Beat

```bash
# Terminal 3: Celery Beat scheduler
celery -A proj beat --loglevel=info
```

## Monitoring with Flower

### Install Flower

```bash
pip install flower
```

### Start Flower

```bash
celery -A proj flower
```

Access at: **http://localhost:5555**

Features:
- Real-time task monitoring
- Task history and statistics
- Worker status
- Task rate graphs
- Restart/shutdown workers

## Multiple Queues

### Define Queues

```python
# settings.py
CELERY_TASK_ROUTES = {
    'myapp.tasks.send_email': {'queue': 'emails'},
    'myapp.tasks.process_image': {'queue': 'media'},
    'myapp.tasks.generate_report': {'queue': 'reports'},
}
```

### Start Workers for Specific Queues

```bash
# Worker 1: High-priority emails
celery -A proj worker -Q emails --loglevel=info

# Worker 2: Media processing
celery -A proj worker -Q media --loglevel=info

# Worker 3: Default queue
celery -A proj worker -Q default --loglevel=info
```

## Production Deployment

### Using Supervisor

```ini
; /etc/supervisor/conf.d/celery.conf
[program:celery]
command=/path/to/venv/bin/celery -A proj worker --loglevel=info
directory=/path/to/project
user=www-data
numprocs=1
stdout_logfile=/var/log/celery/worker.log
stderr_logfile=/var/log/celery/worker.log
autostart=true
autorestart=true
startsecs=10
stopwaitsecs=600
```

### Using Systemd

```ini
# /etc/systemd/system/celery.service
[Unit]
Description=Celery Service
After=network.target

[Service]
Type=forking
User=www-data
Group=www-data
WorkingDirectory=/path/to/project
ExecStart=/path/to/venv/bin/celery multi start w1 \
    -A proj --pidfile=/var/run/celery/%n.pid \
    --logfile=/var/log/celery/%n%I.log --loglevel=info
ExecStop=/path/to/venv/bin/celery multi stopwait w1 \
    --pidfile=/var/run/celery/%n.pid
ExecReload=/path/to/venv/bin/celery multi restart w1 \
    -A proj --pidfile=/var/run/celery/%n.pid \
    --logfile=/var/log/celery/%n%I.log --loglevel=info

[Install]
WantedBy=multi-user.target
```

### Docker Compose

```yaml
version: '3.8'

services:
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0
    depends_on:
      - redis

  celery:
    build: .
    command: celery -A proj worker --loglevel=info
    volumes:
      - .:/app
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0
    depends_on:
      - redis

  celery_beat:
    build: .
    command: celery -A proj beat --loglevel=info
    volumes:
      - .:/app
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0
    depends_on:
      - redis

  flower:
    build: .
    command: celery -A proj flower
    ports:
      - "5555:5555"
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0
    depends_on:
      - redis
```

Start with: `docker-compose up`

## Testing

```python
# test_tasks.py
from django.test import TestCase, override_settings

@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
class TaskTests(TestCase):
    """Tasks run synchronously in tests"""
    
    def test_welcome_email(self):
        result = send_welcome_email.delay('test@example.com', 'test')
        
        self.assertTrue(result.successful())
        self.assertIn('Email sent', result.result)
```

## Best Practices

1. **Use `@shared_task`** instead of `@app.task` for reusability
2. **Set time limits** to prevent hanging tasks
3. **Implement retries** for unreliable operations
4. **Use exponential backoff** for external APIs
5. **Monitor tasks** with Flower in production
6. **Use multiple queues** to prioritize tasks
7. **Clean up old results** regularly
8. **Test with `CELERY_TASK_ALWAYS_EAGER=True`**

## Troubleshooting

### Tasks Not Running

✅ Check Redis is running: `redis-cli ping` (should return PONG)  
✅ Check Celery worker is running  
✅ Check task is discovered: Look for task name in worker startup  
✅ Check Django settings: CELERY_BROKER_URL correct?

### Tasks Failing Silently

✅ Check worker logs: `celery -A proj worker --loglevel=debug`  
✅ Check task code for exceptions  
✅ Enable task tracking: `CELERY_TASK_TRACK_STARTED = True`

### Performance Issues

✅ Increase worker concurrency: `celery -A proj worker --concurrency=8`  
✅ Use multiple workers for different queues  
✅ Optimize task code  
✅ Consider using prefork pool for CPU-bound tasks

## Celery vs Django 6 Tasks

| Feature | Celery | Django 6 Tasks |
|---------|--------|----------------|
| Production Ready | ✅ Yes | ⚠️ Limited backends |
| Task Chains | ✅ Yes | ❌ No |
| Periodic Tasks | ✅ Beat | ❌ No |
| Monitoring | ✅ Flower | ⚠️ Basic |
| Retry Logic | ✅ Automatic | ⚠️ Manual |
| Setup Complexity | ⚠️ Moderate | ✅ Simple |
| Ecosystem | ✅ Mature | 🔄 Emerging |

## Recommendation

**For Django 6 Projects:**
- Use **Celery** for production applications (now)
- Monitor Django tasks ecosystem development
- Consider migration path when Celery backend emerges for django.tasks

**Future Vision:**
The Django community expects future Celery backends for django.tasks, allowing:
- Define tasks with `@task` (Django API)
- Execute with Celery workers
- Best of both worlds!

## Resources

- [Celery Documentation](https://docs.celeryq.dev)
- [Django + Celery Tutorial](https://realpython.com/asynchronous-tasks-with-django-and-celery/)
- [Flower Documentation](https://flower.readthedocs.io)
- [Django 6 Tasks](https://docs.djangoproject.com/en/6.0/topics/tasks/)
