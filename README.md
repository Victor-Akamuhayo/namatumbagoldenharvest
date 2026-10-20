# Namutumba Golden Harvest SACCO

Public website for Namutumba Golden Harvest Farmers and Traders SACCO, built with Django.

## Run locally

Uses Python 3.14, pinned for Vercel in `.python-version`.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. Local development uses SQLite by default.

## Deploy to Vercel

Vercel detects this Django project from `manage.py` and uses the WSGI application configured in `namatumbagoldenharvest/settings.py`. Static assets are collected and served by Vercel when `STATIC_ROOT` is configured; no custom serverless entrypoint is required.

1. Push this project to a Git provider and import the repository into Vercel. Keep the project root at the repository root and use Vercel's detected Django build settings.
2. Provision a persistent PostgreSQL database through a Vercel Marketplace integration or another PostgreSQL provider. SQLite is only for local development; Vercel function storage is ephemeral.
3. Add these variables to the Vercel project for Preview and Production:
   - `DJANGO_SECRET_KEY`: a long, unique random secret.
   - `DJANGO_DEBUG`: `false`.
   - `DATABASE_URL`: the PostgreSQL connection URL from your database provider.
4. For custom domains, set `DJANGO_ALLOWED_HOSTS` to comma-separated hostnames without schemes, and set `DJANGO_CSRF_TRUSTED_ORIGINS` to comma-separated HTTPS origins. Vercel-provided deployment hostnames are added automatically.
5. Apply database migrations against the configured production database before relying on contact and membership submissions:

```powershell
$env:DJANGO_SECRET_KEY = "your-production-secret"
$env:DJANGO_DEBUG = "false"
$env:DATABASE_URL = "your-production-postgresql-url"
python manage.py migrate
```

After migrations, create the administrator account using the same production environment values:

```powershell
python manage.py createsuperuser
```

Then sign in at `/admin/`. Only trusted staff accounts should be granted admin access. Gallery images, news article images, and product images are managed there using public HTTPS image URLs; upload files to an image host first and paste their direct image URL into the relevant image URL field. Vercel's Django integration runs `collectstatic` during the build.

## Checks

```powershell
python manage.py check
python manage.py test core
```
