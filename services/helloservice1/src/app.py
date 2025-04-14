# app.py
from flask import Flask, Response
from google.cloud import storage
from datetime import datetime

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

    return Response(
        "Hello PK -\n"
        "repo: cloudrun-basic-repo-v2\n"
        "service: helloservice1\n"
        f"current time is: {current_time}",
        mimetype="text/plain"
    )


# Run on port 8081 (Cloud Run expects the container to listen on this port)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)