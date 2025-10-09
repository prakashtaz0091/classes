"""
Expense Tracker Application
Main entry point for the application
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
from PIL import Image, ImageTk
import json
import os
import shutil
from tkcalendar import DateEntry


class ExpenseManager:
    """Handles expense data storage and retrieval"""

    def __init__(self, data_file="expenses.json", images_dir="receipts"):
        self.data_file = data_file
        self.images_dir = images_dir
        self.expenses = []

        # Create directories if they don't exist
        if not os.path.exists(self.images_dir):
            os.makedirs(self.images_dir)

        self.load_expenses()

    def load_expenses(self):
        """Load expenses from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    self.expenses = json.load(f)
            except:
                self.expenses = []

    def save_expenses(self):
        """Save expenses to JSON file"""
        with open(self.data_file, "w") as f:
            json.dump(self.expenses, f, indent=2)

    def add_expense(self, date, name, amount, receipt_path=None):
        """Add a new expense"""
        expense_id = len(self.expenses) + 1
        saved_receipt = None
        if receipt_path:
            # Copy receipt to receipts directory
            ext = os.path.splitext(receipt_path)[1]
            saved_receipt = f"receipt_{expense_id}{ext}"
            shutil.copy2(receipt_path, os.path.join(self.images_dir, saved_receipt))

        expense = {
            "id": expense_id,
            "date": date,
            "name": name,
            "amount": amount,
            "receipt": saved_receipt,
        }

        self.expenses.append(expense)
        self.save_expenses()
        return expense

    def get_all_expenses(self):
        """Get all expenses"""
        return self.expenses

    def search_expenses(self, query):
        """Search expenses by name"""
        query = query.lower()
        return [e for e in self.expenses if query in e["name"].lower()]

    def filter_expenses(self, date):
        """Filter expenses by date"""
        return [e for e in self.expenses if e["date"] == date]

    def get_expense_by_id(self, expense_id):
        """Get a specific expense by ID"""
        for expense in self.expenses:
            if expense["id"] == expense_id:
                return expense
        return None


class ExpenseDetailWindow:
    """Window to display expense details"""

    def __init__(self, parent, expense, images_dir):
        self.window = tk.Toplevel(parent)
        self.window.title(f"Expense Details - {expense['name']}")
        self.window.geometry("500x600")
        self.window.resizable(False, False)

        # Details Frame
        details_frame = ttk.LabelFrame(
            self.window, text="Expense Information", padding=20
        )
        details_frame.pack(fill=tk.BOTH, padx=20, pady=20)

        # Display details
        ttk.Label(details_frame, text="Date:", font=("Arial", 10, "bold")).grid(
            row=0, column=0, sticky=tk.W, pady=5
        )
        ttk.Label(details_frame, text=expense["date"]).grid(
            row=0, column=1, sticky=tk.W, pady=5, padx=10
        )

        ttk.Label(details_frame, text="Name:", font=("Arial", 10, "bold")).grid(
            row=1, column=0, sticky=tk.W, pady=5
        )
        ttk.Label(details_frame, text=expense["name"]).grid(
            row=1, column=1, sticky=tk.W, pady=5, padx=10
        )

        ttk.Label(details_frame, text="Amount:", font=("Arial", 10, "bold")).grid(
            row=2, column=0, sticky=tk.W, pady=5
        )
        ttk.Label(
            details_frame, text=f"${expense['amount']:.2f}", font=("Arial", 10)
        ).grid(row=2, column=1, sticky=tk.W, pady=5, padx=10)

        # Receipt Frame
        receipt_frame = ttk.LabelFrame(self.window, text="Receipt", padding=20)
        receipt_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        if expense["receipt"]:
            receipt_path = os.path.join(images_dir, expense["receipt"])
            if os.path.exists(receipt_path):
                try:
                    # Load and display image
                    img = Image.open(receipt_path)
                    # Resize to fit
                    img.thumbnail((400, 400), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(img)

                    label = ttk.Label(receipt_frame, image=photo)
                    label.image = photo  # Keep a reference
                    label.pack()
                except Exception as e:
                    ttk.Label(
                        receipt_frame, text=f"Error loading image: {str(e)}"
                    ).pack()
            else:
                ttk.Label(receipt_frame, text="Receipt file not found").pack()
        else:
            ttk.Label(receipt_frame, text="No receipt attached").pack()

        # Close button
        ttk.Button(self.window, text="Close", command=self.window.destroy).pack(pady=10)


class ExpenseTrackerApp:
    """Main application window"""

    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("900x700")
        self.root.resizable(False, False)

        self.manager = ExpenseManager()
        self.receipt_path = None

        self.setup_ui()
        self.load_expenses()

    def setup_ui(self):
        """Setup the user interface"""

        # Add Expense Frame
        add_frame = ttk.LabelFrame(self.root, text="Add New Expense", padding=20)
        add_frame.pack(fill=tk.X, padx=20, pady=20)

        # Date
        ttk.Label(add_frame, text="Date:").grid(row=0, column=0, sticky=tk.W, pady=5)
        # self.date_entry = ttk.Entry(add_frame, width=30)
        self.date_entry = DateEntry(
            add_frame,
            width=27,
            background="darkblue",
            foreground="white",
            date_pattern="yyyy-mm-dd",  # or "dd/mm/yyyy"
        )
        self.date_entry.set_date(datetime.now())

        # self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.date_entry.grid(row=0, column=1, sticky=tk.W, pady=5, padx=10)

        # Name
        ttk.Label(add_frame, text="Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.name_entry = ttk.Entry(add_frame, width=30)
        self.name_entry.grid(row=1, column=1, sticky=tk.W, pady=5, padx=10)

        # Amount
        ttk.Label(add_frame, text="Amount ($):").grid(
            row=2, column=0, sticky=tk.W, pady=5
        )
        self.amount_entry = ttk.Entry(add_frame, width=30)
        self.amount_entry.grid(row=2, column=1, sticky=tk.W, pady=5, padx=10)

        # Receipt
        ttk.Label(add_frame, text="Receipt:").grid(row=3, column=0, sticky=tk.W, pady=5)
        receipt_btn_frame = ttk.Frame(add_frame)
        receipt_btn_frame.grid(row=3, column=1, sticky=tk.W, pady=5, padx=10)

        self.receipt_label = ttk.Label(receipt_btn_frame, text="No file selected")
        self.receipt_label.pack(side=tk.LEFT)

        ttk.Button(receipt_btn_frame, text="Browse", command=self.browse_receipt).pack(
            side=tk.LEFT, padx=10
        )

        # Add Button
        ttk.Button(add_frame, text="Add Expense", command=self.add_expense).grid(
            row=4, column=0, columnspan=2, pady=15
        )

        # Expenses List Frame
        list_frame = ttk.LabelFrame(self.root, text="Expenses", padding=20)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        # Search
        search_frame = ttk.Frame(list_frame)
        search_frame.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(search_frame, text="Search:").pack(side=tk.LEFT, padx=(0, 10))
        self.search_entry = ttk.Entry(search_frame, width=40)
        self.search_entry.pack(side=tk.LEFT)
        self.search_entry.bind("<KeyRelease>", lambda e: self.search_expenses())

        # date filter frame
        date_filter_frame = ttk.Frame(list_frame)
        date_filter_frame.pack(fill=tk.X, pady=(0, 10))
        ttk.Label(date_filter_frame, text="Date Filter:").pack(
            side=tk.LEFT, padx=(0, 10)
        )
        self.date_filter_entry = DateEntry(
            date_filter_frame,
            width=27,
            background="darkblue",
            foreground="white",
            date_pattern="yyyy-mm-dd",  # or "dd/mm/yyyy"
        )
        self.date_filter_entry.pack(side=tk.LEFT)
        self.date_filter_entry.bind(
            "<<DateEntrySelected>>", lambda e: self.filter_by_date()
        )
        self.reset_button = ttk.Button(
            date_filter_frame, text="Reset Filter", command=self.reset_filter
        )
        self.reset_button.pack(side=tk.LEFT, padx=(0, 10))

        # Table
        table_frame = ttk.Frame(list_frame)
        table_frame.pack(fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Treeview
        columns = ("ID", "Date", "Name", "Amount", "Receipt")
        self.tree = ttk.Treeview(
            table_frame, columns=columns, show="headings", yscrollcommand=scrollbar.set
        )
        scrollbar.config(command=self.tree.yview)

        # Define headings
        self.tree.heading("ID", text="ID")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Receipt", text="Receipt")

        # Define column widths
        self.tree.column("ID", width=50)
        self.tree.column("Date", width=100)
        self.tree.column("Name", width=300)
        self.tree.column("Amount", width=100)
        self.tree.column("Receipt", width=100)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Bind double-click event
        self.tree.bind("<Double-Button-1>", self.show_expense_details)

    def browse_receipt(self):
        """Browse for receipt image"""
        filename = filedialog.askopenfilename(
            title="Select Receipt Image",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"),
                ("All files", "*.*"),
            ],
        )

        if filename:
            self.receipt_path = filename
            self.receipt_label.config(text=os.path.basename(filename))

    def add_expense(self):
        """Add a new expense"""
        date = self.date_entry.get().strip()
        name = self.name_entry.get().strip()
        amount_str = self.amount_entry.get().strip()

        if not date or not name or not amount_str:
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        try:
            amount = float(amount_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
            return

        # Add expense
        self.manager.add_expense(date, name, amount, self.receipt_path)

        # Clear form
        self.name_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.receipt_path = None
        self.receipt_label.config(text="No file selected")

        # Reload expenses
        self.load_expenses()

        messagebox.showinfo("Success", "Expense added successfully!")

    def load_expenses(self):
        """Load expenses into the table"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        expenses = self.manager.get_all_expenses()
        total = 0

        for expense in expenses:
            receipt_status = "Yes" if expense["receipt"] else "No"
            self.tree.insert(
                "",
                tk.END,
                values=(
                    expense["id"],
                    expense["date"],
                    expense["name"],
                    f"${expense['amount']:.2f}",
                    receipt_status,
                ),
            )
            total += expense["amount"]

    def search_expenses(self):
        """Search expenses"""
        query = self.search_entry.get().strip()

        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        if query:
            expenses = self.manager.search_expenses(query)
        else:
            expenses = self.manager.get_all_expenses()

        total = 0
        for expense in expenses:
            receipt_status = "Yes" if expense["receipt"] else "No"
            self.tree.insert(
                "",
                tk.END,
                values=(
                    expense["id"],
                    expense["date"],
                    expense["name"],
                    f"${expense['amount']:.2f}",
                    receipt_status,
                ),
            )
            total += expense["amount"]

        self.total_label.config(text=f"Total: ${total:.2f}")

    def filter_by_date(self):
        filter_date = self.date_filter_entry.get().strip()

        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        if filter_date:
            expenses = self.manager.filter_expenses(filter_date)
        else:
            expenses = self.manager.get_all_expenses()

        for expense in expenses:
            receipt_status = "Yes" if expense["receipt"] else "No"
            self.tree.insert(
                "",
                tk.END,
                values=(
                    expense["id"],
                    expense["date"],
                    expense["name"],
                    f"${expense['amount']:.2f}",
                    receipt_status,
                ),
            )

    def reset_filter(self):
        self.date_filter_entry.delete(0, tk.END)
        self.filter_by_date()

    def show_expense_details(self, event):
        """Show expense details in a new window"""
        selection = self.tree.selection()
        if not selection:
            return

        item = self.tree.item(selection[0])
        expense_id = item["values"][0]

        expense = self.manager.get_expense_by_id(expense_id)
        if expense:
            ExpenseDetailWindow(self.root, expense, self.manager.images_dir)


def main():
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
