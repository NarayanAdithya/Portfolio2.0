# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

**Run the app (development):**
```bash
python adithya.py
```

**Build Tailwind CSS (watches for changes):**
```bash
npm run build
```

**Production server:**
```bash
gunicorn -k gevent --workers=1 adithya:app
```

**Database migrations:**
```bash
flask db migrate -m "message"
flask db upgrade
```

## Architecture

Flask + Tailwind CSS personal portfolio site with a real-time chat bot.

**Entry point:** `adithya.py` — initializes Flask app with `flask_socketio.SocketIO` and runs it.

**App factory:** `app/__init__.py` — creates Flask app, registers blueprints (`auth`, `bot`, `main`), initializes SQLAlchemy, Flask-Migrate, Flask-Login, Flask-Admin, and SocketIO.

**Blueprints:**
- `app/routes.py` (main) — home/portfolio page, image upload
- `app/auth/` — login/logout with three-part password verification (k1/k2/k3 fields)
- `app/bot/` — real-time chat via SocketIO events; stores history in MongoDB; calls external bot API at `ADI_BOT_URL`

**Data:**
- **SQLite** (`app.db` via SQLAlchemy) — `TechStack` and `Project` models displayed on portfolio page
- **MongoDB** (Atlas, via pymongo) — chat history per visitor IP

**Frontend:** Jinja2 templates in `app/templates/`. CSS source is `app/static/css/index.css` (Tailwind input), compiled to `app/static/css/tailwind.css`.

**Admin:** Flask-Admin at `/admin/` — CRUD for `TechStack` and `Project`. Requires login. Admin user is hardcoded as user ID 3.

## Environment Variables

Required in a `.env` file or environment:
- `environment` — `"Development"` or `"Production"`
- `SECRET_KEY`
- `UPLOAD_FOLDER` / `PROJECT_UPLOAD_FOLDER` — paths for uploaded images
- `ADI_BOT_ENDPOINT` — external bot API URL
- `ADI_BOT_USERNAME` / `ADI_BOT_PASSWORD` — MongoDB Atlas credentials
- `MONGO_URI` — MongoDB connection string
