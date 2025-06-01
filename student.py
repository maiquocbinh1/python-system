from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from time import strftime
import mysql.connector

students_data = []
classes_data = []

def connect_to_database():
    try:
        db_connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='pythonsystem',
            port=3306
        )
        print("Connection successful!")
        return db_connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Hệ thống điểm danh sinh viên")
        today = strftime("%d-%m-%Y")

        # Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_radio1 = StringVar()
        self.var_com_search = StringVar()
        self.var_search = StringVar()
        self.var_class = StringVar()
        self.var_nameclass = StringVar()
        self.var_com_searchclass = StringVar()
        self.var_searchclass = StringVar()

        # ========== Top Frame (Time, Date, Title) ==========
        top_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        top_frame.place(x=10, y=10, width=1510, height=80)

        # Time and date
        self.time_label = Label(top_frame, font=("yu gothic ui", 13, "bold"), bg="white", fg="black")
        self.time_label.place(x=10, y=5, width=200, height=25)
        self.date_label = Label(top_frame, font=("yu gothic ui", 13, "bold"), bg="white", fg="black")
        self.date_label.place(x=10, y=35, width=200, height=25)
        self.update_time()
        self.date_label.config(text=strftime("%d-%m-%Y"))

        # Title
        title_label = Label(top_frame, text="Quản lý thông tin sinh viên", font=("yu gothic ui", 28, "bold"), bg="white", fg="black")
        title_label.place(x=300, y=10, width=900, height=60)

        # ========== Main Frame ==========
        main_frame = Frame(self.root, bg="#e9e9e9", bd=2, relief=RIDGE)
        main_frame.place(x=10, y=100, width=1510, height=670)

        # ========== Left Frame (Student Info) ==========
        left_frame = LabelFrame(main_frame, bd=2, bg="white", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=730, height=646)

        label_Update_att = Label(left_frame, bg="white", fg="red2", text="Thông tin sinh viên", font=("yu gothic ui", 16, "bold"))
        label_Update_att.place(x=0, y=1, width=700, height=42)

        # Course Info
        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Thông tin khoá học", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=55, width=720, height=130)

        dep_label = Label(current_course_frame, text="Chuyên ngành", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 13, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Chọn chuyên ngành", "Điện tử viễn thông", "IT", "Cơ khí", "Điện", "Kế toán", "Tự động hóa")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        course_label = Label(current_course_frame, text="Hệ đào tạo", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 13, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Chọn hệ", "Chính quy", "Liên Thông", "CLC")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        year_label = Label(current_course_frame, text="Năm học", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 13, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Chọn năm học", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        semester_label = Label(current_course_frame, text="Học kì", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)
        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 13, "bold"), state="readonly", width=20)
        semester_combo["values"] = ("Chọn học kì", "Học kì I", "Học kì II")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Info
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Thông tin lớp học", font=("times new roman", 13, "bold"))
        class_student_frame.place(x=5, y=195, width=720, height=420)

        studentID_label = Label(class_student_frame, text="ID Sinh Viên:", font=("times new roman", 13, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        studentID_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_std_id, font=("times new roman", 13, "bold"), state="normal")
        studentID_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        studentName_label = Label(class_student_frame, text="Tên Sinh Viên:", font=("times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)
        studentName_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_std_name, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        class_div_label = Label(class_student_frame, text="Lớp học:", font=("times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        class_div_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_div, font=("times new roman", 13, "bold"))
        class_div_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        roll_no_label = Label(class_student_frame, text="CMND", font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        roll_no_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_roll, font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        gender_label = Label(class_student_frame, text="Giới tính:", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 13, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Nam", "Nữ", "Khác")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        dob_label = Label(class_student_frame, text="Ngày sinh:", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        self.dob_entry = DateEntry(class_student_frame, width=18, bd=3, selectmode='day', year=2021, month=5, font=("times new roman", 13), day=22, date_pattern='dd/mm/yyyy')
        self.dob_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        email_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_email, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        phone_label = Label(class_student_frame, text="SĐT:", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=10, sticky=W)
        phone_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_phone, font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=10, sticky=W)

        address_label = Label(class_student_frame, text="Địa chỉ:", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
        address_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_address, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)


        # Button frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=280, width=715, height=35)
        save_btn = Button(btn_frame, text="Lưu", command=self.add_data, font=("times new roman", 13, "bold"), bg="#38a6f0", fg="white", width=17)
        save_btn.grid(row=0, column=0)
        update_btn = Button(btn_frame, text="Sửa", command=self.update_data, font=("times new roman", 13, "bold"), bg="#38a6f0", fg="white", width=17)
        update_btn.grid(row=0, column=1)
        delete_btn = Button(btn_frame, text="Xóa", command=self.delete_data, font=("times new roman", 13, "bold"), bg="#38a6f0", fg="white", width=17)
        delete_btn.grid(row=0, column=2)
        reset_btn = Button(btn_frame, text="Làm mới", command=self.reset_data, font=("times new roman", 13, "bold"), bg="#38a6f0", fg="white", width=17)
        reset_btn.grid(row=0, column=3)

        # ========== Right Frame (Search & Table) ==========
        right_frame = LabelFrame(main_frame, bd=2, bg="white", font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=720, height=330)

        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Hệ Thống Tìm kiếm", font=("yu gothic ui", 13, "bold"))
        search_frame.place(x=5, y=5, width=710, height=70)
        search_label = Label(search_frame, text="Tìm kiếm theo :", font=("times new roman", 13, "bold"), bg="white", fg="red2")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        search_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), state="readonly", width=13, textvariable=self.var_com_search)
        search_combo["values"] = ("ID Sinh viên", "Tên sinh viên", "Lớp biên chế")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 13, "bold"), textvariable=self.var_search)
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        search_btn = Button(search_frame, text="Tìm kiếm", font=("times new roman", 12, "bold"), bg="#38a6f0", fg="white", width=12, command=self.search_data)
        search_btn.grid(row=0, column=3, padx=4)
        showAll_btn = Button(search_frame, text="Xem tất cả", font=("times new roman", 12, "bold"), bg="#38a6f0", fg="white", width=12, command=self.fetch_data)
        showAll_btn.grid(row=0, column=4, padx=4)

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=85, width=710, height=230)
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column=("id", "dep", "course", "year", "sem", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("id", text="ID Sinh viên")
        self.student_table.heading("dep", text="Chuyên ngành")
        self.student_table.heading("course", text="Hệ đào tạo")
        self.student_table.heading("year", text="Năm học")
        self.student_table.heading("sem", text="Học kì")
        self.student_table.heading("name", text="Họ tên")
        self.student_table.heading("div", text="Lớp biên chế")
        self.student_table.heading("roll", text="CMND")
        self.student_table.heading("gender", text="Giới tính")
        self.student_table.heading("dob", text="Ngày sinh")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Số điện thoại")
        self.student_table.heading("address", text="Địa chỉ")
        self.student_table["show"] = "headings"
        for col in ("id", "dep", "course", "year", "sem", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "photo"):
            self.student_table.column(col, width=100)
        self.student_table.column("photo", width=150)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # ========== Bottom Right Frame (Class Management) ==========
        underright_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, font=("yu gothic ui", 12, "bold"))
        underright_frame.place(x=750, y=345, width=720, height=310)
        label_studentsb = Label(underright_frame, bg="white", fg="red2", text="Quản lý lớp học", font=("yu gothic ui", 14, "bold"))
        label_studentsb.place(x=0, y=1, width=700, height=35)
        search_combo = ttk.Combobox(underright_frame, font=("times new roman", 12, "bold"), textvariable=self.var_com_searchclass, state="readonly", width=12)
        search_combo["values"] = ("Lớp", "Tên lớp")
        search_combo.current(0)
        search_combo.grid(row=0, column=0, padx=10, pady=40, sticky=W)
        searchstd_entry = ttk.Entry(underright_frame, textvariable=self.var_searchclass, width=13, font=("times new roman", 11, "bold"))
        searchstd_entry.grid(row=0, column=1, padx=5, pady=35, sticky=W)
        searchstd_btn = Button(underright_frame, command=self.search_Classdata, text="Tìm kiếm", font=("times new roman", 11, "bold"), bg="#38a6f0", fg="white", width=10)
        searchstd_btn.grid(row=0, column=2, padx=5)
        showAllstd_btn = Button(underright_frame, text="Xem tất cả", command=self.fetch_Classdata, font=("times new roman", 11, "bold"), bg="#38a6f0", fg="white", width=10)
        showAllstd_btn.grid(row=0, column=3, padx=5)
        studentid_label = Label(underright_frame, text="Lớp học:", font=("times new roman", 12, "bold"), bg="white", width=12)
        studentid_label.place(x=20, y=120, width=100)
        studentid_entry = ttk.Entry(underright_frame, textvariable=self.var_class, font=("times new roman", 12, "bold"), width=20)
        studentid_entry.place(x=135, y=120, width=200)
        subsub_label = Label(underright_frame, text="Tên lớp học:", font=("times new roman", 12, "bold"), bg="white")
        subsub_label.place(x=20, y=165, width=80)
        subsub_entry = ttk.Entry(underright_frame, width=22, textvariable=self.var_nameclass, font=("times new roman", 12, "bold"))
        subsub_entry.place(x=135, y=165, width=200)
        btn_framestd = Frame(underright_frame, bg="white", bd=2, relief=RIDGE)
        btn_framestd = Frame(underright_frame, bg="white", bd=2, relief=RIDGE)
        btn_framestd.place(x=20, y=245, width=455, height=55)
        addTc_btn = Button(btn_framestd, text="Thêm mới", command=self.add_Classdata, font=("times new roman", 12, "bold"), bg="#fbd568", fg="#996319", width=10)
        addTc_btn.grid(row=9, column=0, pady=10, padx=5)
        deleteTc_btn = Button(btn_framestd, text="Xóa", command=self.delete_Classdata, font=("times new roman", 12, "bold"), bg="#fbd568", fg="#996319", width=10)
        deleteTc_btn.grid(row=9, column=1, pady=10, padx=5)
        updateTc_btn = Button(btn_framestd, text="Cập nhật", command=self.update_Classdata, font=("times new roman", 12, "bold"), bg="#fbd568", fg="#996319", width=10)
        updateTc_btn.grid(row=9, column=2, pady=10, padx=5)
        resetTc_btn = Button(btn_framestd, text="Làm mới", command=self.reset_Classdata, font=("times new roman", 12, "bold"), bg="#fbd568", fg="#996319", width=10)
        resetTc_btn.grid(row=9, column=3, pady=10, padx=5)
        tablestd_frame = Frame(underright_frame, bd=2, relief=RIDGE, bg="white")
        tablestd_frame.place(x=490, y=40, width=200, height=260)
        scroll_x = ttk.Scrollbar(tablestd_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tablestd_frame, orient=VERTICAL)
        self.StudentTable = ttk.Treeview(tablestd_frame, column=("class", "name"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.StudentTable.xview)
        scroll_y.config(command=self.StudentTable.yview)
        self.StudentTable.heading("class", text="Lớp học")
        self.StudentTable.heading("name", text="Tên")
        self.StudentTable["show"] = "headings"
        self.StudentTable.column("class", width=80)
        self.StudentTable.column("name", width=80)
        self.StudentTable.pack(fill=BOTH, expand=1)
        self.StudentTable.bind("<ButtonRelease>", self.get_cursorClass)
        self.fetch_Classdata()

    def update_time(self):
        self.time_label.config(text=strftime('%H:%M:%S %p'))
        self.time_label.after(1000, self.update_time)

    # CRUD and search methods for students and classes
    def add_data(self):
        if self.var_std_id.get() == "" or self.var_std_name.get() == "" or self.var_div.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin", parent=self.root)
            return

        db_connection = connect_to_database()
        if not db_connection:
            return

        try:
            db_query = db_connection.cursor()
            # Check if student ID already exists
            db_query.execute("SELECT * FROM student WHERE Student_id = %s", (self.var_std_id.get(),))
            if db_query.fetchone():
                messagebox.showerror("Lỗi", "ID sinh viên đã tồn tại", parent=self.root)
                return

            # Insert new student
            sql = """INSERT INTO student (Student_id, Dep, course, Year, Semester, Name, Class, Roll, Gender, Dob, Email, Phone, Address) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (
                self.var_std_id.get(),
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.dob_entry.get_date().strftime('%d/%m/%Y'),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get()
            )
            db_query.execute(sql, values)
            db_connection.commit()
            messagebox.showinfo("Thành công", "Thêm thông tin sinh viên thành công", parent=self.root)
            self.fetch_data()
            self.reset_data()
        except mysql.connector.Error as err:
            messagebox.showerror("Lỗi", f"Lỗi cơ sở dữ liệu: {err}", parent=self.root)
        finally:
            if db_connection.is_connected():
                db_query.close()
                db_connection.close()

    def fetch_data(self):
        db_connection = connect_to_database()
        if not db_connection:
            return

        try:
            db_query = db_connection.cursor()
            db_query.execute("SELECT * FROM student")
            rows = db_query.fetchall()
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Lỗi", f"Lỗi cơ sở dữ liệu: {err}", parent=self.root)
        finally:
            if db_connection.is_connected():
                db_query.close()
                db_connection.close()

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        if not data:
            return
        self.var_std_id.set(data[0])
        self.var_dep.set(data[1])
        self.var_course.set(data[2])
        self.var_year.set(data[3])
        self.var_semester.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        try:
            from datetime import datetime
            dob_str = data[9]
            if dob_str:
                dob_date = datetime.strptime(dob_str, '%d/%m/%Y').date()
                self.dob_entry.set_date(dob_date)
        except Exception:
            from datetime import date
            self.dob_entry.set_date(date.today())
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        if len(data) > 13:
            self.var_radio1.set(data[13])
        else:
            self.var_radio1.set("")

    def update_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng chọn sinh viên cần cập nhật", parent=self.root)
            return

        db_connection = connect_to_database()
        if not db_connection:
            return

        try:
            db_query = db_connection.cursor()
            sql = """UPDATE student SET 
                    Dep = %s, course = %s, Year = %s, Semester = %s, 
                    Name = %s, Class = %s, Roll = %s, Gender = %s, 
                    Dob = %s, Email = %s, Phone = %s, Address = %s 
                    WHERE Student_id = %s"""
            values = (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.dob_entry.get_date().strftime('%d/%m/%Y'),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_std_id.get()
            )
            db_query.execute(sql, values)
            db_connection.commit()
            messagebox.showinfo("Thành công", "Cập nhật thông tin sinh viên thành công", parent=self.root)
            self.fetch_data()
            self.reset_data()
        except mysql.connector.Error as err:
            messagebox.showerror("Lỗi", f"Lỗi cơ sở dữ liệu: {err}", parent=self.root)
        finally:
            if db_connection.is_connected():
                db_query.close()
                db_connection.close()

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng chọn sinh viên cần xóa", parent=self.root)
            return

        if not messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa sinh viên này?", parent=self.root):
            return

        db_connection = connect_to_database()
        if not db_connection:
            return

        try:
            db_query = db_connection.cursor()
            db_query.execute("DELETE FROM student WHERE Student_id = %s", (self.var_std_id.get(),))
            db_connection.commit()
            messagebox.showinfo("Thành công", "Xóa sinh viên thành công", parent=self.root)
            self.fetch_data()
            self.reset_data()
        except mysql.connector.Error as err:
            messagebox.showerror("Lỗi", f"Lỗi cơ sở dữ liệu: {err}", parent=self.root)
        finally:
            if db_connection.is_connected():
                db_query.close()
                db_connection.close()

    def reset_data(self):
        self.var_dep.set("Chọn chuyên ngành")
        self.var_course.set("Chọn hệ")
        self.var_year.set("Chọn năm học")
        self.var_semester.set("Chọn học kì")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("Nam")
        self.dob_entry.set_date(strftime("%d/%m/%Y"))
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")

    def search_data(self):
        if self.var_com_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập thông tin tìm kiếm", parent=self.root)
            return

        db_connection = connect_to_database()
        if not db_connection:
            return

        try:
            db_query = db_connection.cursor()
            search_field = ""
            if self.var_com_search.get() == "ID Sinh viên":
                search_field = "Student_id"
            elif self.var_com_search.get() == "Tên sinh viên":
                search_field = "Name"
            elif self.var_com_search.get() == "Lớp biên chế":
                search_field = "Class"

            sql = f"SELECT * FROM student WHERE {search_field} LIKE %s"
            db_query.execute(sql, (f"%{self.var_search.get()}%",))
            rows = db_query.fetchall()
            
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
            
            if rows:
                messagebox.showinfo("Thông báo", f"Có {len(rows)} bản ghi thỏa mãn điều kiện", parent=self.root)
            else:
                messagebox.showinfo("Thông báo", "Không có bản ghi nào thỏa mãn điều kiện", parent=self.root)
        except mysql.connector.Error as err:
            messagebox.showerror("Lỗi", f"Lỗi cơ sở dữ liệu: {err}", parent=self.root)
        finally:
            if db_connection.is_connected():
                db_query.close()
                db_connection.close()

    # Class management (in-memory)
    def add_Classdata(self):
        if self.var_class.get() == "" or self.var_nameclass.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin", parent=self.root)
            return

        db_connection = connect_to_database()
        if not db_connection:
            return

        try:
            db_query = db_connection.cursor()
            # Check if class already exists
            db_query.execute("SELECT * FROM class WHERE Class = %s", (self.var_class.get(),))
            if db_query.fetchone():
                messagebox.showerror("Lỗi", "Lớp học đã tồn tại", parent=self.root)
                return

            # Insert new class
            sql = "INSERT INTO class (Class, Name) VALUES (%s, %s)"
            values = (self.var_class.get(), self.var_nameclass.get())
            db_query.execute(sql, values)
            db_connection.commit()
            messagebox.showinfo("Thành công", "Thêm thông tin lớp học thành công", parent=self.root)
            self.fetch_Classdata()
            self.reset_Classdata()
        except mysql.connector.Error as err:
            messagebox.showerror("Lỗi", f"Lỗi cơ sở dữ liệu: {err}", parent=self.root)
        finally:
            if db_connection.is_connected():
                db_query.close()
                db_connection.close()

    def fetch_Classdata(self):
        db_connection = connect_to_database()
        if not db_connection:
            return

        try:
            db_query = db_connection.cursor()
            db_query.execute("SELECT * FROM class")
            rows = db_query.fetchall()
            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert("", END, values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Lỗi", f"Lỗi cơ sở dữ liệu: {err}", parent=self.root)
        finally:
            if db_connection.is_connected():
                db_query.close()
                db_connection.close()

    def get_cursorClass(self, event=""):
        cursor_row = self.StudentTable.focus()
        content = self.StudentTable.item(cursor_row)
        rows = content['values']
        if not rows:
            return
        self.var_class.set(rows[0])
        self.var_nameclass.set(rows[1])

    def update_Classdata(self):
        if self.var_class.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng chọn lớp cần cập nhật", parent=self.root)
            return

        db_connection = connect_to_database()
        if not db_connection:
            return

        try:
            db_query = db_connection.cursor()
            sql = "UPDATE class SET Name = %s WHERE Class = %s"
            values = (self.var_nameclass.get(), self.var_class.get())
            db_query.execute(sql, values)
            db_connection.commit()
            messagebox.showinfo("Thành công", "Cập nhật thông tin lớp học thành công", parent=self.root)
            self.fetch_Classdata()
            self.reset_Classdata()
        except mysql.connector.Error as err:
            messagebox.showerror("Lỗi", f"Lỗi cơ sở dữ liệu: {err}", parent=self.root)
        finally:
            if db_connection.is_connected():
                db_query.close()
                db_connection.close()

    def delete_Classdata(self):
        if self.var_class.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng chọn lớp cần xóa", parent=self.root)
            return

        if not messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa lớp học này?", parent=self.root):
            return

        db_connection = connect_to_database()
        if not db_connection:
            return

        try:
            db_query = db_connection.cursor()
            db_query.execute("DELETE FROM class WHERE Class = %s", (self.var_class.get(),))
            db_connection.commit()
            messagebox.showinfo("Thành công", "Xóa lớp học thành công", parent=self.root)
            self.fetch_Classdata()
            self.reset_Classdata()
        except mysql.connector.Error as err:
            messagebox.showerror("Lỗi", f"Lỗi cơ sở dữ liệu: {err}", parent=self.root)
        finally:
            if db_connection.is_connected():
                db_query.close()
                db_connection.close()

    def reset_Classdata(self):
        self.var_class.set("")
        self.var_nameclass.set("")

    def search_Classdata(self):
        if self.var_com_searchclass.get() == "" or self.var_searchclass.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập thông tin tìm kiếm", parent=self.root)
            return

        db_connection = connect_to_database()
        if not db_connection:
            return

        try:
            db_query = db_connection.cursor()
            search_field = "Class" if self.var_com_searchclass.get() == "Lớp" else "Name"
            sql = f"SELECT * FROM class WHERE {search_field} LIKE %s"
            db_query.execute(sql, (f"%{self.var_searchclass.get()}%",))
            rows = db_query.fetchall()
            
            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert("", END, values=row)
            
            if rows:
                messagebox.showinfo("Thông báo", f"Có {len(rows)} bản ghi thỏa mãn điều kiện", parent=self.root)
            else:
                messagebox.showinfo("Thông báo", "Không có bản ghi nào thỏa mãn điều kiện", parent=self.root)
        except mysql.connector.Error as err:
            messagebox.showerror("Lỗi", f"Lỗi cơ sở dữ liệu: {err}", parent=self.root)
        finally:
            if db_connection.is_connected():
                db_query.close()
                db_connection.close()

if __name__ == "__main__":
    db_connection = connect_to_database()
    if db_connection:
        db_connection.close()
    root = Tk()
    obj = Student(root)
    root.mainloop()