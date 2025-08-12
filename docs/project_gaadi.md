# Vehicle Reservation System Plan

---

## 1. Roles & Users

| Role              | Responsibilities                                                                                          |
| ----------------- | --------------------------------------------------------------------------------------------------------- |
| **User**          | Book vehicles, view & cancel their reservations (before 2 days)                                           |
| **Vehicle Owner** | Register vehicles (submit KYC), approve/reject reservations, cancel approved reservations (before 5 days) |
| **Admin**         | Approve vehicle registrations (after KYC review), manage vehicle owners and system settings               |

---

## 2. Models Updates

### User model

- Use Django’s default User or extend it with a **role** field or groups to distinguish:

  - Regular user
  - Vehicle owner
  - Admin (use Django’s staff/superuser flags)

### Vehicle model

```python
class Vehicle(models.Model):
    VEHICLE_TYPES = [('car', 'Car'), ('van', 'Van'), ('bus', 'Bus'), ('truck', 'Truck')]
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPES)
    capacity = models.PositiveIntegerField()
    registration_number = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)  # Active only after admin approval
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vehicles')

    # KYC fields
    citizenship_number = models.CharField(max_length=50)
    license_number = models.CharField(max_length=50)
    kyc_submitted_at = models.DateTimeField(auto_now_add=True)
    kyc_approved = models.BooleanField(default=False)
    kyc_approved_at = models.DateTimeField(blank=True, null=True)
```

---

### Reservation model with owner cancellation policy

```python
from datetime import timedelta
from django.utils import timezone

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
    ]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='reservations')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservations')
    start_date = models.DateField()
    end_date = models.DateField()
    purpose = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def can_user_cancel(self):
        """User can cancel if more than 2 days remain."""
        return timezone.now().date() <= self.start_date - timedelta(days=2)

    def can_owner_cancel(self):
        """Owner can cancel if more than 5 days remain."""
        return timezone.now().date() <= self.start_date - timedelta(days=5)
```

---

## 3. Business Logic Updates

### Vehicle registration workflow

1. **Vehicle owner registers a vehicle**, submitting KYC details (citizenship number, license number).
2. Vehicle status:

   - `is_active=False`
   - `kyc_approved=False`

3. **Admin reviews KYC documents** (could be via admin panel or a special dashboard).
4. Admin approves/rejects vehicle registration:

   - If approved → `is_active=True`, `kyc_approved=True`, `kyc_approved_at` timestamped
   - If rejected → notify owner for correction

### Reservation approval workflow

- When user books a vehicle, the reservation status is initially `pending`.
- **Vehicle owner reviews pending reservations** for their vehicles and approves/rejects them.
- Only approved reservations are valid bookings.

### Cancellation rules

- **User can cancel** their reservations only if more than 2 days remain before start date.
- **Vehicle owner can cancel** approved reservations only if more than 5 days remain before start date.
- Both cancellation attempts check ownership and status before proceeding.

---

## 4. Security & Access Control

| Action                       | Allowed Role(s)                               | Notes                                 |
| ---------------------------- | --------------------------------------------- | ------------------------------------- |
| Register new vehicle         | Vehicle Owner                                 | Vehicle inactive until admin approval |
| Approve vehicle registration | Admin                                         | After KYC review                      |
| Create reservation           | User                                          | On approved vehicles only             |
| Approve/reject reservations  | Vehicle Owner                                 | Only for their vehicles               |
| Cancel reservation (user)    | User (owner of reservation)                   | Must respect 2-day cancellation rule  |
| Cancel reservation (owner)   | Vehicle Owner (owner vehicle)                 | Must respect 5-day cancellation rule  |
| View reservations            | User (own), Owner (own vehicles), Admin (all) | Permission filtering needed           |

---

## 5. Updated Booking Logic with Locking

```python
from django.db import transaction

@transaction.atomic
def create_reservation(user, vehicle_id, start_date, end_date, purpose):
    vehicle = Vehicle.objects.select_for_update().get(id=vehicle_id, is_active=True, kyc_approved=True)

    overlapping = Reservation.objects.filter(
        vehicle=vehicle,
        status='approved',
        start_date__lt=end_date,
        end_date__gt=start_date
    ).exists()

    if overlapping:
        raise Exception("Vehicle already booked for selected dates.")

    reservation = Reservation.objects.create(
        vehicle=vehicle,
        user=user,
        start_date=start_date,
        end_date=end_date,
        purpose=purpose,
        status='pending',
    )
    return reservation
```

---

## 6. Suggested Views & Workflows

| Feature                     | Role(s)       | Description                                  |
| --------------------------- | ------------- | -------------------------------------------- |
| Vehicle registration form   | Vehicle Owner | Submit vehicle details + KYC info            |
| Vehicle registration review | Admin         | Approve/reject vehicle with KYC verification |
| Vehicle list & details      | All users     | Show only active & approved vehicles         |
| Reservation creation        | User          | Book available vehicles                      |
| Reservation approval        | Vehicle Owner | Approve/reject pending reservations          |
| Cancellation (User)         | User          | Cancel if ≥ 2 days left                      |
| Cancellation (Owner)        | Vehicle Owner | Cancel if ≥ 5 days left                      |
| Dashboards                  | All roles     | Different dashboards showing relevant info   |

---

## 7. Project Structure (Updated)

```
vehicle_reservation/
├── accounts/           # User auth, roles, profiles
├── vehicles/           # Vehicle registration, KYC, admin approval
├── reservations/       # Booking, approvals, cancellations
├── admin_panel/        # Admin views for KYC approvals (can be Django Admin or custom)
├── templates/
│   ├── accounts/
│   ├── vehicles/
│   ├── reservations/
│   └── base.html
├── static/
└── manage.py
```

---

## 8. Additional Recommendations

- Use Django’s **Group & Permission** system or custom user model to manage roles cleanly.
- For KYC docs, you can add file uploads (e.g., scanned copies).
- Send email notifications on:

  - Vehicle registration submission & approval/rejection
  - Reservation approval/rejection
  - Cancellations by user or owner

- Use frontend calendars to show availability visually.
- Add audit logs for KYC approval and reservation actions.
