# IN16 Study Manager (BISWA Class Manager)

A full-featured Django web application for IN16 students to manage study resources — notes, groups, announcements, reminders, and more.

---

## Features

- 🔐 Login / Register with student profile
- 📚 Units listing with note & group counts
- 📝 Notes per unit with full-detail view
- 👥 Study groups with member listings
- 🎓 Full class list with search & gender filter
- 📣 Announcements board
- ⏰ Personal class reminders
- 🌙 Dark mode toggle
- 📱 Fully responsive (Bootstrap 5)
- ⚙️ Django Admin panel for all data management

---

## Tech Stack

- **Backend**: Django 4.2+
- **Frontend**: Bootstrap 5.3 + Bootstrap Icons + Google Fonts (Sora, JetBrains Mono)
- **Database**: SQLite (local) / PostgreSQL (production)
- **Static files**: WhiteNoise (no separate static server needed)
- **Server**: Gunicorn
- **Auth**: Django built-in

---

## Deploy to Render (Recommended)

### Option A — One-Click with render.yaml

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → New → Blueprint
3. Connect your repo — Render reads `render.yaml` automatically
4. Click **Apply** — Render creates the web service + PostgreSQL database
5. Done! Visit your `.onrender.com` URL

> The `render.yaml` auto-generates a `SECRET_KEY` and a random admin password.  
> Find the generated `DJANGO_SUPERUSER_PASSWORD` in your Render service **Environment** tab.

### Option B — Manual Render setup

1. Push repo to GitHub
2. Render → New Web Service → connect repo
3. Set **Build Command**: `./build.sh`
4. Set **Start Command**: `gunicorn IN16_Study_Manager.wsgi:application --bind 0.0.0.0:$PORT --workers 2`
5. Add a **PostgreSQL** database from Render dashboard
6. Set these **Environment Variables** on the service:

| Variable | Value |
|---|---|
| `SECRET_KEY` | (generate a random string) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `.onrender.com` |
| `CSRF_TRUSTED_ORIGINS` | `https://your-app.onrender.com` |
| `DATABASE_URL` | (paste from Render PostgreSQL → Connect) |
| `DJANGO_SUPERUSER_USERNAME` | `admin` |
| `DJANGO_SUPERUSER_EMAIL` | `admin@in16.ac.ke` |
| `DJANGO_SUPERUSER_PASSWORD` | (choose a strong password) |

---

## Deploy to Railway

1. Push repo to GitHub
2. [railway.app](https://railway.app) → New Project → Deploy from GitHub repo
3. Add a **PostgreSQL** plugin from Railway dashboard
4. Railway auto-sets `DATABASE_URL` — just add:

| Variable | Value |
|---|---|
| `SECRET_KEY` | (generate random) |
| `DEBUG` | `False` |
| `DJANGO_SUPERUSER_PASSWORD` | (your admin password) |
| `CSRF_TRUSTED_ORIGINS` | `https://your-app.up.railway.app` |
| `ALLOWED_HOSTS` | `.up.railway.app` |

Railway reads `nixpacks.toml` and runs migrations + collectstatic automatically.

---

## Local Development

```bash
# Clone and enter the project
git clone <your-repo>
cd biswa_class_manager

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy env file
cp .env.example .env            # Edit if needed

# Run migrations
python manage.py migrate

# (Optional) Seed sample data
python seed_data.py

# Start server
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**  
Admin: **http://127.0.0.1:8000/admin/** → `admin` / `admin123`

---

## Project Structure

```
biswa_class_manager/
├── manage.py
├── seed_data.py              ← Populate sample data (local only)
├── requirements.txt
├── Procfile                  ← Gunicorn start command
├── build.sh                  ← Render build script
├── render.yaml               ← Render Blueprint (one-click deploy)
├── railway.json              ← Railway config
├── nixpacks.toml             ← Railway build steps
├── .env.example              ← Local environment template
├── .gitignore
├── IN16_Study_Manager/
│   ├── settings.py           ← Production-ready (env vars + WhiteNoise + PostgreSQL)
│   ├── urls.py
│   └── wsgi.py
└── notes_app/
    ├── models.py             ← Unit, Student, Note, Group, Announcement, Reminder
    ├── views.py
    ├── urls.py
    ├── forms.py
    ├── admin.py
    ├── management/
    │   └── commands/
    │       └── create_superuser_if_not_exists.py
    └── templates/notes_app/
        ├── base.html
        ├── login.html / register.html
        ├── home.html
        ├── units.html / notes.html / note_detail.html
        ├── groups.html / students.html
        ├── announcements.html / reminders.html
        └── ...
```
