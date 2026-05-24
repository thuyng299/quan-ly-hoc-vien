# Quản Lý Học Viên - Student Management System

## Mô Tả
Ứng dụng Python không cần giao diện để quản lý học viên, lớp học, thi cử và điểm số cho trường học/trung tâm.

## Tính Năng Chính

### 1. Quản Lý Học Viên (Bắt buộc) ✅
- Nhập thông tin học viên
- Xuất danh sách học viên
- Cập nhật thông tin học viên
- Xóa học viên
- Tìm kiếm học viên

### 2. Quản Lý Lớp Học
- Tạo lớp học
- Phân sinh viên vào lớp
- Quản lý ban cán sự lớp
- Xem danh sách học viên theo lớp

### 3. Quản Lý Thi Cử
- Tổ chức ca thi
- Quản lý phòng thi
- Xếp thí sinh vào phòng thi

### 4. Quản Lý Điểm
- Nhập điểm thành phần
- Tính điểm trung bình
- Xếp loại học viên

## Cấu Trúc Thư Mục

```
quan-ly-hoc-vien/
├── README.md
├── requirements.txt
├── config/
│   ├── __init__.py
│   └── settings.py
├── students/
│   ├── __init__.py
│   ├── student.py
│   └── student_manager.py
├── classes/
│   └── __init__.py
├── exams/
│   └── __init__.py
├── grades/
│   └── __init__.py
├── utils/
│   ├── __init__.py
│   ├── validators.py
│   ├── file_handler.py
│   └── logger.py
├── data/
│   └── .gitkeep
└── main.py
```

## Hướng Dẫn Cài Đặt

```bash
# Clone repository
git clone https://github.com/thuyng299/quan-ly-hoc-vien.git
cd quan-ly-hoc-vien

# Tạo virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Cài đặt dependencies
pip install -r requirements.txt
```

## Chạy Ứng Dụng

```bash
python main.py
```

## Công Nghệ Sử Dụng
- Python 3.8+
- JSON cho lưu trữ dữ liệu
- Modules tổ chức theo tính năng

## Tác Giả
- @thuyng299
