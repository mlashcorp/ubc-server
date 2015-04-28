from flask import render_template, flash, redirect, session, url_for, request, g
from werkzeug.utils import secure_filename
from app import app
import os


assay_id_counter = 0
processed_frames = 0

@app.route("/request_assay")
def request_assay():    
    global assay_id_counter
    assay_id_counter += 1
    global processed_frames
    processed_frames = 0

    return str(assay_id_counter)


@app.route("/start_assay")
def start_assay():
    return render_template("start_assay.html")
    

@app.route("/view_assay")
def view_assay():
    return render_template("view_assay.html")

# Non-visible 

@app.route("/query_assay")
def query_assay():
    global processed_frames
    total_frames = 600
    progress = round(float(processed_frames) / float(total_frames), 3)

    ## Fake: simulates progress change
    processed_frames += 10

    return str(progress*100)

# Non-visible
@app.route("/cancel_assay")
def cancel_assay():
    global processed_frames
    processed_frames = 0
    success = 0
    return str(success) 

@app.route("/upload_file", methods=['GET', 'POST'])
def upload_file():

    def create_upload_filename(machine_id, user_id, assay_id, filename):
        return secure_filename(machine_id) + "__" + secure_filename(user_id) + "__" + secure_filename(assay_id) + "__" + secure_filename(filename)

    upload = request.files['upload']

    machine_id = request.form["machine_id"]
    user_id = request.form["user_id"]
    assay_id = request.form["assay_id"]

    filename = create_upload_filename(machine_id, user_id, assay_id, upload.filename)

    upload.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    return render_template("upload_file.html",
                           machine_id=machine_id,
                           assay_id=assay_id,
                           user_id=user_id,
                           filename=filename)
