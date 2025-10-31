from flask import Flask, request, jsonify
from google.cloud import storage
import os

app = Flask(__name__)

# Initialize GCS client
storage_client = storage.Client()
BUCKET_NAME = os.environ.get("BUCKET_NAME", "your-bucket-name")

@app.route('/')
def index():
    return '''
    <h2>Upload a file to Google Cloud Storage</h2>
    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file" />
        <input type="submit" />
    </form>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if not file:
        return "No file uploaded.", 400

    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file)

    # Make file public
    blob.make_public()

    return jsonify({
        "message": f"File uploaded successfully to {BUCKET_NAME}",
        "public_url": blob.public_url
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
