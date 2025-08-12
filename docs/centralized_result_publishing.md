# Centralized Result Publishing System — Rough Instructions

---

## 1. User and Role Setup

### Extend the User Model

- Use **Django’s built-in User model** with a **profile** or **custom user model** to add `role` and `school` fields.

Example using a Profile model:

```python
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('schooladmin', 'School Admin'),
        ('teacher', 'Teacher'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE)
```

- Create `UserProfile` on user creation using signals.

---

### User Groups & Permissions

- Create Django groups manually via admin or migration:

  - `SchoolAdmins`
  - `Teachers`

- Assign Django’s built-in **model-level permissions** accordingly:

  - `SchoolAdmins`: full CRUD on grades, exams, subjects, students, marks within their school.
  - `Teachers`: limited permission — can only **add/update** marks for assigned subjects & students.

- Filter views & querysets by logged-in user’s group and their school.

---

## 2. School Registration & Approval

### School Model

```python
class School(models.Model):
    name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=100, unique=True)
    address = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

### Workflow

- School registers via a form (with basic info).
- Admin views pending schools in admin or custom view.
- Admin approves school → sets `is_approved=True`.
- Only approved schools can be used for teacher, student, or academic setup.

---

## 3. Academic Setup (By SchoolAdmin)

### Models to create:

- **AcademicYear**
  Fields: school, year (char field like `"2024-2025"`)

- **Grade**
  Fields: school, name (e.g., "Class 5")

- **Subject**
  Fields: school, name, assigned_teacher (FK to UserProfile filtered by role=teacher)

- **Exam**
  Fields: school, name, academic_year (FK)

### Implementation tips:

- Auto-generate AcademicYear string based on current date — e.g., if month >= 7 then `"{year}-{year+1}"`, else previous year range.
- SchoolAdmin creates grades, subjects, exams — assign subjects to teachers by selecting from teachers linked to their school.

---

## 4. Student & Marks Management

### Student Model

```python
class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    roll_number = models.CharField(max_length=20)
```

### Marks Model

```python
class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

---

## 5. Permissions & Access Control in Views

### SchoolAdmin Views

- Full access to manage:

  - Teachers (create, edit)
  - Grades
  - Academic years
  - Subjects (assign teachers)
  - Exams
  - Students
  - Generate and print report cards

### Teacher Views

- Allowed to:

  - View only their assigned subjects and students in those subjects’ grades.
  - Enter/update marks for those students, exams, and subjects.

---

### How to enforce permissions

- **Filter Querysets** by logged-in user and their school:

```python
def get_teacher_subjects(user):
    profile = user.userprofile
    if profile.role != 'teacher':
        return Subject.objects.none()
    return Subject.objects.filter(school=profile.school, assigned_teacher=profile.user)
```

- In mark entry views:

```python
# Get only students in the grades for teacher's subjects
subjects = get_teacher_subjects(request.user)
students = Student.objects.filter(school=request.user.userprofile.school, grade__in=subjects.values_list('grade', flat=True))
```

- Use Django’s `@login_required` and custom decorators/mixins to restrict views by role.

---

## 6. Marks Entry Interface

- Use **Django formsets** or **ModelFormsets** to allow teachers to enter marks for multiple students in a subject/exam at once.
- Example: one page shows list of students for a subject/exam, with fields to enter marks.

---

## 7. Report Card Generation

- When SchoolAdmin clicks **Print Report Card** for a grade & exam:

  - Query all students in that grade.
  - Aggregate their marks for all subjects in that exam.
  - Calculate total, percentage, and grades (based on configured grade boundaries).
  - Render an HTML template styled for printing.

- Optional: later add PDF export using libraries like `WeasyPrint`.

---

## 8. Additional Technical Recommendations

- Use Django’s **transaction.atomic** around mark updates to ensure data integrity.
- Add **signals** to notify SchoolAdmin when all marks for a subject/exam are submitted by teachers.
- Validate marks (e.g., numeric ranges) in forms.
- For future **student login**, filter their access strictly to their own marks only.
- Secure all views with appropriate authentication & role checks.

---

## 9. Suggested Project Structure

```
centralized_results/
├── accounts/          # User, UserProfile, authentication, role assignment
├── schools/           # School registration, approval
├── academics/         # Grades, academic years, exams, subjects
├── students/          # Student profiles, marks entry forms/views
├── reports/           # Report card generation & printing
├── templates/
│   ├── accounts/
│   ├── schools/
│   ├── academics/
│   ├── students/
│   ├── reports/
│   └── base.html
├── static/
└── manage.py
```
