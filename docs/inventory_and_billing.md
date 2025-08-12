# Retail POS System — Rough Plan

---

## 1. Simple System Flow (Step-by-Step)

1. **User Registration & Login**

   - Admin and cashier (staff) accounts created.

2. **Inventory Setup**

   - Admin adds products with details including barcode, price, stock quantity, category.

3. **Product Scanning & Lookup**

   - Cashier searches product by name/SKU (later scans barcode).
   - System auto-fills product details and adds to current sale cart.

4. **Billing & Checkout**

   - Cashier adds multiple products with quantity to the cart.
   - System calculates subtotal, taxes, discounts, and total price dynamically.
   - Select payment method (cash, card, digital wallets).
   - Complete the sale, update stock automatically.

5. **Receipt Generation**

   - Generate and print or email receipt instantly after checkout.

6. **Returns & Refunds**

   - Handle product returns with stock adjustments and refund processing.

7. **Reports & Analytics**

   - Sales reports by day, product, cashier.
   - Inventory stock alerts for low stock.

---

## 2. Roles & Users

| Role    | Responsibilities                             |
| ------- | -------------------------------------------- |
| Admin   | Manage products, users, categories, reports  |
| Cashier | Process sales, returns, view limited reports |

---

## 3. Core Models

```python
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)

class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Cashier
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('wallet', 'Digital Wallet'),
    ])
    payment_status = models.CharField(max_length=20, choices=[
        ('paid', 'Paid'),
        ('pending', 'Pending'),
    ], default='paid')

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # price at sale time
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
```

---

## 4. Key Features

### Product Scanning & Cart Management

- Use barcode scanner input or manual search for products.
- Add scanned products to a sale cart with quantity adjustments.
- Display live price calculations with tax and discounts.

### Real-time Stock Management

- Decrease product stock on sale completion.
- Warn cashier when stock is low.

### Payment Handling

- Multiple payment methods supported.
- Payment status tracked.

### Receipt Generation

- Printable receipts with sale details, payment info, and totals.
- Optionally email receipt to customer.

### Returns and Refunds

- Allow returns by referencing original sale.
- Adjust stock and update sales records.

### Reporting

- Daily sales, top-selling products, cashier-wise sales.
- Stock level reports with alerts for restocking.

---

## 5. Permissions & Access Control

- Use Django groups:

  - Admin (full access)
  - Cashier (restricted access to sales and limited reports)

- Secure views and templates accordingly.

---

## 6. Suggested Project Structure

```
retail_pos/
├── accounts/          # User auth, roles
├── inventory/         # Products, categories, stock management
├── sales/             # Sales, sale items, payments, returns
├── reports/           # Sales & stock reports
├── templates/
│   ├── accounts/
│   ├── inventory/
│   ├── sales/
│   ├── reports/
│   └── base.html
├── static/
└── manage.py
```

---

## 7. Additional Notes & Next Steps

- **Frontend:** Use AJAX for live cart updates and barcode scanning integration.
- **Stock updates:** Use `transaction.atomic` to avoid race conditions during concurrent sales.
- **UI:** Design a fast, clean interface optimized for touchscreen or keyboard+scanner input.
- **Testing:** Thoroughly test edge cases like partial payments, returns, and stock limits.
- **Extendability:** Add loyalty program, multi-store support, or integration with accounting software later.
