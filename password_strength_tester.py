import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import re

class PasswordStrengthTester:
    def __init__(self, master):
        self.master = master
        self.master.title("🔐 Password Strength Tester")
        self.master.geometry("450x500")
        self.master.resizable(False, False)
        self.master.configure(bg="#ffffff")

        self.passwords = set()
        self.password_visible = False

        self.setup_style()
        self.create_widgets()

    def setup_style(self):
        style = ttk.Style(self.master)
        style.theme_use("clam")
        style.configure("TButton", padding=6, relief="flat", font=("Segoe UI", 10))
        style.configure("TLabel", font=("Segoe UI", 11))
        style.configure("TEntry", padding=6)
        style.configure("Horizontal.TProgressbar", thickness=20)

    def create_widgets(self):
        self.frame = ttk.Frame(self.master, padding=20)
        self.frame.pack(expand=True)

        ttk.Label(self.frame, text="Enter your password:").pack(pady=(10, 5))

        self.password_var = tk.StringVar()
        self.password_var.trace("w", lambda *args: self.update_strength())

        self.password_entry = ttk.Entry(self.frame, textvariable=self.password_var, show='*', width=30)
        self.password_entry.pack()

        self.toggle_btn = ttk.Button(self.frame, text="👁 Show", command=self.toggle_password_view)
        self.toggle_btn.pack(pady=5)

        self.strength_label = ttk.Label(self.frame, text="")
        self.strength_label.pack(pady=5)

        self.progress = ttk.Progressbar(self.frame, orient="horizontal", mode="determinate", length=250)
        self.progress.pack(pady=5)

        ttk.Button(self.frame, text="Check Strength", command=self.check_strength).pack(pady=(10, 5))
        ttk.Button(self.frame, text="Generate Strong Password", command=self.generate_password).pack(pady=(5, 15))

        # Length slider for password generation
        ttk.Label(self.frame, text="Select password length:").pack()
        self.length_slider = ttk.Scale(self.frame, from_=8, to=20, orient="horizontal")
        self.length_slider.set(12)
        self.length_slider.pack()

    def password_strength(self, password):
        score = 0

        if len(password) >= 8:
            score += 1
        if len(password) >= 12:
            score += 1
        if len(password) >= 16:
            score += 1
        if re.search(r"[A-Z]", password):
            score += 1
        if re.search(r"[a-z]", password):
            score += 1
        if re.search(r"[0-9]", password):
            score += 1
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1

        if score < 3:
            return "Weak", 30, "red"
        elif score < 5:
            return "Moderate", 60, "orange"
        else:
            return "Strong", 100, "green"

    def update_strength(self):
        password = self.password_var.get()
        strength, bar_val, color = self.password_strength(password)
        self.strength_label.config(text=f"Strength: {strength}", foreground=color)
        self.progress["value"] = bar_val

    def check_strength(self):
        password = self.password_entry.get()
        if not password:
            messagebox.showwarning("Warning", "Please enter a password.")
            return

        if password in self.passwords:
            messagebox.showinfo("Info", "This password has already been tested.")
            return

        self.passwords.add(password)
        strength, _, _ = self.password_strength(password)
        if strength == "Weak":
            messagebox.showinfo("Suggestions", "Use uppercase, lowercase, numbers, and special characters for better strength.")

    def generate_password(self):
        length = int(self.length_slider.get())
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_var.set(password)

        # Copy to clipboard
        self.master.clipboard_clear()
        self.master.clipboard_append(password)
        self.master.update()
        messagebox.showinfo("Generated", "Password copied to clipboard!")

    def toggle_password_view(self):
        if self.password_visible:
            self.password_entry.config(show='*')
            self.toggle_btn.config(text="👁 Show")
        else:
            self.password_entry.config(show='')
            self.toggle_btn.config(text="🙈 Hide")
        self.password_visible = not self.password_visible


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthTester(root)
    root.mainloop()
