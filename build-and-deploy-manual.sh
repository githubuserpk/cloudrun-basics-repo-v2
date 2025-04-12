#!/bin/bash

# Configuration
export PROJECT_ID="pk-aiproject"
export REGION="us-central1"  # e.g., us-central1
export SERVICE_NAME="helloservice1"
export IMAGE_NAME="helloservice1-image"
export REPO_NAME="helloservice-repo"  # Artifact Registry repo name
export BUCKET_NAME="helloservice-bucket-001"

# Enable necessary services
gcloud services enable run.googleapis.com artifactregistry.googleapis.com storage.googleapis.com


# Build & push image to Artifact Registry
gcloud artifacts repositories create $REPO_NAME \
    --repository-format=docker \
    --location=$REGION || echo "Repo may already exist."

gcloud builds submit --tag $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$IMAGE_NAME .

gcloud run deploy $SERVICE_NAME   --image $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$IMAGE_NAME   --region $REGION   --allow-unauthenticated   --execution-environment=gen2 --port=8081


# Optional: Output service URL
gcloud run services describe $SERVICE_NAME --region $REGION --format="value(status.url)"

gcloud run services logs read $SERVICE_NAME   --project=$PROJECT_ID   --region=$REGION   --limit=50

