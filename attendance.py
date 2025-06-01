import os
from tkinter import *
from tkinter import ttk, messagebox
from time import strftime
import mysql.connector
from tkcalendar import DateEntry
from datetime import datetime

def connect_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='pythonsystem',
            port=3306
        )
        handler = conn.cursor()
        return conn, handler
    except Exception as e:
        messagebox.showerror("Lỗi kết nối", f"Không thể kết nối CSDL: {str(e)}")
        return None, None

class AttendanceSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x800+50+50")
        self.root.title("Hệ thống điểm danh sinh viên")

        # Main container
        main_frame = Frame(self.root)
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # Top section - Lesson selection and controls
        top_frame = LabelFrame(main_frame, text="Thông tin buổi học", font=("Arial", 12, "bold"))
        top_frame.pack(fill="x", pady=(0, 10))

        # Lesson selection
        lesson_frame = Frame(top_frame)
        lesson_frame.pack(fill="x", padx=10, pady=10)
        
        Label(lesson_frame, text="Buổi học:", font=("Arial", 11)).pack(side=LEFT, padx=5)
        self.lesson_var = StringVar()
        self.lesson_combo = ttk.Combobox(lesson_frame, textvariable=self.lesson_var, font=("Arial", 11), width=50, state="readonly")
        self.lesson_combo.pack(side=LEFT, padx=5)
        self.load_lessons()

        Button(lesson_frame, text="Xem danh sách sinh viên", command=self.load_students, 
               font=("Arial", 11), bg="#4CAF50", fg="white").pack(side=LEFT, padx=10)

        # Status and note controls
        control_frame = Frame(top_frame)
        control_frame.pack(fill="x", padx=10, pady=10)

        Label(control_frame, text="Trạng thái:", font=("Arial", 11)).pack(side=LEFT, padx=5)
        self.status_var = StringVar(value="Có mặt")
        status_combo = ttk.Combobox(control_frame, textvariable=self.status_var, 
                                  font=("Arial", 11), width=15, state="readonly")
        status_combo['values'] = ("Có mặt", "Vắng", "Đi muộn")
        status_combo.pack(side=LEFT, padx=5)

        Label(control_frame, text="Ghi chú:", font=("Arial", 11)).pack(side=LEFT, padx=5)
        self.var_note = StringVar()
        Entry(control_frame, textvariable=self.var_note, width=30).pack(side=LEFT, padx=5)

        # Action buttons
        Button(control_frame, text="Lưu", command=self.checkin, 
               font=("Arial", 11, "bold"), bg="#28b779", fg="white").pack(side=LEFT, padx=5)
        Button(control_frame, text="Sửa", command=self.edit_attendance, 
               font=("Arial", 11, "bold"), bg="#5bc0de", fg="white").pack(side=LEFT, padx=5)
        Button(control_frame, text="Xóa", command=self.delete_attendance, 
               font=("Arial", 11, "bold"), bg="#d9534f", fg="white").pack(side=LEFT, padx=5)

        # Middle section - Student details and list
        middle_frame = Frame(main_frame)
        middle_frame.pack(fill="both", expand=True, pady=10)

        # Student details (left side)
        detail_frame = LabelFrame(middle_frame, text="Thông tin sinh viên", font=("Arial", 12, "bold"))
        detail_frame.pack(side=LEFT, fill="y", padx=(0, 10))

        self.var_student_id = StringVar()
        self.var_student_name = StringVar()
        self.var_class = StringVar()
        self.var_time_in = StringVar()
        self.var_date = StringVar(value=strftime("%d/%m/%Y"))
        self.var_status = StringVar()
        self.var_lesson_id = StringVar()

        # Create a grid layout for student details
        details = [
            ("ID Sinh viên:", self.var_student_id),
            ("Tên sinh viên:", self.var_student_name),
            ("Lớp học:", self.var_class),
            ("Giờ vào:", self.var_time_in),
            ("Ngày:", self.var_date),
            ("ID Bài học:", self.var_lesson_id),
            ("Trạng thái:", self.var_status)
        ]

        for i, (label, var) in enumerate(details):
            Label(detail_frame, text=label, font=("Arial", 11)).grid(row=i, column=0, sticky=W, padx=10, pady=5)
            Entry(detail_frame, textvariable=var, state="readonly", width=25).grid(row=i, column=1, padx=10, pady=5)

        # Student list (right side)
        list_frame = LabelFrame(middle_frame, text="Danh sách sinh viên", font=("Arial", 12, "bold"))
        list_frame.pack(side=LEFT, fill="both", expand=True)

        columns = ("Mã SV", "Tên", "Lớp", "Trạng thái")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings", selectmode="browse")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Bottom section - Attendance history
        history_frame = LabelFrame(main_frame, text="Lịch sử điểm danh", font=("Arial", 12, "bold"))
        history_frame.pack(fill="both", expand=True, pady=(10, 0))

        self.history_tree = ttk.Treeview(history_frame, 
            columns=("Mã SV", "Tên", "Lớp", "Thời gian", "Ngày", "Trạng thái", "ID Bài học", "Ghi chú"), 
            show="headings")
        
        for col in ("Mã SV", "Tên", "Lớp", "Thời gian", "Ngày", "Trạng thái", "ID Bài học", "Ghi chú"):
            self.history_tree.heading(col, text=col)
            self.history_tree.column(col, width=100)
        
        self.history_tree.pack(fill="both", expand=True, padx=10, pady=10)
        self.history_tree.bind("<<TreeviewSelect>>", self.on_history_select)
        self.load_attendance_history()

    def load_lessons(self):
        conn, handler = connect_db()
        if not conn:
            return
        try:
            handler.execute("SELECT Lesson_id, Date, Subject_id FROM lesson ORDER BY Date DESC")
            lessons = handler.fetchall()
            self.lesson_combo['values'] = [f"{l[0]} - {l[1]} - Môn {l[2]}" for l in lessons]
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tải danh sách buổi học: {str(e)}", parent=self.root)
        finally:
            conn.close()

    def load_students(self):
        lesson_info = self.lesson_var.get()
        if not lesson_info:
            messagebox.showerror("Lỗi", "Vui lòng chọn buổi học!", parent=self.root)
            return
        lesson_id = lesson_info.split(" - ")[0]
        conn, handler = connect_db()
        if not conn:
            return
        try:
            handler.execute("""
                SELECT s.Student_id, s.Name, s.Class, a.AttendanceStatus
                FROM student s
                JOIN student_has_subject ss ON s.Student_id = ss.Student_id
                JOIN lesson l ON ss.Subject_id = l.Subject_id
                LEFT JOIN attendance a ON a.Student_id = s.Student_id AND a.Lesson_id = l.Lesson_id
                WHERE l.Lesson_id = %s
            """, (lesson_id,))
            students = handler.fetchall()
            self.tree.delete(*self.tree.get_children())
            for s in students:
                status = s[3] if s[3] else "Chưa điểm danh"
                self.tree.insert('', 'end', values=(s[0], s[1], s[2], status))
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tải danh sách sinh viên: {str(e)}", parent=self.root)
        finally:
            conn.close()

    def on_tree_select(self, event):
        selected = self.tree.focus()
        if not selected:
            return
        student = self.tree.item(selected)['values']
        self.var_student_id.set(student[0])
        self.var_student_name.set(student[1])
        self.var_class.set(student[2])
        self.var_time_in.set(datetime.now().strftime("%H:%M:%S"))
        self.var_date.set(strftime("%d/%m/%Y"))
        lesson_info = self.lesson_var.get()
        self.var_lesson_id.set(lesson_info.split(" - ")[0] if lesson_info else "")
        self.var_status.set(self.status_var.get())

    def checkin(self):
        student_id = self.var_student_id.get()
        name = self.var_student_name.get()
        class_name = self.var_class.get()
        time_in = self.var_time_in.get()
        date = self.var_date.get()
        lesson_id = self.var_lesson_id.get()
        status = self.status_var.get()
        note = self.var_note.get()

        if not student_id or not lesson_id:
            messagebox.showerror("Lỗi", "Vui lòng chọn sinh viên và buổi học!", parent=self.root)
            return

        conn, handler = connect_db()
        if not conn:
            return
        try:
            handler.execute("SELECT * FROM attendance WHERE Student_id=%s AND Lesson_id=%s", (student_id, lesson_id))
            if handler.fetchone():
                messagebox.showwarning("Thông báo", "Sinh viên này đã được điểm danh buổi này rồi!", parent=self.root)
                return
            handler.execute(
                "INSERT INTO attendance (IdAuttendance, Student_id, Name, Class, Time_in, Date, Lesson_id, AttendanceStatus, Note) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (f"{student_id}_{lesson_id}_{date}", student_id, name, class_name, time_in, date, lesson_id, status, note)
            )
            conn.commit()
            messagebox.showinfo("Thành công", "Điểm danh thành công!", parent=self.root)
            self.load_attendance_history()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể điểm danh: {str(e)}", parent=self.root)
        finally:
            conn.close()

    def edit_attendance(self):
        student_id = self.var_student_id.get()
        lesson_id = self.var_lesson_id.get()
        status = self.var_status.get()
        note = self.var_note.get()
        if not student_id or not lesson_id:
            messagebox.showerror("Lỗi", "Vui lòng chọn sinh viên và buổi học!", parent=self.root)
            return
        conn, handler = connect_db()
        try:
            handler.execute("UPDATE attendance SET AttendanceStatus=%s, Note=%s WHERE Student_id=%s AND Lesson_id=%s", (status, note, student_id, lesson_id))
            conn.commit()
            messagebox.showinfo("Thành công", "Đã sửa thông tin điểm danh!", parent=self.root)
            self.load_attendance_history()
            self.load_students()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể sửa điểm danh: {str(e)}", parent=self.root)
        finally:
            conn.close()

    def delete_attendance(self):
        student_id = self.var_student_id.get()
        lesson_id = self.var_lesson_id.get()
        if not student_id or not lesson_id:
            messagebox.showerror("Lỗi", "Vui lòng chọn sinh viên và buổi học!", parent=self.root)
            return
        conn, handler = connect_db()
        try:
            handler.execute("DELETE FROM attendance WHERE Student_id=%s AND Lesson_id=%s", (student_id, lesson_id))
            conn.commit()
            messagebox.showinfo("Thành công", "Đã xóa bản ghi điểm danh!", parent=self.root)
            self.load_attendance_history()
            self.load_students()  # Đồng bộ lại danh sách sinh viên
            self.var_note.set("")
            self.var_status.set("Có mặt")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xóa điểm danh: {str(e)}", parent=self.root)
        finally:
            conn.close()

    def load_attendance_history(self):
        conn, handler = connect_db()
        if not conn:
            return
        try:
            handler.execute("""
                SELECT Student_id, Name, Class, Time_in, Date, AttendanceStatus, Lesson_id, Note
                FROM attendance
                ORDER BY Date DESC, Time_in DESC
            """)
            records = handler.fetchall()
            self.history_tree.delete(*self.history_tree.get_children())
            for r in records:
                self.history_tree.insert('', 'end', values=r)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tải lịch sử điểm danh: {str(e)}", parent=self.root)
        finally:
            conn.close()

    def on_history_select(self, event):
        selected = self.history_tree.focus()
        if not selected:
            return
        record = self.history_tree.item(selected)['values']
        self.var_student_id.set(record[0])
        self.var_student_name.set(record[1])
        self.var_class.set(record[2])
        self.var_time_in.set(record[3])
        self.var_date.set(record[4])
        self.var_status.set(record[5])
        self.var_lesson_id.set(record[6])
        self.var_note.set(record[7])

if __name__ == "__main__":
    root = Tk()
    app = AttendanceSystem(root)
    root.mainloop()