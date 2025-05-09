from tkinter import *
from tkinter import messagebox
from time import strftime

# Biến dùng chung giữa các file
value_from_p1 = None

def new_print(value):
    global value_from_p1
    value_from_p1 = value

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống nhận diện khuôn mặt")
        self.root.geometry("800x500+300+150")

        today = strftime("%d-%m-%Y")

        # Hiển thị thông tin cơ bản
        Label(self.root, text="MÀN HÌNH CHÍNH", font=("Arial", 24, "bold")).pack(pady=20)
        Label(self.root, text=f"Ngày: {today}", font=("Arial", 14)).pack()
        Label(self.root, text=f"Tài khoản: {value_from_p1}", font=("Arial", 14), fg="green").pack(pady=10)

        Button(self.root, text="Đăng xuất", font=("Arial", 12), command=self.root.destroy).pack(pady=20)

if __name__ == "__main__":
    root = Tk()
    Face_Recognition_System(root)
    root.mainloop()
