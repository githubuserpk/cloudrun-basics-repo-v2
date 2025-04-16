# app.py
from flask import Flask, Response
from google.cloud import storage
from datetime import datetime

import requests
import io

import pkg_resources
print(pkg_resources.get_distribution("google-cloud-storage"))

app = Flask(__name__)

# Replace with your bucket and file name
# BUCKET_NAME = "pkbucket-001"
# FILE_NAME = "pkfile.txt"

# @app.route("/")
# def read_file():
#     """Reads the first line of the file from GCS and returns it as an HTML response."""
#     try:
#         client = storage.Client()
#         bucket = client.bucket(BUCKET_NAME)
#         blob = bucket.blob(FILE_NAME)

#         # Read the file from GCS
#         content = blob.download_as_text().splitlines()
#         first_line = content[0] if content else "File is empty."

#         return Response(first_line, mimetype="text/plain")
#     except Exception as e:
#         return Response(f"Error reading file: {str(e)}", status=500)



@app.route("/")
def hello():
    """Simple route to verify the service is running."""
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Format the current time

    result2 = invoke_cloudrun_server()
    if result2:
        print("Successfully invoked CLOUDRUN server:")
        print(result2)
    else:
        print("Failed to invoke CLOUDRUN server.")


    return Response(
        "Hello PK -\n"
        "repo: cloudrun-basic-repo-v2\n"
        "service: helloservice1\n"
        f"current time is: {current_time}\n"
        f"invoked cloudrun server vm on port 8081 result: {result2}",
        mimetype="text/plain"
    )




# Assuming you know the internal IP address of your CLOUDRUN server VM
# CLOUDRUN_SERVER_IP = os.environ.get("CLOUDRUN_SERVER_IP")
# CLOUDRUN_SERVER_IP = "34.58.118.42"
CLOUDRUN_SERVER_IP = "10.0.1.2"
CLOUDRUN_SERVER_PORT = 8082
CLOUDRUN_SERVER_ENDPOINT = f"http://{CLOUDRUN_SERVER_IP}:{CLOUDRUN_SERVER_PORT}"  # Replace /your-endpoint

def invoke_cloudrun_server():
    if not CLOUDRUN_SERVER_IP:
        print("Error: CLOUDRUN_SERVER_IP environment variable not set.")
        return None

    try:
        response = requests.get(CLOUDRUN_SERVER_ENDPOINT)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()  # Or response.text if it's not JSON
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to CLOUDRUN server: {e}")
        return None


# Run on port 8081 (Cloud Run expects the container to listen on this port)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)


