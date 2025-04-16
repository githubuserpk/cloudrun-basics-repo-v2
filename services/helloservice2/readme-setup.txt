Step 0: good to enable network management api [ to Troubleshoot if ssh to vm is not working ]
======================

Step 1 create network 
=====================

gcloud compute networks create vpc-int-us \
    --project=pk-aiproject \
    --subnet-mode=custom \
    --description="VPC network for my Tini server and Cloud Run"

gcloud compute networks subnets create subnet-int-us \
    --project=pk-aiproject \
    --region=us-south1 \
    --network=vpc-int-us \
    --range=10.0.1.0/24  # Choose an appropriate IP range for your subnet
    --description="Subnet for my Tini server"

Step 2: Enable api vpc access vpcaccess.googleapis.com

Step 2: Create vm tiny server
==============================

gcloud compute instances create tiny-server-vm ^
  --project=pk-aiproject ^
  --zone=us-south1-b ^
  --machine-type=e2-micro ^
  --network-interface=network=vpc-int-us,subnet=subnet-int-us ^
  --boot-disk-size=10GB ^
  --boot-disk-type=pd-standard ^
  --image=debian-12-bookworm-v20250311 ^
  --image-project=debian-cloud ^
  --labels=serverless-access=enabled,tier=backend ^
  --tags=http-server,https-server



Step 2 enable vpc access api 
====================================================================================
gcloud services enable vpcaccess.googleapis.com

Step 3: Use Option 1 or Option 2

Create cloudrun connector Create a network connector cidr range for cloud run to come through ie egress
====================================================================================
check if any cide range overlap are already being used 
gcloud compute networks subnets list ^
  --project=pk-aiproject ^
  --filter="network=vpc-int-us" ^
  --format="table(name, ipCidrRange, region)"


# Option-1 : serverless vpc access connector:
==============================================
gcloud compute networks vpc-access connectors create cloudrun-connector ^
  --project=pk-aiproject ^
  --region=us-south1 ^
  --network=vpc-int-us ^
  --range=10.11.0.0/28

# Deleting the serverless access vpc connector 
gcloud compute networks vpc-access connectors delete cloudrun-connector ^
    --project=pk-aiproject ^
    --region=us-south1


# option-2: direct vpc egress:   AAAA + BBBB
==============================

AAAA

gcloud run deploy YOUR_CLOUD_RUN_SERVICE_NAME \
    --project=YOUR_GCP_PROJECT_ID \
    --region=YOUR_GCP_REGION \
    --image=YOUR_CONTAINER_IMAGE \
    --network=pkvpc \
    --subnet=pkvpc-subnet  # Specify the subnet where your Tini VM resides
    --vpc-egress=all-traffic  # Or 'private-ranges-only'
    --allow-internal

    OR 
gcloud run services update helloservice1 \
    --project=pk-aiproject \
    --region=us-south1 \
    --network=vpc-int-us \
    --subnet=subnet-int-us  # Replace with the subnet where your Tini VM is
    --vpc-egress=all-traffic \
    --allow-internal

BBBB 

# create firewall rule to allow the traffic
=============================================
gcloud compute firewall-rules create allow-cloud-run-to-tini \
    --project=pk-aiproject \
    --network=vpc-int-us \
    --allow=tcp:8082 \
    --source-ranges=10.0.1.0/24    # Use the IP range of your Cloud Run subnet ie subnet-int-us
    --target-tags=tini-server      # If your Tini VM has a network tag



===============
modified steps:
===============
gcloud compute networks create vpc-int-usc1 \
    --project=pk-aiproject \
    --subnet-mode=custom \
    --description="VPC network for my Tini server and Cloud Run"

Done

gcloud compute networks subnets create subnet-int-usc1 \
    --project=pk-aiproject \
    --region=us-central1 \
    --network=vpc-int-usc1 \
    --range=10.0.1.0/24  # Choose an appropriate IP range for your subnet
    --description="Subnet for my Tini server"

Done

create vpc network:
===================

create vm
============
gcloud compute instances create cloudrun-server-vm \
  --project=pk-aiproject \
  --zone=us-central1-a \
  --machine-type=e2-micro \
  --network-interface=network=vpc-int-usc1,subnet=subnet-int-usc1 \
  --boot-disk-size=10GB \
  --boot-disk-type=pd-standard \
  --image=debian-12-bookworm-v20250311 \
  --image-project=debian-cloud \
  --labels=serverless-access=enabled,tier=backend \
  --tags=http-server,https-server,cloudrun-server


firewall: allow ssh port 22
===========================
gcloud compute firewall-rules create allow-ssh-to-crvm \
    --project=pk-aiproject \
    --network=vpc-int-usc1 \
    --allow=tcp:22 \
    --source-ranges=0.0.0.0/0    # Use the IP range of your Cloud Run subnet ie subnet-int-us
    --target-tags=http-server,cloudrun-server      # If your cloudrun VM has a network tag

firewall: allow http 8082 to crvm 

gcloud compute firewall-rules create allow-http-to-crvm \
    --project=pk-aiproject \
    --network=vpc-int-usc1 \
    --allow=tcp:80,tcp:443,tcp:8082 \
    --source-ranges=0.0.0.0/0 \
    --target-tags=http-server,cloudrun-server



setup nginx
===============
sudo apt-get update
sudo apt-get install -y nginx
ps auwx | grep nginx

sudo nano /etc/nginx/sites-available/default
edit to port 8082 for default_server

make sure nginx is running using netstat
sudo netstat -tulnp | grep 8082



Access the web server from http://<EXT-IP>:8082 

restart web server if it is not running
sudo systemctl restart nginx

Done

# create firewall rule to allow the traffic
=============================================
gcloud compute firewall-rules create allow-cloud-run-to-crvm \
    --project=pk-aiproject \
    --network=vpc-int-usc1 \
    --allow=tcp:8082 \
    --source-ranges=10.0.1.0/24    # Use the IP range of your Cloud Run subnet ie subnet-int-usc1
    --target-tags=http-server      # If your Tini VM has a network tag

Done

# allow access for cloud run to access the vm
==============================================

gcloud run services update helloservice1 \
    --project=pk-aiproject \
    --region=us-central1 \
    --network=vpc-int-usc1 \
    --subnet=subnet-int-usc1  # Replace with the subnet where your Tini VM is
    --vpc-egress=all-traffic \
    --allow-internal

Done

Troubleshooting logs 
gcloud run services logs read helloservice1 \
  --project=pk-aiproject \
  --region=us-central1 \
  --limit=50




