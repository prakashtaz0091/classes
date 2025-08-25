

## **Week 1 → Setup & Foundation**

* **Project setup**

  * Create Django project & app (`shop`, `accounts`, `payments`, `dashboard`).
  * Configure environment (`python-decouple`, PostgreSQL/MySQL).
  * Install dependencies (`django-crispy-forms`, `pillow`, etc.).
* **Models (initial draft)**

  * `Jewellery` (name, category, description, price, image, stock).
  * `User` (extend `AbstractUser`, add fields for citizenship info, profile).
  * `Order` (user, items, total, status, payment info).
* **Templates setup** with base layout & navigation.
* **Public pages**: Home, product listing, product detail.

✅ Deliverable: Visitors can browse jewellery listings with clean Django templates.

---

## **Week 2 → Accounts & Verification**

* **User authentication** (Django auth): register, login, logout.
* **Citizenship verification**:

  * Extend signup form → upload citizenship scan/image + enter details (name, dob, address as per card).
  * Store documents securely (file uploads).
* **Restrict purchase flow**:

  * Only verified users (with documents submitted) can proceed to checkout.
* **Profile page** for updating details/documents.

✅ Deliverable: Verified users can create an account and upload citizenship before buying.

---

## **Week 3 → Order & Checkout Flow**

* **Cart system** (session-based or user-based).
* **Checkout page** with user’s citizenship details auto-filled.
* **Order model finalization** (line items, billing details, payment status).
* **Payment integration (Khalti test mode)**

  * Add Khalti payment button at checkout.
  * Handle callback/verification from Khalti API.
  * Save payment response in DB (transaction id, amount, status).

✅ Deliverable: Users can place orders and pay via Khalti (test mode working).

---

## **Week 4 → Admin Dashboard (Owner View)**

* Restrict with superuser-only login (jewellery shop owner).
* **Dashboard features**:

  * CRUD for jewellery listings (add/update/delete items).
  * View all sales/orders.
  * Filters (by date, status).
* **Graphs & insights** (using Chart.js / Django + JS):

  * Monthly sales chart.
  * Top selling jewellery.
  * Revenue growth line/bar graph.

✅ Deliverable: Owner can manage listings & see sales performance visually.

---

## **Week 5 → Polishing & Deployment Prep**

* **UI/UX improvements** (Bootstrap/Tailwind).
* **Validation & security**:

  * Validate citizenship uploads.
  * Ensure payment security (verify Khalti signature).
* **Email notifications** (order confirmation).
* **Testing**:

  * Test payment flow (sandbox/live).
  * Test edge cases (no stock, invalid document, failed payment).
* **Deployment readiness** (settings, static/media config).

---

## **Week 6 → Deployment & Final Touches**

* Deploy to hosting (PythonAnywhere, VPS, or DigitalOcean).
* Finalize **Khalti Live mode** integration.
* Owner training on using dashboard.
* Documentation (how to add products, view sales, manage orders).

✅ Deliverable: Fully functional jewellery e-commerce site with secure checkout & admin dashboard.

---

⚡ **Extras (if time permits):**

* Order invoice PDF generation (with citizenship details).
* Wishlist/favorites.
* Search & filters for jewellery.

---

Do you want me to also draft a **DB schema (tables + fields)** for this plan so you have a concrete starting point?
