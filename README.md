# Hệ Thống Điểm Danh Sinh Viên 

## Mô tả
Đây là hệ thống quản lý và điểm danh sinh viên sử dụng Python (Tkinter) và MySQL. Hệ thống hỗ trợ đăng nhập bằng tài khoản admin hoặc giáo viên, quản lý sinh viên, môn học, buổi học, giáo viên, điểm danh, và thống kê chuyên sâu. Giao diện trực quan, dễ sử dụng, dữ liệu đồng bộ và xử lý lỗi tốt.

## Chức năng chính
- **Đăng nhập:**
  - Đăng nhập bằng tài khoản admin hoặc giáo viên (email + mật khẩu).
  - Hiển thị tên giáo viên ở góc trên giao diện chính khi đăng nhập bằng giáo viên.
- **Quản lý sinh viên:**
  - Thêm, sửa, xóa, tìm kiếm sinh viên.
- **Quản lý môn học:**
  - Thêm, sửa, xóa, tìm kiếm môn học.
- **Quản lý buổi học:**
  - Thêm, sửa, xóa, tìm kiếm buổi học.
- **Quản lý giáo viên:**
  - Thêm, sửa, xóa, tìm kiếm giáo viên.
- **Điểm danh:**
  - Giao diện điểm danh sinh viên theo buổi học, xác nhận popup, kiểm tra dữ liệu đầu vào.
- **Thống kê:**
  - Thống kê số sinh viên, số lần điểm danh, số lần đi muộn, số lần vắng, xuất CSV.

## Cấu trúc thư mục
```
├── img/                  # Thư mục chứa các file ảnh giao diện (bg1.png, sv.png, sodd.png, late.png, vang.png, ...)
├── Attendance_CSV/       # Thư mục xuất file CSV thống kê (tự động tạo khi xuất CSV, nếu chưa có hãy tự tạo thư mục này)
├── login.py              # Giao diện và xử lý đăng nhập
├── main.py               # Giao diện chính, điều hướng các chức năng
├── student.py            # Quản lý sinh viên
├── subject.py            # Quản lý môn học
├── lesson.py             # Quản lý buổi học
├── teacher.py            # Quản lý giáo viên
├── report_attendance.py  # Thống kê điểm danh, xuất CSV
├── pythonsystem1.sql     # File cấu trúc và dữ liệu mẫu database
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
   - Import file `pythonsystem1.sql` vào MySQL:
     ```bash
     mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS pythonsystem;"
     mysql -u root -p pythonsystem < pythonsystem1.sql
     ```
4. **Đảm bảo các file ảnh giao diện nằm trong thư mục `img/`**
5. **Nếu chưa có thư mục Attendance_CSV, hãy tạo thư mục này để lưu file xuất CSV:**
   ```bash
   mkdir Attendance_CSV
   ```

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
   - Khi bấm "Thống kê" sẽ mở giao diện thống kê chuyên sâu, có thể xuất các file CSV thống kê vào thư mục Attendance_CSV.

## Lưu ý
- Đảm bảo MySQL đang chạy trên máy.
- Tên database phải là `pythonsystem` (có thể đổi trong code nếu bạn dùng tên khác).
- Các file ảnh phải đúng tên và nằm trong thư mục `img/`.
- Nếu xuất CSV bị lỗi, hãy kiểm tra đã có thư mục Attendance_CSV chưa.

## Đóng góp
Nếu bạn muốn đóng góp hoặc phát triển thêm, hãy fork repo và gửi pull request!

---
**Tác giả:**
Mai Quốc Bình


