# Cloud Run Basics Repo (v2)

This repository demonstrates how to build and deploy multiple Google Cloud Run services using GitHub Actions for CI/CD.

## Folder Structure

cloudrun-basics-repo-v2/ │ ├── services/ │ ├── helloservice1/ │ │ └── src/ │ │ ├── app.py │ │ ├── requirements.txt │ │ └── Dockerfile │ │ │ └── helloservice2/ │ └── src/ │ ├── app.py │ ├── requirements.txt │ └── Dockerfile │ ├── venv/ # (Optional) Shared virtual environment at the repo root ├── .github/ │ └── workflows/ │ └── deploy.yml # GitHub Actions workflow ├── README.md └── other files...
