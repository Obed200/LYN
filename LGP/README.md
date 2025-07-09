# Lyn Gallery

A responsive Django-based gallery website with user authentication, admin management, image/video upload, and more.

## Features
- User registration, login, profile, and password management
- Admin dashboard with quick actions and stats
- Gallery with image upload/download (admin), video on home page
- Logo and site settings management (admin)
- Contact form
- Responsive design (Bootstrap)

## Setup Instructions

1. **Clone the repository**

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Apply migrations**
```bash
python manage.py migrate
```

4. **Create a superuser (admin)**
```bash
python manage.py createsuperuser
```

5. **Run the development server**
```bash
python manage.py runserver
```

6. **Access the site**
- Main site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## File Uploads
- Media files (images, videos, logos, avatars) are stored in the `media/` directory.
- Static files (CSS, JS, images) are in the `static/` directory.

## Notes
- For production, set `DEBUG = False` and configure `ALLOWED_HOSTS` in `settings.py`.
- Use a production-ready database and static/media file server for deployment.

--- 