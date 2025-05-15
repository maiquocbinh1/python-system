
import os
import random
from PIL import Image as PILImage, ImageTk as PILImageTk
from tkinter import *
from tkinter import ttk, messagebox
from time import strftime

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Hệ thống nhận diện khuôn mặt")

        today = strftime("%d-%m-%Y")

        # Background
        img3 = PILImage.open("img/bgbtn.png")
        img3 = img3.resize((1530, 790), PILImage.Resampling.LANCZOS)
        self.photoimg3 = PILImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=790)

        # Time display
        img_time = PILImage.open("img/timsearch50.png")
        img_time = img_time.resize((27, 27), PILImage.Resampling.LANCZOS)
        self.photoimgtime = PILImageTk.PhotoImage(img_time)
        Label(self.root, image=self.photoimgtime, bg="white").place(x=43, y=40, width=27, height=27)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(self.root, font=("yu gothic ui", 13, "bold"), bg="white", fg="black")
        lbl.place(x=80, y=35, width=100, height=20)
        time()

        Label(self.root, text=today, font=("yu gothic ui", 13, "bold"), bg="white", fg="black").place(x=80, y=60, width=100, height=20)

        # Title
        self.txt = "Hệ thống điểm danh sinh viên"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.root, text=self.txt, font=("yu gothic ui", 26, "bold"), bg="white", fg="black", bd=5, relief=FLAT)
        self.heading.place(x=360, y=22, width=500)
        self.slider()
        self.heading_color()

        # Account display
        self.account = "Tài khoản mẫu"
        img_peop = PILImage.open("img/peop.png")
        img_peop = img_peop.resize((27, 27), PILImage.Resampling.LANCZOS)
        self.photoimgpeop = PILImageTk.PhotoImage(img_peop)
        Label(self.root, image=self.photoimgpeop, bg="white").place(x=970, y=45, width=27, height=27)

        Label(self.root, text=self.account, font=("yu gothic ui", 12, "bold"), bg="white", fg="green").place(x=1000, y=48, width=150, height=22)

        # Logout
        img_logout = PILImage.open("img/logout.png")
        img_logout = img_logout.resize((27, 27), PILImage.Resampling.LANCZOS)
        self.photoimglogout = PILImageTk.PhotoImage(img_logout)

        Button(self.root, image=self.photoimglogout, cursor="hand2", command=self.exit, borderwidth=0, bg="white").place(x=1350, y=45, width=27, height=27)
        Button(self.root, text="Đăng xuất", cursor="hand2", command=self.exit, font=("times new roman", 13, "bold"), bg="white", fg="black", borderwidth=0).place(x=1380, y=48, width=100, height=27)

        # Buttons
        self.create_button("Sinh viên", "student.png", 180, 200, self.student_details)
        self.create_button("Điểm danh", "ghichu.png", 520, 200, self.attendance_data)
        self.create_button("Môn học", "book.png", 860, 200, self.subject_data)
        self.create_button("Buổi học", "lesson.png", 1175, 200, self.lesson_data)
        self.create_button("Thống kê", "report.png", 180, 490, self.report_data)
        self.create_button("Giáo viên", "teacher.png", 520, 490, self.teacher_data)

    def create_button(self, text, image_file, x, y, command):
        img = PILImage.open(f"img/{image_file}")
        img = img.resize((80, 113), PILImage.Resampling.LANCZOS)
        photo = PILImageTk.PhotoImage(img)
        button = Button(self.root, text=text, font=("yu gothic ui", 16, "bold"), image=photo, cursor="hand2",
                        activebackground="white", bg="white", borderwidth=0, compound="top", command=command)
        button.image = photo
        button.place(x=x, y=y, width=180, height=180)

    def slider(self):
        if self.count >= len(self.txt):
            self.count = -1
            self.text = ''
            self.heading.config(text=self.text)
        else:
            self.text += self.txt[self.count]
            self.heading.config(text=self.text)
        self.count += 1
        self.heading.after(100, self.slider)

    def heading_color(self):
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)

    def exit(self):
        if messagebox.askyesno("Đăng xuất", "Bạn có chắc chắn muốn đăng xuất không?", parent=self.root):
            self.root.destroy()

    def student_details(self):
        messagebox.showinfo("Thông báo", "Bạn đã nhấn vào nút 'Sinh viên'")

    def attendance_data(self):
        messagebox.showinfo("Thông báo", "Bạn đã nhấn vào nút 'Điểm danh'")

    def subject_data(self):
        messagebox.showinfo("Thông báo", "Bạn đã nhấn vào nút 'Môn học'")

    def teacher_data(self):
        messagebox.showinfo("Thông báo", "Bạn đã nhấn vào nút 'Giáo viên'")

    def lesson_data(self):
        messagebox.showinfo("Thông báo", "Bạn đã nhấn vào nút 'Buổi học'")

    def report_data(self):
        messagebox.showinfo("Thông báo", "Bạn đã nhấn vào nút 'Thống kê'")

value_from_p1 = None

def new_print(value):
    global value_from_p1
    value_from_p1 = value

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
