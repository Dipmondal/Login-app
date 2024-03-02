import firebase_admin,os, smtplib
from firebase_admin import db, credentials, storage, auth
from flask import Flask, render_template


databaseUrl = "https://test-95a2c-default-rtdb.asia-southeast1.firebasedatabase.app/"

cred = credentials.Certificate(f"{os.getcwd()}/social media app/credential/cread.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": databaseUrl,
    'storageBucket': "test-95a2c.appspot.com"  # Only the bucket name is needed
})

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(os.getcwd()+"/social media app/templates/index.html")
if __name__ == "__main__":
	app.run(debug=True)