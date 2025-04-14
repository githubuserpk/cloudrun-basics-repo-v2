Setup steps for cloudrun-basics-repo-v2 - This hosts multiple services

Step 01: Setup venv virtual environment
========================================
python -m venv venv
.\venv\Scripts\activate

Step 02: IDE setup: copy the settings.json to ctrl + shift + p + Preferences: Open Settings (JSON)
========================================================================================
This will help you to login with command prompt instead of PS and it invokes the venv as well 


Step 03: Create cloudrun-cicd-sa service account and grant required roles to the sa and download the key 
==========================================================================================================
gcloud iam service-accounts create cloudrun-cicd-sa ^
  --display-name="GitHub Actions cloudrun cicd service account"



gcloud projects add-iam-policy-binding pk-aiproject ^
  --member="serviceAccount:cloudrun-cicd-sa@pk-aiproject.iam.gserviceaccount.com" ^
  --role="roles/run.admin"

gcloud projects add-iam-policy-binding pk-aiproject ^
  --member="serviceAccount:cloudrun-cicd-sa@pk-aiproject.iam.gserviceaccount.com" ^
  --role="roles/artifactregistry.admin"

gcloud projects add-iam-policy-binding pk-aiproject ^
  --member="serviceAccount:cloudrun-cicd-sa@pk-aiproject.iam.gserviceaccount.com" ^
  --role="roles/editor"

gcloud projects add-iam-policy-binding pk-aiproject ^
  --member="serviceAccount:cloudrun-cicd-sa@pk-aiproject.iam.gserviceaccount.com" ^
  --role="roles/iam.serviceAccountUser"

gcloud projects add-iam-policy-binding pk-aiproject ^
  --member="serviceAccount:cloudrun-cicd-sa@pk-aiproject.iam.gserviceaccount.com" ^
  --role="roles/serviceusage.serviceUsageAdmin"


gcloud projects add-iam-policy-binding pk-aiproject ^
  --member="serviceAccount:cloudrun-cicd-sa@pk-aiproject.iam.gserviceaccount.com" ^
  --role="roles/cloudbuild.builds.editor"

gcloud projects add-iam-policy-binding pk-aiproject ^
  --member="serviceAccount:cloudrun-cicd-sa@pk-aiproject.iam.gserviceaccount.com" ^
  --role="roles/iam.serviceAccountTokenCreator"


gcloud projects add-iam-policy-binding pk-aiproject ^
  --member="serviceAccount:cloudrun-cicd-sa@pk-aiproject.iam.gserviceaccount.com" ^
  --role="roles/artifactregistry.writer"

gcloud projects add-iam-policy-binding pk-aiproject ^
  --member="serviceAccount:cloudrun-cicd-sa@pk-aiproject.iam.gserviceaccount.com" ^
  --role="roles/cloudbuild.builds.editor"

gcloud projects add-iam-policy-binding pk-aiproject ^
  --member="serviceAccount:cloudrun-cicd-sa@pk-aiproject.iam.gserviceaccount.com" ^
  --role="roles/storage.admin"


gcloud projects add-iam-policy-binding pk-aiproject ^
  --member="serviceAccount:cloudrun-cicd-sa@pk-aiproject.iam.gserviceaccount.com" ^
  --role="roles/storage.objectAdmin"

gcloud projects add-iam-policy-binding pk-aiproject ^
  --member="serviceAccount:cloudrun-cicd-sa@pk-aiproject.iam.gserviceaccount.com" ^
  --role="roles/storage.objects.list"


gcloud projects add-iam-policy-binding pk-aiproject ^
  --member="serviceAccount:cloudrun-cicd-sa@pk-aiproject.iam.gserviceaccount.com" ^
  --role="roles/storage.objectViewer"


# also assigned storage object admin from UI

gcloud iam service-accounts keys create cloudrun-cicd-sa-key.json ^
  --iam-account=cloudrun-cicd-sa@pk-aiproject.iam.gserviceaccount.com


Step 04: In github UI, create a git hub actions template for cloud run.  It will create the 
    workflows and the yml file 

Step 05: Give permissions to cicd service account separately as it has UBLA enabled, so even if you 
give perms at project level, it does not matter 

gcloud storage buckets add-iam-policy-binding pk-aiproject_cloudbuild ^
  --member="serviceAccount:cloudrun-cicd-sa@pk-aiproject.iam.gserviceaccount.com" ^
  --role="roles/storage.objectAdmin"


