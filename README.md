# Little Star Public School — Website Backend

Django + Django REST Framework backend for the LSPS website. Every
piece of content described in the requirements doc is modeled as a
Django app, editable from **Django Admin** with no coding required,
and exposed to your React frontend as a read-only REST API (plus a
handful of public POST endpoints for forms).

Stack decisions (as confirmed): **SQLite** for the database, **local
media folder** for file storage. Both are easy to swap later — see
"Moving to production on AWS" below.

---

## 1. Setup

```bash
# 1. Create & activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# edit .env — at minimum set DJANGO_SECRET_KEY to something random

# 4. Create the database tables
python manage.py makemigrations
python manage.py migrate

# 5. Create your admin login
python manage.py createsuperuser

# 6. Run it
python manage.py runserver
```

- Django Admin: **http://127.0.0.1:8000/admin/**
- API root: **http://127.0.0.1:8000/api/**

Every endpoint below also has a browsable HTML view if you open it
directly in a browser (courtesy of DRF's BrowsableAPIRenderer) —
useful for checking your data while wiring up React.

---

## 2. Project layout

```
lsps_backend/
├── manage.py
├── config/              # settings, root urls, wsgi/asgi
├── apps/
│   ├── core/             # site settings, floating buttons, popup-automailer recipients
│   ├── pages/             # Home welcome msg, About Us, Chairman/Principal messages, highlights, quick links
│   ├── sliders/           # Banner slider + Admission popup settings
│   ├── testimonials/
│   ├── academics/         # ClassCategory + 9 per-class content types
│   ├── admissions/        # process steps, fees, required docs, enquiries, school-visit bookings
│   ├── infrastructure/    # facilities by category
│   ├── studentlife/       # activity categories + posts + photos
│   ├── newsevents/        # news, events, announcements, circulars, notice board
│   ├── gallery/           # albums, photos, videos
│   ├── downloads/         # download categories + documents
│   └── contact/           # contact details, phone numbers, social links, contact form
├── media/                 # uploaded images/PDFs/videos (gitignored)
└── requirements.txt
```

Every list-type model (banners, highlights, facilities, testimonials,
etc.) has `order` and `is_active` fields, so admins can reorder or
hide items from Admin without deleting them — the public API only
ever returns `is_active=True` rows.

---

## 3. API reference

All paths are prefixed with `/api/`. List/detail endpoints are
read-only (`GET`) unless marked **POST**.

| Area | Endpoint | Notes |
|---|---|---|
| Core | `core/settings/` | Site-wide settings singleton |
| Core | `core/floating-buttons/` | Apply Now / WhatsApp / Call Now |
| Home/About | `pages/home-content/` | Welcome message |
| Home/About | `pages/chairman-message/`, `pages/principal-message/` | |
| Home/About | `pages/about-us/` | |
| Home/About | `pages/highlights/`, `pages/why-choose-us/`, `pages/quick-links/` | |
| Sliders | `sliders/banners/` | Auto-slide banners |
| Sliders | `sliders/admission-popup/` | Popup content/settings |
| Testimonials | `testimonials/` | |
| Academics | `academics/classes/` | List of classes |
| Academics | `academics/classes/{slug}/` | **Everything for one class** in a single call (curriculum, calendar, timings, uniform, homework, worksheets, gallery, videos, downloads) |
| Academics | `academics/curriculum/?class=<slug>` | Also: `academic-calendar`, `school-timings`, `uniform-guidelines`, `holiday-homework`, `worksheets`, `gallery`, `videos`, `downloads` — all filterable by `?class=<slug>` |
| Admissions | `admissions/process-steps/`, `fee-structure/`, `required-documents/`, `form-download/` | |
| Admissions | **POST** `admissions/enquiry/` | Admissions-page enquiry form |
| Admissions | **POST** `admissions/popup-enquiry/` | Home-page popup form — triggers the automailer |
| Admissions | **POST** `admissions/school-visit/` | Book a School Visit |
| Infrastructure | `infrastructure/?category=<key>` | smart_classroom / computer_lab / library / sports / medical / transport |
| Student Life | `student-life/categories/`, `student-life/posts/?category=<id>` | |
| News & Events | `news-events/news/`, `events/`, `announcements/`, `circulars/`, `notice-board/` | |
| Gallery | `gallery/albums/` (list), `gallery/albums/{id}/` (full, with photos+videos) | |
| Downloads | `downloads/categories/` (nested docs), `downloads/documents/?category=<id>` | |
| Contact | `contact/details/` | Address, email, timings, map, WhatsApp, phones, social links |
| Contact | **POST** `contact/messages/` | Contact form |

---

## 4. The admission-popup automailer

Requirement: *"After submission, an automailer send to the respective
mail id which can be updated from the admin panel."*

- Admin Panel → **Admissions → Notification Recipients (Popup Automailer)**
  is where you add/remove the email addresses that get notified.
- Every new `AdmissionEnquiry` (from the popup, the Admissions page
  form, or a school-visit booking) fires a signal
  (`apps/admissions/signals.py`) that emails all active recipients.
- With the default `.env`, emails are printed to the console instead
  of actually sent (`django.core.mail.backends.console.EmailBackend`)
  so you can test locally without SMTP credentials. Fill in
  `EMAIL_HOST_USER` / `EMAIL_HOST_PASSWORD` in `.env` and switch
  `DJANGO_EMAIL_BACKEND` to `django.core.mail.backends.smtp.EmailBackend`
  when you're ready to send real emails.

---

## 5. Connecting your React frontend

- CORS is already configured (`django-cors-headers`) — just add your
  dev/prod React origins to `CORS_ALLOWED_ORIGINS` in `.env`.
- Public POST endpoints (enquiry, popup-enquiry, school-visit,
  contact/messages) accept **anonymous** requests — no auth/token
  needed from the frontend.
- Everything else is read-only and public too, so your React app can
  just `fetch()`/`axios.get()` these directly — no login required to
  render the site.
- Uploaded images/files are served from `/media/...` — when you fetch
  e.g. `sliders/banners/`, the `image` field is already an absolute
  URL you can drop straight into an `<img src>`.

---

## 6. Moving to production on AWS

Two things were deliberately kept simple for now and are easy to swap
without touching your models or API:

**Database → PostgreSQL**
1. `pip install psycopg2-binary` (already commented in `requirements.txt`)
2. Replace the `DATABASES` block in `config/settings.py` with your
   Postgres credentials (or read them from `.env`)
3. `python manage.py migrate` again against the new database

**Media storage → AWS S3**
1. `pip install django-storages[s3]` (already commented in `requirements.txt`)
2. Add `storages` to `INSTALLED_APPS` and set `DEFAULT_FILE_STORAGE` /
   `AWS_STORAGE_BUCKET_NAME` etc. in `config/settings.py`
3. Existing files in `/media/` will need to be uploaded to the bucket
   (e.g. via `aws s3 sync media/ s3://your-bucket/media/`)

Also for production: set `DJANGO_DEBUG=False`, fill in
`DJANGO_ALLOWED_HOSTS` with your real domain, and run
`python manage.py collectstatic` (Whitenoise is already wired up to
serve static files).

---

## 7. Admin Panel quick tour

- **Academics → Class Categories**: open any class (e.g. "Grade II")
  to edit its curriculum, calendar, timings, uniform guidelines,
  holiday homework, worksheets, gallery, videos and downloads all
  from one page (or use the standalone list views for bulk edits).
- **Admissions → Admission Enquiries**: every enquiry from the popup,
  the Admissions page, and every school-visit booking lands here with
  an editable status (New / Follow-up / Admitted / Closed).
- Singleton content (Site Settings, Home welcome message, About Us,
  Chairman's/Principal's message, Admission Popup, Contact Details)
  only ever has one row — the "Add" button disables itself once it
  exists, so nobody accidentally creates a duplicate.
"# lsps_backend" 
