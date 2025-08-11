# **Lead Management System** using Django and Django Templates

1. **Core features & requirements**
2. **Database models**
3. **User roles & permissions**
4. **Views & templates**
5. **Project structure**
6. **Step-by-step development plan**
7. **Extra considerations** (security, scalability, enhancements)

---

## 1. Core Features & Requirements

A **Lead Management System (LMS)** is a tool for tracking and managing potential customers (leads) through different sales pipeline stages.
Here’s what your Django app should handle:

### **Must-have**

- User authentication (Admin, Sales Manager, Sales Executive)
- Dashboard showing lead stats (new, contacted, converted, lost)
- Lead CRUD (Create, Read, Update, Delete)
- Lead assignment to team members
- Lead status tracking (New, In Progress, Converted, Lost)
- Search & filter leads
- Notes/comments per lead
- Upload documents/images related to a lead
- Activity logging (who did what, when)

### **Optional (can add later)**

- Email integration (send follow-up from system)
- Lead import/export (CSV/Excel)
- Notifications (email or in-app)
- Kanban-style lead pipeline view
- Reporting & analytics

---

## 2. Database Models

### **User Model**

- Extend `AbstractUser` for custom fields if needed (e.g., role, phone)
- Roles: `"admin"`, `"sales_manager"`, `"sales_executive"`

### **Lead**

```python
class Lead(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("in_progress", "In Progress"),
        ("converted", "Converted"),
        ("lost", "Lost"),
    ]
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    source = models.CharField(max_length=200, blank=True, null=True)  # e.g., Website, Referral
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### **LeadNote**

```python
class LeadNote(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="notes")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

### **ActivityLog**

```python
class ActivityLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=200)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
```

---

## 3. User Roles & Permissions

- **Admin**

  - Full access (manage users, leads, reports, etc.)

- **Sales Manager**

  - Create, view, edit, delete leads
  - Assign leads to executives
  - View team reports

- **Sales Executive**

  - View & update only assigned leads
  - Add notes
  - Change lead status

We can handle permissions via:

- Django’s built-in **Groups & Permissions**
- Custom decorators/mixins for view restrictions

---

## 4. Views & Templates

**Pages to create:**

1. **Authentication**

   - Login (`templates/auth/login.html`)
   - Logout

2. **Dashboard**

   - Stats + recent leads (`templates/dashboard.html`)

3. **Leads**

   - List view with filters (`templates/leads/list.html`)
   - Create/edit form (`templates/leads/form.html`)
   - Detail view with notes (`templates/leads/detail.html`)

4. **Notes**

   - Add note form (AJAX for quick add)

5. **Reports**

   - Simple charts (conversion rate, source stats)

6. **User Management** (for Admin)

   - List users
   - Assign roles

---

## 5. Project Structure

```bash
lead_management/
│
├── manage.py
├── requirements.txt
├── lead_management/        # Project config
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/               # User authentication & profiles
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/accounts/
│       ├── login.html
│       ├── register.html
│       └── profile.html
│
├── leads/                  # Core lead management app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── filters.py          # django-filter for lead search
│   ├── templates/leads/
│       ├── list.html
│       ├── form.html
│       ├── detail.html
│       └── dashboard.html
│
├── static/                 # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
│
└── templates/              # Base templates
    ├── base.html
    ├── dashboard.html
    └── 404.html
```

---

## 6. Step-by-step Development Plan

**Phase 1 — Setup**

- Create Django project & apps (`accounts`, `leads`)
- Configure PostgreSQL or SQLite for dev
- Create custom `User` model (if needed)
- Setup authentication (login/logout)

**Phase 2 — Lead CRUD**

- Create `Lead` model & admin
- Implement `ListView`, `CreateView`, `UpdateView`, `DetailView`
- Create templates with Bootstrap/Tailwind

**Phase 3 — Permissions**

- Create groups (`admin`, `manager`, `executive`)
- Add view-level restrictions
- Show/hide UI elements based on role

**Phase 4 — Notes & Activity Logs**

- Implement `LeadNote` model
- Create AJAX note form on lead detail page
- Log all actions in `ActivityLog`

**Phase 5 — Dashboard & Filters**

- Use Django ORM aggregations for stats
- Implement `django-filter` for lead search
- Add date range filtering

**Phase 6 — Reports**

- Integrate charts (Chart.js)
- Show conversion rate & source breakdown

**Phase 7 — Testing & Deployment**

- Write unit tests for models & views
- Configure production settings
- Deploy to server (Gunicorn + Nginx)

---

## 7. Extra Considerations

- **Security**

  - CSRF protection
  - Login required on all lead pages
  - Strict role-based data access

- **Performance**

  - Use `select_related` & `prefetch_related` for related queries

- **Scalability**

  - Modular app design for future features

- **UI**

  - Responsive design with Bootstrap/Tailwind

- **Future Enhancements**

  - Email follow-up automation
  - Third-party CRM integration
  - Kanban drag-and-drop UI

---
