# Hệ Thống Điểm Danh Sinh Viên 

## Mô tả
Đây là hệ thống quản lý và điểm danh sinh viên sử dụng giao diện Tkinter và cơ sở dữ liệu MySQL. Hệ thống hỗ trợ đăng nhập bằng tài khoản admin hoặc giáo viên, quản lý sinh viên, môn học, buổi học, giáo viên, điểm danh, và thống kê chuyên sâu.

## Chức năng chính
- **Đăng nhập:**
  - Đăng nhập bằng tài khoản admin hoặc giáo viên (email + mật khẩu).
- **Quản lý sinh viên:**
  - Thêm, sửa, xóa, tìm kiếm sinh viên.
- **Quản lý môn học:**
  - Thêm, sửa, xóa, tìm kiếm môn học.
- **Quản lý buổi học:**
  - Thêm, sửa, xóa, tìm kiếm buổi học.
- **Quản lý giáo viên:**
  - Thêm, sửa, xóa, tìm kiếm giáo viên.
- **Điểm danh:**
  - Giao diện điểm danh sinh viên theo buổi học.
- **Thống kê:**
  - Thống kê số sinh viên, số lần điểm danh, số lần đi muộn, số lần vắng, xuất CSV.

## Cấu trúc thư mục
```
├── img/                  # Thư mục chứa các file ảnh giao diện
├── Attendance_CSV/       # Thư mục xuất file CSV thống kê
├── login.py              # Giao diện và xử lý đăng nhập
├── main.py               # Giao diện chính, điều hướng các chức năng
├── student.py            # Quản lý sinh viên
├── subject.py            # Quản lý môn học
├── lesson.py             # Quản lý buổi học
├── teacher.py            # Quản lý giáo viên
├── report_attendance.py  # Thống kê điểm danh
├── pythonsystem.sql      # File cấu trúc và dữ liệu mẫu database
└── README.md             # File hướng dẫn này
```

## Hướng dẫn cài đặt
1. **Cài đặt Python 3.x**
2. **Cài đặt các thư viện cần thiết:**
   ```bash
   pip install pillow tk mysql-connector-python tkcalendar
   ```
3. **Cài đặt MySQL và import database:**
   - Tạo database tên `pythonsystem`.
   - Import file `pythonsystem.sql` vào MySQL:
     ```bash
     mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS pythonsystem;"
     mysql -u root -p pythonsystem < pythonsystem.sql
     ```
4. **Đảm bảo các file ảnh giao diện nằm trong thư mục `img/`**

## Hướng dẫn sử dụng
1. **Chạy chương trình:**
   ```bash
   python login.py
   ```
2. **Đăng nhập:**
   - Nếu chọn "Đăng nhập bằng tài khoản Admin": nhập tài khoản/mật khẩu admin (bảng `admin`).
   - Nếu không chọn: nhập email/mật khẩu giáo viên (bảng `teacher`).
3. **Sử dụng các chức năng trên giao diện chính:**
   - Quản lý sinh viên, môn học, buổi học, giáo viên, điểm danh, thống kê.
   - Khi bấm "Thống kê" sẽ mở giao diện thống kê chuyên sâu.

## Lưu ý
- Đảm bảo MySQL đang chạy trên máy.
- Tên database phải là `pythonsystem` (có thể đổi trong code nếu bạn dùng tên khác).
- Các file ảnh phải đúng tên và nằm trong thư mục `img/`.

<<<<<<< HEAD
## Đóng góp
Nếu bạn muốn đóng góp hoặc phát triển thêm, hãy fork repo và gửi pull request!

---
**Tác giả:**
binh
