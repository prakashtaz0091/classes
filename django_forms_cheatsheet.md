# Django Forms

## 1. What is a Django Form?

Django Form is a Python class that:

* Collects user input
* Validates input
* Converts cleaned data to Python types
* Can re-render with errors

---

# 2. Creating a Simple Form

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

---

# 3. Common Form Fields (with examples)

### 3.1 Text Fields

```python
forms.CharField(max_length=100)
forms.EmailField()
forms.RegexField(regex=r'^[0-9]+$')
forms.SlugField()
forms.URLField()
```

### 3.2 Number Fields

```python
forms.IntegerField()
forms.FloatField()
forms.DecimalField(max_digits=10, decimal_places=2)
```

### 3.3 Date and Time Fields

```python
forms.DateField(widget=forms.DateInput)
forms.DateTimeField(widget=forms.DateTimeInput)
forms.TimeField(widget=forms.TimeInput)
```

### 3.4 Choice Fields

```python
GENDER = [
    ('M', 'Male'),
    ('F', 'Female'),
]

forms.ChoiceField(choices=GENDER)
forms.TypedChoiceField(coerce=int, choices=[('1','One'),('2','Two')])
forms.MultipleChoiceField(choices=GENDER)
forms.TypedMultipleChoiceField(coerce=int, choices=[('1','One'),('2','Two')])
```

### 3.5 Boolean Fields

```python
forms.BooleanField(required=False)
forms.NullBooleanField()
```

### 3.6 File Fields

```python
forms.FileField()
forms.ImageField()
```

### 3.7 Other Useful Fields

```python
forms.UUIDField()
forms.JSONField()
forms.GenericIPAddressField()
```

---

# 4. Form Widgets (with examples)

Widgets control how the field renders in HTML.

### Common Widgets:

```python
forms.TextInput(attrs={'class': 'form-control'})
forms.Textarea(attrs={'rows': 4})
forms.NumberInput()
forms.EmailInput()
forms.PasswordInput()
forms.URLInput()
forms.DateInput(attrs={'type':'date'})
forms.TimeInput(attrs={'type':'time'})
forms.DateTimeInput(attrs={'type':'datetime-local'})
forms.CheckboxInput()
forms.Select()
forms.SelectMultiple()
forms.RadioSelect()
forms.FileInput()
forms.ClearableFileInput()
```

### Example:

```python
class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
```

---

# 5. Adding Custom Classes to Form Fields

### 5.1 Directly inside the field (recommended)

```python
username = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control'})
)
```

### 5.2 Dynamically in `__init__`

```python
class MyForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
```

### 5.3 Add different classes for different fields

```python
self.fields['email'].widget.attrs.update({
    'class': 'email-input'
})
```

---

# 6. Rendering Forms in Templates

You can render forms in **3 ways**:

### 6.1 Render Manually (most control)

```html
<form method="post">
    {% csrf_token %}
    {{ form.non_field_errors }}

    <div>
        {{ form.name.label_tag }}
        {{ form.name }}
        {{ form.name.errors }}
    </div>

    <div>
        {{ form.email.label_tag }}
        {{ form.email }}
        {{ form.email.errors }}
    </div>

    <button type="submit">Submit</button>
</form>
```

### 6.2 Render As Table

```html
<form method="post">
    {% csrf_token %}
    {{ form.as_table }}
    <button type="submit">Submit</button>
</form>
```

### 6.3 Render As Paragraphs

```html
{{ form.as_p }}
```

### 6.4 Render As Unordered List

```html
{{ form.as_ul }}
```

---

# 7. Validating Forms

## 7.1 Basic Validation

```python
if form.is_valid():
    # cleaned_data is available
    print(form.cleaned_data)
```

---

# 8. Cleaning and Validating Data

## 8.1 Clean a specific field

```python
class ContactForm(forms.Form):
    email = forms.EmailField()
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Only Gmail addresses allowed.")
        return email
```

## 8.2 Clean multiple fields (cross-field validation)

```python
def clean(self):
    cleaned = super().clean()
    start = cleaned.get('start_date')
    end = cleaned.get('end_date')

    if start and end and start > end:
        raise forms.ValidationError("Start date cannot be after end date.")
    return cleaned
```

---

# 9. Custom Error Messages

```python
name = forms.CharField(
    error_messages={
        'required': 'Name cannot be empty.',
        'max_length': 'Too long.',
    }
)
```

---

# 10. Initial Values

```python
class ProfileForm(forms.Form):
    country = forms.CharField(initial="Nepal")
```

Set dynamically:

```python
form = ProfileForm(initial={'country': 'India'})
```

---

# 11. Disable a Field

```python
forms.CharField(disabled=True)
```

---

# 12. Hidden Fields

```python
forms.CharField(widget=forms.HiddenInput())
```

---

# 13. Form with File Upload

### form.py

```python
class UploadForm(forms.Form):
    title = forms.CharField()
    file = forms.FileField()
```

### template

```html
<form method="post" enctype="multipart/form-data">
```

---

# 14. ModelForm (Quick Overview)

```python
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }
```

---

# 15. How to Show Errors

## Field error:

```html
{{ form.name.errors }}
```

## Form-wide errors:

```html
{{ form.non_field_errors }}
```

---

# 16. Full Example: Complete Form With Validation + Widgets + Classes

### forms.py

```python
class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control'
        })
    )
    age = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class':'form-control'})
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if ' ' in username:
            raise forms.ValidationError("Username cannot contain spaces.")
        return username

    def clean(self):
        cleaned = super().clean()
        age = cleaned.get('age')
        if age and age < 18:
            raise forms.ValidationError("Age must be at least 18.")
        return cleaned
```

### views.py

```python
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})
```

### template.html

```html
<form method="post">
    {% csrf_token %}
    {{ form.non_field_errors }}
    <div>
        {{ form.username.label_tag }}
        {{ form.username }}
        {{ form.username.errors }}
    </div>
    <div>
        {{ form.email.label_tag }}
        {{ form.email }}
        {{ form.email.errors }}
    </div>
    <div>
        {{ form.age.label_tag }}
        {{ form.age }}
        {{ form.age.errors }}
    </div>
    <button type="submit">Register</button>
</form>
```

---
# Django ModelForm

## 1. What is a ModelForm?

ModelForm is a Django form that:

* Automatically generates form fields from a model
* Handles validation based on model field types
* Saves data directly to the database
* Lets you override widgets, labels, help texts, and errors

---

# 2. Basic ModelForm Example

### models.py

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
```

### forms.py

```python
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email']
```

---

# 3. `fields` vs `exclude`

### Use `fields` to include specific fields

```python
fields = ['name', 'email']
```

### Use `exclude` to exclude specific fields

```python
exclude = ['created_at', 'updated_at']
```

Only use one of them, never both.

---

# 4. Adding Custom Widgets in ModelForm

```python
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
```

---

# 5. Adding Custom Labels and Help Text

```python
class Meta:
    labels = {
        'name': 'Full Name',
    }
    help_texts = {
        'email': 'Enter a valid email.',
    }
```

---

# 6. Custom Error Messages

```python
class Meta:
    error_messages = {
        'name': {
            'required': 'Name must not be empty.',
            'max_length': 'Name too long.',
        }
    }
```

---

# 7. Setting Initial Values

### Option A: In Meta

```python
class StudentForm(forms.ModelForm):
    name = forms.CharField(initial='Default Name')
```

### Option B: In view function

```python
form = StudentForm(initial={'age': 20})
```

---

# 8. Readonly / Disabled Fields

```python
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].disabled = True
```

---

# 9. Cleaning and Validating ModelForm

ModelForms support:

## 9.1 Clean a specific field (`clean_<fieldname>` method)

```python
def clean_name(self):
    name = self.cleaned_data.get('name')
    if len(name.split()) < 2:
        raise forms.ValidationError("Enter at least first and last name.")
    return name
```

## 9.2 Cross-field validation (`clean()` method)

```python
def clean(self):
    cleaned = super().clean()
    age = cleaned.get('age')
    email = cleaned.get('email')

    if age and age < 18 and email.endswith('@college.com'):
        raise forms.ValidationError("Underage students cannot use college email.")
    return cleaned
```

---

# 10. Saving ModelForm Data

## 10.1 Basic save

```python
if form.is_valid():
    form.save()
```

## 10.2 Save without committing (modify before save)

```python
obj = form.save(commit=False)
obj.created_by = request.user
obj.save()
```

## 10.3 Save Many-to-Many fields manually

```python
obj = form.save(commit=False)
obj.save()
form.save_m2m()
```

---

# 11. Overriding Fields in ModelForm

You can override a model field with a custom form field.

```python
class StudentForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'example@gmail.com'}))

    class Meta:
        model = Student
        fields = '__all__'
```

This does not change the model; only the form.

---

# 12. Add Custom CSS Classes to All Fields Dynamically

```python
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
```

---

# 13. ModelForm With File Upload

### models.py

```python
class Document(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='docs/')
```

### forms.py

```python
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']
```

### template

```html
<form method="post" enctype="multipart/form-data">
```

---

# 14. Full Complete Example (ModelForm with cleaning, widgets, save, errors)

### models.py

```python
class Employee(models.Model):
    full_name = models.CharField(max_length=120)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    joined_on = models.DateField()
```

### forms.py

```python
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['full_name', 'age', 'email', 'salary', 'joined_on']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'joined_on': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        labels = {
            'full_name': 'Employee Name',
        }
        help_texts = {
            'salary': 'Enter salary in NPR.',
        }
        error_messages = {
            'email': {
                'unique': 'This email already exists.',
            }
        }

    def clean_full_name(self):
        name = self.cleaned_data['full_name']
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Name cannot contain numbers.")
        return name

    def clean(self):
        cleaned = super().clean()
        age = cleaned.get('age')
        salary = cleaned.get('salary')

        if age and salary and age < 18 and salary > 0:
            raise forms.ValidationError("Underage employees cannot have a salary.")
        return cleaned
```

### views.py

```python
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = EmployeeForm()

    return render(request, 'employee_form.html', {'form': form})
```

### template.html

```html
<form method="post">
    {% csrf_token %}
    {{ form.non_field_errors }}

    {% for field in form %}
        <div>
            {{ field.label_tag }}
            {{ field }}
            {{ field.errors }}
        </div>
    {% endfor %}

    <button type="submit">Save</button>
</form>
```

---
