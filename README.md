# Cloud Run Basics Repo (v2)

This repository demonstrates how to build and deploy multiple Google Cloud Run services using GitHub Actions for CI/CD.

## Folder Structure

```
cloudrun-basics-repo-v2/
│
├── services/
│
├── helloservice1/
│
│ └── src/
│
│
├── app.py
│
│
├── requirements.txt
│
│ └── Dockerfile
│
│
│ └── helloservice2/
│
└── src/
│
├── app.py
│
├── requirements.txt
│
└── Dockerfile
│
├── venv/ # (Optional) Shared virtual environment at the repo root
├── .github/
│ └── workflows/
│ └── deploy.yml # GitHub Actions workflow
├── README.md
└── other files...
```

## Services

- **helloservice1**: A simple Flask-based Cloud Run service.
- **helloservice2**: Placeholder for future services.

## CI/CD

CI/CD is managed using GitHub Actions in `.github/workflows/deploy.yml`.
