# Django Templates – Study Notes

## 1. Introduction to Django Templates

### What is a template?
A **template** is an HTML file that can also contain special Django syntax. It defines *how* data is displayed to the user (the look of the page).

### How templates fit into Django's MVT architecture
Django follows the **MVT** pattern:

- **Model** – handles data (database)
- **View** – contains logic, fetches data from the model
- **Template** – displays the data to the user

> **Flow:** User requests a page → View gets data from Model → View sends data to Template → Template renders HTML → User sees the page.

---

## 2. Rendering a Template

### `render()` function
The `render()` function combines a template with data (called **context**) and returns an HTTP response.

```python
# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

### Creating a template file
By default, Django looks for templates inside a `templates` folder in your app.

```
myapp/
    templates/
        home.html
```

```html
<!-- templates/home.html -->
<h1>Welcome to my Django site!</h1>
```

---

## 3. Template Variables

### Displaying data using `{{ variable }}`
You can send data from the view to the template using a **context dictionary**.

```python
def home(request):
    context = {'name': 'Alice'}
    return render(request, 'home.html', context)
```

```html
<h1>Hello, {{ name }}!</h1>
```

### Accessing object attributes
Use a dot (`.`) to access attributes of objects.

```python
def profile(request):
    user = {'username': 'alice', 'age': 25}
    return render(request, 'profile.html', {'user': user})
```

```html
<p>Username: {{ user.username }}</p>
<p>Age: {{ user.age }}</p>
```

> **Note:** The dot works for dictionary keys, object attributes, and method calls — Django tries each automatically.

---

## 4. Template Filters

Filters change how a variable is displayed. Syntax: `{{ variable|filter }}`

| Filter    | Description                      | Example                              |
|-----------|-----------------------------------|----------------------------------------|
| `upper`   | Converts text to uppercase       | `{{ name|upper }}` → `ALICE`         |
| `lower`   | Converts text to lowercase       | `{{ name|lower }}` → `alice`         |
| `title`   | Capitalizes each word             | `{{ name|title }}` → `Alice Smith`   |
| `length`  | Returns the length of a value     | `{{ name|length }}` → `5`            |
| `default` | Shows a fallback if value is empty| `{{ name|default:"Guest" }}`         |

```html
<p>{{ name|upper }}</p>
<p>{{ items|length }} items in cart</p>
<p>Hello, {{ username|default:"Guest" }}!</p>
```

---

## 5. Conditional Statements

Use `{% if %}`, `{% elif %}`, and `{% else %}` to show content conditionally.

```html
{% if user.age >= 18 %}
    <p>You are an adult.</p>
{% elif user.age >= 13 %}
    <p>You are a teenager.</p>
{% else %}
    <p>You are a child.</p>
{% endif %}
```

> **Note:** Always close `{% if %}` with `{% endif %}`.

---

## 6. Loops

### `{% for %}`
Loop through a list or queryset.

```html
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```

### `forloop.counter`
Gives the current loop iteration number (starting from 1).

```html
<ul>
{% for item in items %}
    <li>{{ forloop.counter }}. {{ item }}</li>
{% endfor %}
</ul>
```

### `{% empty %}`
Shows content if the list is empty.

```html
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% empty %}
    <li>No items found.</li>
{% endfor %}
</ul>
```

---

## 7. Working with QuerySets in Templates

A **QuerySet** is the result of a database query (a list of model objects). You can loop through it just like a normal list.

```python
# views.py
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
```

```html
<!-- products.html -->
<ul>
{% for product in products %}
    <li>{{ product.name }} - ${{ product.price }}</li>
{% empty %}
    <li>No products available.</li>
{% endfor %}
</ul>
```

---

## 8. Template Inheritance

Inheritance lets you create a common layout (`base.html`) and reuse it across pages.

### `base.html`
```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>My Site</title>
</head>
<body>
    <header><h1>My Website</h1></header>

    {% block content %}
    {% endblock %}

    <footer>© 2024 My Site</footer>
</body>
</html>
```

### `{% extends %}` and `{% block %}`
Child templates extend the base and override specific blocks.

```html
<!-- templates/home.html -->
{% extends 'base.html' %}

{% block content %}
    <p>Welcome to the homepage!</p>
{% endblock %}
```

> **Note:** `{% extends %}` must be the **first line** of the template.

---

## 9. Including Reusable Templates

`{% include %}` inserts another template file — useful for things like navbars or footers used on multiple pages.

```html
<!-- templates/navbar.html -->
<nav>
    <a href="/">Home</a> | <a href="/about/">About</a>
</nav>
```

```html
<!-- templates/home.html -->
{% extends 'base.html' %}

{% block content %}
    {% include 'navbar.html' %}
    <p>Welcome!</p>
{% endblock %}
```

---

## 10. Static Files

Static files include CSS, JavaScript, and images.

### `{% load static %}`
Must be added at the top of the template to use static files.

```
myapp/
    static/
        css/
            style.css
```

### CSS example
```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <h1>Styled Page</h1>
</body>
</html>
```

---

## 11. URL Tag

### `{% url %}`
Generates a URL based on the **name** of a URL pattern (defined in `urls.py`), instead of writing the path manually.

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
]
```

```html
<a href="{% url 'about' %}">About Us</a>
```

### Why it is better than hardcoding URLs
- If the URL path changes, you only update `urls.py` — templates stay correct automatically.
- Reduces the risk of broken links.
- Makes code easier to maintain.

---

## 12. `get_absolute_url()`

### Purpose
A model method that returns the **canonical URL** for a specific object. Useful for linking directly to detail pages and used by Django's admin "View on site" feature.

### Simple example
```python
# models.py
from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.id])
```

```html
<a href="{{ product.get_absolute_url }}">{{ product.name }}</a>
```

---

## 13. Summary / Key Takeaways

- Templates are HTML files that display data — they belong to the **T** in MVT.
- Use `render()` in views to send a template + context data to the browser.
- `{{ variable }}` displays data; `{{ variable|filter }}` formats it.
- `{% if %}`, `{% for %}`, etc. add logic to templates using template tags.
- `{% extends %}` and `{% block %}` avoid repeating layout code.
- `{% include %}` reuses small template snippets.
- `{% load static %}` and `{% static %}` link CSS, JS, and images.
- `{% url %}` and `get_absolute_url()` create flexible, maintainable links.

---

## ✅ Quick Revision Checklist

- [ ] I know what a template is and where it fits in MVT.
- [ ] I can render a template using `render()`.
- [ ] I can display variables using `{{ }}` and access object attributes.
- [ ] I can use filters: `upper`, `lower`, `title`, `length`, `default`.
- [ ] I can write `{% if %}`, `{% elif %}`, `{% else %}` conditions.
- [ ] I can loop with `{% for %}`, use `forloop.counter`, and `{% empty %}`.
- [ ] I can loop through a QuerySet in a template.
- [ ] I understand `{% extends %}` and `{% block %}` for inheritance.
- [ ] I can use `{% include %}` for reusable components.
- [ ] I can load and use static files (`{% load static %}`, `{% static %}`).
- [ ] I can use `{% url %}` instead of hardcoded links.
- [ ] I understand the purpose of `get_absolute_url()`.
