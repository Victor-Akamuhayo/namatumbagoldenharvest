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
   - `CLOUDINARY_URL`: Cloudinary's API environment URL, required for durable image uploads on Vercel.
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

Then sign in at `/admin/`. Only trusted staff accounts should be granted admin access. Gallery, news, and product image forms include a local file picker. On Vercel, uploaded files are stored in Cloudinary, so configure `CLOUDINARY_URL` before deploying; without it, Vercel will refuse production startup rather than save uploads to temporary storage. Existing image URLs continue to work. Vercel's Django integration runs `collectstatic` during the build.

## Checks

```powershell
python manage.py check
python manage.py test core
```
