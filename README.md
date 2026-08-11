# Laravel Django blog

Blog cá nhân kết nối Laravel Frontend với Django API, tích hợp AI phản hồi bình luận.

## Tech Stack

- Backend API: Django Rest Framework
- Frontend: Laravel + Vuejs + Bootstrap
- AI: Gemini, OpenRouter
- Automation Test: Playwright (Python)

## Chạy test

- bash

## Cài dependency

pip install pytest-playwright
playwright install chromium

# Chạy test

pytest test_blog.py -v --headed --slowmo 1000
