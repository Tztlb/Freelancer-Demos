import tkinter as tk
from tkinter import filedialog, messagebox
import csv

# کلاس مدیریت کارکنان
class EmployeeManager:
    def __init__(self, file_path):
        self.file_path = file_path
    
    # متد برای ذخیره‌سازی اطلاعات کارکنان در فایل
    def update_file(self, emp_code, last_name, salary):
        with open(self.file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([emp_code, last_name, salary])
    
    # متد برای نمایش محتویات فایل
    def display_file(self):
        employees = []
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                employees = list(reader)
        except FileNotFoundError:
            return "File not found."
        return employees
    
    # متد برای جستجو بر اساس کد کارمندی یا نام خانوادگی
    def search(self, search_term):
        employees = self.display_file()
        results = [emp for emp in employees if search_term in emp]
        return results if results else "No matches found."

# ساخت رابط کاربری گرافیکی
class EmployeeApp:
    def __init__(self, root):
        self.manager = None
        self.root = root
        self.root.title("Employee Manager")
        
        # قسمت انتخاب فایل
        self.file_label = tk.Label(root, text="No file selected")
        self.file_label.pack()
        self.select_file_button = tk.Button(root, text="Select File", command=self.select_file)
        self.select_file_button.pack()

        # قسمت ورودی اطلاعات کارکنان
        self.emp_code_label = tk.Label(root, text="Employee Code:")
        self.emp_code_label.pack()
        self.emp_code_entry = tk.Entry(root)
        self.emp_code_entry.pack()

        self.last_name_label = tk.Label(root, text="Last Name:")
        self.last_name_label.pack()
        self.last_name_entry = tk.Entry(root)
        self.last_name_entry.pack()

        self.salary_label = tk.Label(root, text="Salary:")
        self.salary_label.pack()
        self.salary_entry = tk.Entry(root)
        self.salary_entry.pack()

        self.add_button = tk.Button(root, text="Add Employee", command=self.add_employee)
        self.add_button.pack()

        # قسمت جستجو
        self.search_label = tk.Label(root, text="Search by Code or Last Name:")
        self.search_label.pack()
        self.search_entry = tk.Entry(root)
        self.search_entry.pack()
        self.search_button = tk.Button(root, text="Search", command=self.search_employee)
        self.search_button.pack()

        # دکمه برای نمایش محتویات فایل
        self.show_button = tk.Button(root, text="Show All Employees", command=self.show_employees)
        self.show_button.pack()

    # متد برای انتخاب فایل
    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.file_label.config(text=f"File: {file_path}")
            self.manager = EmployeeManager(file_path)
        else:
            messagebox.showwarning("Warning", "No file selected!")

    # متد برای افزودن کارمند به فایل
    def add_employee(self):
        if self.manager:
            emp_code = self.emp_code_entry.get()
            last_name = self.last_name_entry.get()
            salary = self.salary_entry.get()
            if emp_code and last_name and salary:
                self.manager.update_file(emp_code, last_name, salary)
                messagebox.showinfo("Success", "Employee added successfully!")
            else:
                messagebox.showwarning("Warning", "All fields are required!")
        else:
            messagebox.showwarning("Warning", "No file selected!")

    # متد برای جستجو
    def search_employee(self):
        if self.manager:
            search_term = self.search_entry.get()
            if search_term:
                results = self.manager.search(search_term)
                messagebox.showinfo("Search Results", str(results))
            else:
                messagebox.showwarning("Warning", "Enter a search term!")
        else:
            messagebox.showwarning("Warning", "No file selected!")

    # متد برای نمایش محتویات فایل
    def show_employees(self):
        if self.manager:
            employees = self.manager.display_file()
            messagebox.showinfo("All Employees", str(employees))
        else:
            messagebox.showwarning("Warning", "No file selected!")

# اجرای برنامه
if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeApp(root)
    root.mainloop()
