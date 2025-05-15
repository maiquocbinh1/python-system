import os
from PIL import Image as PILImage, ImageTk, ImageDraw
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
from time import strftime
from math import *
from main import Face_Recognition_System ,new_print

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #duongdanthumucdetruycapanh

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng nhập")#tieude
        self.root.geometry("1350x700+0+0")#kichthuoc
        self.root.config(bg="#021e2f")#maunen
        today = strftime("%d-%m-%Y")#layngayhientai

        # Biến
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.varcheck = IntVar()

        # Giao diện trái/phải
        Label(self.root, bg="#08A3D2", bd=0).place(x=0, y=0, relheight=1, width=600)#nenxanh
        Label(self.root, bg="#031F3C", bd=0).place(x=600, y=0, relheight=1, relwidth=1)

        # Frame đăng nhập
        login_frame = Frame(self.root, bg="white")#cacnhannhaptrenform
        login_frame.place(x=250, y=100, width=800, height=500)#toado
        #tieudevacacnhan
        Label(login_frame, text="Đăng nhập", font=("times new roman", 30, "bold"), bg="white", fg="#08A3D2").place(x=250, y=40)
        Label(login_frame, text="Email", font=("times new roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=130)
        self.txtuser = ttk.Entry(login_frame, textvariable=self.var_email, font=("times new roman", 15))#nhanemailchoonhapten
        self.txtuser.place(x=250, y=160, height=35, width=350)

        Label(login_frame, text="Mật khẩu", font=("times new roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=220)
        self.txtpass = ttk.Entry(login_frame, textvariable=self.var_password, font=("times new roman", 15), show="*")
        self.txtpass.place(x=250, y=250, height=35, width=350)#onhapmatkhau

        Checkbutton(login_frame, variable=self.varcheck, text="Đăng nhập bằng tài khoản Admin",#varcheck=1 khi tich chon
                    font=("times new roman", 12), onvalue=1, offvalue=0).place(x=250, y=320)

        Button(login_frame, text="Đăng nhập", command=self.login, font=("times new roman", 17, "bold"), fg="white",
               bg="#B00857", bd=0, cursor="hand2").place(x=250, y=400, width=220, height=40)#goi ham selflogin()

        # Đồng hồ
        self.lbl = Label(self.root, bg="#081923", text=today, font=("Book Antiqua", 20, "bold"), fg="white", bd=0)
        self.lbl.place(x=90, y=120, height=450, width=350)
        self.working()#label hien thi anh dong ho


    def clock_image(self, hr, min_, sec_):
        clock = PILImage.new("RGB", (400, 400), (8, 25, 35))#capnhathinhanhdongho
        draw = ImageDraw.Draw(clock)
        clock_path = os.path.join(BASE_DIR, "img", "clock.png")#taodoituongdevelenclock
        bg = PILImage.open(clock_path).resize((300, 300), PILImage.Resampling.LANCZOS)#moanhmatdongho
        clock.paste(bg, (50, 50))

        draw.line((200, 200, 200 + 50 * sin(radians(hr)), 200 - 50 * cos(radians(hr))), fill="#DF005E", width=4)#kimgio
        draw.line((200, 200, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))), fill="white", width=3)#kim phut
        draw.line((200, 200, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill="yellow", width=2)#kimgiay
        draw.ellipse((195, 195, 205, 205), fill="#1AD5D5")#hinhtron

        clock.save(os.path.join(BASE_DIR, "img", "clock_new.png"))

    def working(self):
        now = datetime.now().time()#laythoigianhientai
        hr = (now.hour / 12) * 360
        min_ = (now.minute / 60) * 360
        sec_ = (now.second / 60) * 360

        self.clock_image(hr, min_, sec_)#capnhatanhdongho
        clock_img = os.path.join(BASE_DIR, "img", "clock_new.png")
        self.img = ImageTk.PhotoImage(file=clock_img)
        self.lbl.config(image=self.img)#datanhdonghovaolabel
        self.lbl.after(200, self.working)#goilaihamworking

    def reset(self):#xoanoidung
        self.var_email.set("")
        self.var_password.set("")
        self.varcheck.set(0)

    def login(self):#hamxulikhidangnhap
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Lỗi !!", "Vui lòng nhập đầy đủ thông tin")
            return

        # Tài khoản dùng thử (không cần CSDL)
        email_demo = "admin"
        pass_demo = "123456"

        if self.varcheck.get() == 1:
            if self.var_email.get() == email_demo and self.var_password.get() == pass_demo:
                new_print("0")
                self.reset()#xoathongtindanhapkhidangnhapthanhcong
                messagebox.showinfo("Thông báo", "Đăng nhập  thành công với quyền Admin")
                self.new_window = Toplevel(self.root)#mocuasomoi
                self.app = Face_Recognition_System(self.new_window)
            else:
                messagebox.showerror("Lỗi", "Sai tài khoản hoặc mật khẩu ")
        else:
            if self.var_email.get() == email_demo and self.var_password.get() == pass_demo:#dangnhapvoitucachngdungthongthuong
                new_print("HS001")
                self.reset()
                self.new_window = Toplevel(self.root)
                self.app = Face_Recognition_System (self.new_window)
            else:
                messagebox.showerror("Lỗi", "Sai tài khoản hoặc mật khẩu ")

if __name__ == "__main__":
    root = Tk()
    obj = Login_Window(root)
    root.mainloop()
