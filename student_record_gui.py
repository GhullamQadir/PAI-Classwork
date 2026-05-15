import os
import tkinter as tk
from tkinter import ttk, messagebox

DATA_FILE = "file.txt"


def ensure_data_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            file.write("")


def read_all_records():
    ensure_data_file()
    records = []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        for recordno, line in enumerate(file, start=1):
            raw = line.strip()
            if not raw:
                continue

            parts = raw.split(",")
            if len(parts) < 4:
                continue

            records.append(
                {
                    "recordno": recordno,
                    "name": parts[0].strip(),
                    "age": parts[1].strip(),
                    "rollno": parts[2].strip(),
                    "gpa": parts[3].strip(),
                }
            )

    return records


def add_record(name, age, rollno, gpa):
    ensure_data_file()

    if not name or not age or not rollno or not gpa:
        return False, "Please fill all fields."

    with open(DATA_FILE, "a", encoding="utf-8") as file:
        file.write(f"{name},{age},{rollno},{gpa}\n")

    return True, "Record added successfully."


def show_all_records():
    return read_all_records()


def showrecord(rollno):
    rollno = rollno.strip()
    if not rollno:
        return []

    matches = []
    for rec in read_all_records():
        if rec["rollno"] == rollno:
            matches.append(rec)

    return matches


# Keep the original function names from the notebook for compatibility.
Addrecord = add_record
showAllrecords = show_all_records


class StudentRecordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Record Manager")
        self.root.geometry("900x560")
        self.root.minsize(780, 500)

        self.build_ui()

    def build_ui(self):
        title = tk.Label(
            self.root,
            text="Student Record Manager",
            font=("Segoe UI", 18, "bold"),
            pady=12,
        )
        title.pack()

        form_frame = ttk.LabelFrame(self.root, text="Record Form", padding=12)
        form_frame.pack(fill="x", padx=12, pady=6)

        ttk.Label(form_frame, text="Name").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        ttk.Label(form_frame, text="Age").grid(row=0, column=2, padx=6, pady=6, sticky="w")
        ttk.Label(form_frame, text="Roll No").grid(row=1, column=0, padx=6, pady=6, sticky="w")
        ttk.Label(form_frame, text="GPA").grid(row=1, column=2, padx=6, pady=6, sticky="w")

        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.roll_var = tk.StringVar()
        self.gpa_var = tk.StringVar()
        self.search_roll_var = tk.StringVar()

        ttk.Entry(form_frame, textvariable=self.name_var, width=30).grid(
            row=0, column=1, padx=6, pady=6, sticky="ew"
        )
        ttk.Entry(form_frame, textvariable=self.age_var, width=20).grid(
            row=0, column=3, padx=6, pady=6, sticky="ew"
        )
        ttk.Entry(form_frame, textvariable=self.roll_var, width=30).grid(
            row=1, column=1, padx=6, pady=6, sticky="ew"
        )
        ttk.Entry(form_frame, textvariable=self.gpa_var, width=20).grid(
            row=1, column=3, padx=6, pady=6, sticky="ew"
        )

        for col in range(4):
            form_frame.columnconfigure(col, weight=1)

        action_frame = ttk.Frame(self.root, padding=(12, 2))
        action_frame.pack(fill="x")

        ttk.Button(action_frame, text="Add Record", command=self.handle_add_record).pack(
            side="left", padx=4, pady=6
        )
        ttk.Button(action_frame, text="Show All Records", command=self.handle_show_all).pack(
            side="left", padx=4, pady=6
        )

        ttk.Label(action_frame, text="Search Roll No:").pack(side="left", padx=(22, 6))
        ttk.Entry(action_frame, textvariable=self.search_roll_var, width=16).pack(
            side="left", padx=4
        )
        ttk.Button(action_frame, text="Show Record", command=self.handle_show_one).pack(
            side="left", padx=4, pady=6
        )
        ttk.Button(action_frame, text="Clear Output", command=self.clear_output).pack(
            side="left", padx=4, pady=6
        )
        ttk.Button(action_frame, text="Exit", command=self.root.quit).pack(side="right", padx=4, pady=6)

        table_frame = ttk.LabelFrame(self.root, text="Output", padding=10)
        table_frame.pack(fill="both", expand=True, padx=12, pady=(4, 10))

        columns = ("recordno", "name", "age", "rollno", "gpa")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        self.tree.heading("recordno", text="Record No")
        self.tree.heading("name", text="Name")
        self.tree.heading("age", text="Age")
        self.tree.heading("rollno", text="Roll No")
        self.tree.heading("gpa", text="GPA")

        self.tree.column("recordno", width=90, anchor="center")
        self.tree.column("name", width=250)
        self.tree.column("age", width=90, anchor="center")
        self.tree.column("rollno", width=150, anchor="center")
        self.tree.column("gpa", width=90, anchor="center")

        yscroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=yscroll.set)

        self.tree.pack(side="left", fill="both", expand=True)
        yscroll.pack(side="right", fill="y")

        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, anchor="w", padding=(12, 4))
        status_bar.pack(fill="x", side="bottom")

    def update_table(self, records):
        self.clear_output()
        for rec in records:
            self.tree.insert(
                "",
                "end",
                values=(
                    rec["recordno"],
                    rec["name"],
                    rec["age"],
                    rec["rollno"],
                    rec["gpa"],
                ),
            )

    def clear_output(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.status_var.set("Output cleared.")

    def handle_add_record(self):
        name = self.name_var.get().strip()
        age = self.age_var.get().strip()
        rollno = self.roll_var.get().strip()
        gpa = self.gpa_var.get().strip()

        success, msg = Addrecord(name, age, rollno, gpa)
        if success:
            self.status_var.set(msg)
            self.handle_show_all()
            self.name_var.set("")
            self.age_var.set("")
            self.roll_var.set("")
            self.gpa_var.set("")
        else:
            messagebox.showwarning("Validation Error", msg)
            self.status_var.set(msg)

    def handle_show_all(self):
        records = showAllrecords()
        self.update_table(records)
        self.status_var.set(f"Showing all records. Total found: {len(records)}")

    def handle_show_one(self):
        rollno = self.search_roll_var.get().strip()
        if not rollno:
            messagebox.showinfo("Input Required", "Enter a roll number to search.")
            self.status_var.set("Search failed: roll number is empty.")
            return

        matches = showrecord(rollno)
        self.update_table(matches)

        if matches:
            self.status_var.set(f"Showing record(s) for roll number: {rollno}")
        else:
            self.status_var.set(f"No record found for roll number: {rollno}")
            messagebox.showinfo("No Record", f"No record found for roll number: {rollno}")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentRecordApp(root)
    root.mainloop()
