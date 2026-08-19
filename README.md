# Blog Automation Tests

Automation test suite cho project Blog cá nhân (Laravel + Django).

## Tech Stack
- Python + Playwright
- pytest

## Test Coverage

### UI Tests
- Trang chủ load thành công
- Trang chi tiết bài viết hiển thị
- Click từ trang chủ sang chi tiết
- Form bình luận hiển thị và điền được

### API Tests
- GET /14/ trả về JSON đúng cấu trúc

## Chạy Test

```bash
# Cài dependency
pip install pytest-playwright
playwright install chromium

# Chạy tất cả
pytest test_blog.py -v

# Chạy 1 test cụ thể
pytest test_blog.py::test_homepage_load -v --headed
