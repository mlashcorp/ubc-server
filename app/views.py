from flask import render_template, flash, redirect, session, url_for, request, g
from werkzeug.utils import secure_filename
from app import app
import os

@app.route("/upload_file", methods=['GET', 'POST'])
def upload_file():
    upload = request.files['upload']

    machine_id = request.form["machine_id"]
    user_id = request.form["user_id"]
    assay_id = request.form["assay_id"]

    filename = secure_filename(upload.filename)

    upload.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    return render_template("upload_file.html",
                           machine_id=machine_id,
                           assay_id=assay_id,
                           user_id=user_id,
                           filename=filename)
