# Hệ Thống Điểm Danh Sinh Viên

Hệ thống quản lý điểm danh sinh viên được phát triển bằng Python và Tkinter, cung cấp giao diện đồ họa để quản lý thông tin sinh viên, điểm danh, môn học và giáo viên.

## Cấu trúc dự án

```
├── main.py              # Giao diện chính của ứng dụng
├── student.py           # Quản lý thông tin sinh viên
├── teacher.py           # Quản lý thông tin giáo viên
├── subject.py           # Quản lý thông tin môn học
├── lesson.py            # Quản lý thông tin buổi học
├── attendance.py        # Quản lý điểm danh
├── login.py             # Xử lý đăng nhập hệ thống
├── pythonsystem1.sql    # Cấu trúc cơ sở dữ liệu
└── img/                 # Thư mục chứa hình ảnh giao diện
```

## Tính năng chính

- **Quản lý sinh viên**: Thêm, sửa, xóa và xem thông tin sinh viên
- **Quản lý giáo viên**: Thêm, sửa, xóa và xem thông tin giáo viên
- **Quản lý môn học**: Thêm, sửa, xóa và xem thông tin môn học
- **Quản lý buổi học**: Theo dõi các buổi học và lịch học
- **Điểm danh**: Ghi nhận điểm danh cho sinh viên
- **Thống kê**: Xem báo cáo thống kê

## Yêu cầu hệ thống

- Python 3.x
- MySQL Server
- Các thư viện Python:
  - tkinter
  - PIL (Pillow)
  - mysql-connector-python

## Cài đặt

1. Cài đặt các thư viện cần thiết:
```bash
pip install pillow mysql-connector-python
```

2. Cấu hình cơ sở dữ liệu:
- Tạo database MySQL tên `pythonsystem`
- Import file `pythonsystem1.sql` vào database

3. Cấu hình kết nối database:
- Mở file `main.py`
- Cập nhật thông tin kết nối trong hàm `connect_to_database()`:
  ```python
  host='localhost'
  user='root'
  password=''
  database='pythonsystem'
  port=3306
  ```

## Sử dụng

1. Chạy ứng dụng:
```bash
python main.py
```

2. Đăng nhập vào hệ thống với tài khoản admin

3. Sử dụng các chức năng thông qua giao diện đồ họa:
   - Quản lý sinh viên
   - Quản lý giáo viên
   - Quản lý môn học
   - Quản lý buổi học
   - Điểm danh
   - Thống kê

## Giao diện

Hệ thống sử dụng giao diện đồ họa với các nút chức năng chính:
- Hiển thị thời gian và ngày tháng
- Menu chính với các chức năng quản lý
- Nút đăng xuất
- Giao diện thân thiện với người dùng

