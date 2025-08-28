# 🚦 Vehicle Registration POC (1 Month Plan, using Django + SQLite + Templates)

## 1. Problem

Currently in Nepal, citizens face **long queues, unclear processes, and dependency on middlemen** to register their vehicles (new or used).
This not only wastes time but also leads to corruption and additional expenses (\~₨1000+).

## 2. Proposed Solution

A **digital workflow platform** for vehicle registration:

* End-users upload documents and apply for registration.
* Staff members verify KYC via call/meeting and approve/reject.
* Vehicle details, insurance, and tax clearance uploaded & approved digitally.
* User only needs to **visit physically once** for the final stamp.

This reduces queues, cuts down corruption, and makes the process transparent.

---

## 3. Detailed 1-Month Development Plan

### 🔹 Week 1 – **Setup & Core Modules**

**Goals:** Django project setup, user authentication, base models.

**Tasks:**

1. **Project Setup**

   * Start Django project (`vehicle_reg_poc`).
   * Create apps:

     * `users` → User, Profile, Documents
     * `vehicles` → Vehicle, VehicleDocs
     * `kyc` → KYC verification workflow
     * `staff` → Staff-specific dashboards
   * Setup static + media storage (for file uploads).

2. **User & Staff Authentication**

   * Extend `AbstractUser` or use `OneToOne` Profile model.
   * Roles:

     * End-user (vehicle owner)
     * Staff (transport office)
   * Implement registration/login/logout templates.

3. **Profile & KYC Base Models**

   ```python
   class Profile(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE)
       phone = models.CharField(max_length=15)
       citizenship_no = models.CharField(max_length=50)
       license_no = models.CharField(max_length=50, blank=True, null=True)
       photo = models.ImageField(upload_to="users/photos/")
       kyc_status = models.CharField(max_length=20, choices=[("pending","Pending"),("approved","Approved"),("rejected","Rejected")], default="pending")
   ```

4. **Templates**

   * Basic Bootstrap/Tailwind layout.
   * User registration form (with document upload).
   * Staff login page.

✅ **End of Week 1 Deliverable:**

* Users can sign up/login.
* Upload basic profile docs.
* Staff can log in (role-based).

---

### 🔹 Week 2 – **KYC Verification Workflow**

**Goals:** Allow staff to verify users via uploaded documents.

**Tasks:**

1. **KYC Document Upload**

   ```python
   class KycDocument(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       doc_type = models.CharField(max_length=50, choices=[("citizenship","Citizenship"),("license","Driving License")])
       file = models.FileField(upload_to="kyc/")
       uploaded_at = models.DateTimeField(auto_now_add=True)
   ```

2. **Staff Verification Dashboard**

   * List of pending KYCs.
   * Detail view with uploaded docs.
   * Staff sets status = Approved / Rejected.
   * Staff can leave remarks (e.g. "Mismatch in photo").

3. **KYC Call/Meeting Notes**

   * Simple text field `verification_notes`.
   * (Future: can integrate Zoom/Meet APIs).

4. **Templates**

   * User dashboard: Track KYC status.
   * Staff dashboard: Approve/reject users.

✅ **End of Week 2 Deliverable:**

* End-user uploads KYC docs.
* Staff verifies and approves/rejects.
* Status visible to user.

---

### 🔹 Week 3 – **Vehicle Registration Workflow**

**Goals:** End-users upload vehicle details & docs, staff approves.

**Tasks:**

1. **Vehicle Model**

   ```python
   class Vehicle(models.Model):
       owner = models.ForeignKey(User, on_delete=models.CASCADE)
       engine_no = models.CharField(max_length=100)
       chassis_no = models.CharField(max_length=100)
       plate_no = models.CharField(max_length=50)
       brand = models.CharField(max_length=100)
       model = models.CharField(max_length=100)
       status = models.CharField(max_length=20, choices=[("pending","Pending"),("registered","Registered"),("rejected","Rejected")], default="pending")
   ```

2. **Vehicle Documents**

   ```python
   class VehicleDocument(models.Model):
       vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
       doc_type = models.CharField(max_length=50, choices=[("insurance","Insurance"),("tax_clearance","Tax Clearance"),("photo","Vehicle Photo")])
       file = models.FileField(upload_to="vehicles/docs/")
   ```

3. **Staff Review**

   * Staff sees pending vehicles.
   * Can approve/reject.
   * Status updates to "Registered".

4. **Templates**

   * End-user: Form to submit vehicle details + upload docs.
   * Staff: Vehicle approval list.

✅ **End of Week 3 Deliverable:**

* Users upload vehicle info & documents.
* Staff approves vehicle registration.
* Vehicle marked as registered.

---

### 🔹 Week 4 – **Polish, Notifications & Demo**

**Goals:** Wrap up with notifications, registration slip, and deployment.

**Tasks:**

1. **Registration Slip**

   * Generate a simple PDF/HTML slip with user info, vehicle info, registration status.
   * (Future: QR code to scan at office).

2. **Notifications**

   * Email user on KYC approval/rejection.
   * Email user on vehicle registration approval.
   * (Use Django’s default email backend with console for POC).

3. **Dashboards**

   * End-user dashboard: My KYC, My Vehicles, Registration Slip download.
   * Staff dashboard: All users, All vehicles.

4. **Deployment**

   * Deploy on server (DigitalOcean / Render / PythonAnywhere).
   * Ensure static/media files working.
   * Document setup & usage for demo.

✅ **End of Week 4 Deliverable:**

* Working POC with full flow: user → KYC → vehicle → staff approval → registration slip.
* Ready for demo to stakeholders.

---

## 4. Final POC Features (1 Month Output)

* 👤 **User system** (sign up, upload docs, track status).
* 🛂 **KYC verification workflow** (staff approves/rejects).
* 🚗 **Vehicle registration workflow** (details + docs, staff approval).
* 📝 **Staff dashboards** (users & vehicles).
* 📄 **Registration slip** (simple downloadable proof).
* 🔔 **Email notifications**.
* ✅ **Deployed demo on SQLite (lightweight but functional).**

---

Would you like me to also prepare a **visual flow diagram (user → staff → approval process)** so you can present this POC plan better to others?
