# Repository Guidelines

## Project Structure

The Django project lives in `neveprojectt/`. Run management commands from that directory, where `manage.py` is located. The `neveprojectt/` package contains settings and root URL/ASGI/WSGI configuration. The `aplikacion/` app holds models, views, forms, URLs, migrations, and tests. App templates are in `aplikacion/templates/`; CSS, JavaScript, and images are in `aplikacion/static/`. User-uploaded media is stored under `media/`. The SQLite development database is `db.sqlite3`.

## Build, Test, and Development

Activate the repository’s virtual environment (`..\venv\Scripts\Activate.ps1` from `neveprojectt/`), then run:

- `python manage.py runserver` — start the local development server.
- `python manage.py test` — run Django’s test suite.
- `python manage.py check` — check project configuration for common issues.
- `python manage.py makemigrations` and `python manage.py migrate` — create and apply model schema changes.

There is no separate frontend build step; templates and static assets are served by Django during development.

## Coding Style

Use standard Python style: four spaces for indentation, `snake_case` for functions and variables, and `PascalCase` for classes. Keep Django responsibilities in the existing app modules (models, forms, views, and URLs) and use descriptive template and static asset names. Follow the surrounding HTML/CSS/JavaScript formatting when editing frontend files. No formatter or linter configuration is currently present.

## Testing

Tests belong in `aplikacion/tests.py` or focused `test_*.py` modules within the app and should use Django’s `TestCase`. Name test methods `test_<behavior>` and cover relevant view responses, form validation, and model behavior. The current `tests.py` contains only the generated placeholder, so add tests alongside behavior changes. Run `python manage.py test` from `neveprojectt/`.

## Commits and Pull Requests

Git history is unavailable in this checkout, so no existing commit convention can be confirmed. Use short, imperative commit subjects (for example, `Add appointment validation`). Pull requests should explain the user-visible change, note migrations or configuration changes, link related issues when available, and include screenshots for template or styling updates.

## Security and Configuration

`settings.py` currently contains development settings, including a development secret key and `DEBUG = True`. Keep secrets out of commits and use environment-specific settings before deployment. Do not commit local database changes or uploaded/private media unless the change specifically requires fixtures or sample assets.
