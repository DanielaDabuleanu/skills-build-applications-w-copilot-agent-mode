# OctoFit Tracker (backend)

This folder contains the backend for the OctoFit Tracker Django project.

Quickstart

- Create the virtual environment (already created for you in this workspace):

```bash
python3 -m venv octofit-tracker/backend/venv
source octofit-tracker/backend/venv/bin/activate
pip install -r octofit-tracker/backend/requirements.txt
```

- Run Django development server from repository root (uses the venv python directly):

```bash
octofit-tracker/backend/venv/bin/python octofit-tracker/backend/octofit_tracker/manage.py runserver 0.0.0.0:8000
```

API scaffolding

- A minimal REST API scaffold has been added with two apps: `users` and `activities`.
- API endpoints are mounted under `/api/`.

Next steps

- Configure a production-ready database and update `DATABASES` in `octofit_tracker/settings.py`.
- Add authentication and permissions as required.
