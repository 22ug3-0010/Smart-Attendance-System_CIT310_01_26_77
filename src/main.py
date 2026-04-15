import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# Professional Theme Colors
BG_COLOR = "#2c3e50"
BTN_COLOR = "#34495e"
TEXT_COLOR = "#ecf0f1"

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CIT310 - Smart Attendance System")
        self.root.geometry("500x600")
        self.root.configure(bg=BG_COLOR)

        # Header Section
        self.header = tk.Label(
            root, text="Smart Attendance System", 
            font=("Helvetica", 18, "bold"), bg=BG_COLOR, fg=TEXT_COLOR, pady=20
        )
        self.header.pack()

        self.sub_header = tk.Label(
            root, text="Project ID: CIT310_01_26_77", 
            font=("Helvetica", 10), bg=BG_COLOR, fg="#bdc3c7"
        )
        self.sub_header.pack()

        # Buttons Frame
        btn_frame = tk.Frame(root, bg=BG_COLOR, pady=30)
        btn_frame.pack()

        # Dashboard Buttons
        self.create_button(btn_frame, "1. Register Student", self.run_register)
        self.create_button(btn_frame, "2. Train Model", self.run_trainer)
        self.create_button(btn_frame, "3. Take Attendance", self.run_attendance)
        self.create_button(btn_frame, "4. Generate Reports", self.run_reports)
        self.create_button(btn_frame, "Exit", root.quit, color="#e74c3c")

        # Footer (Team Credits)
        self.footer = tk.Label(
            root, text="Leader: Mohamed Haizam | Members: Fahad, Ammar, Thanonigsan",
            font=("Helvetica", 8), bg=BG_COLOR, fg="#95a5a6", pady=20
        )
        self.footer.pack(side="bottom")

    def create_button(self, frame, text, command, color=BTN_COLOR):
        btn = tk.Button(
            frame, text=text, command=command, width=25, height=2,
            bg=color, fg=TEXT_COLOR, font=("Helvetica", 11, "bold"),
            relief="flat", activebackground="#1abc9c", cursor="hand2"
        )
        btn.pack(pady=10)

    # Functions to call external scripts
    def run_register(self):
        subprocess.run(["python", "src/register.py"])

    def run_trainer(self):
        subprocess.run(["python", "src/trainer.py"])
        messagebox.showinfo("Success", "Model trained and saved to 'models/'")

    def run_attendance(self):
        subprocess.run(["python", "src/attendance.py"])

    def run_reports(self):
        subprocess.run(["python", "src/reports.py"])
        messagebox.showinfo("Success", "Attendance report generated in 'reports/' folder")

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = AttendanceApp(root)
        root.mainloop()
    except KeyboardInterrupt:
        print("\n[INFO] System closed manually by user.")
    finally:
        # This ensures the program cleans up before closing
        print("[INFO] Cleaning up resources... Goodbye!")