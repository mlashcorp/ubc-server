from flask import render_template, flash, redirect, session, url_for, request, g
from werkzeug.utils import secure_filename
from app import app
import os      

from UbcMachine import UbcMachine as UbcMachine

ubc_machine = UbcMachine()


@app.route("/request_assay")
def request_assay():    
    global ubc_machine
    return str(ubc_machine.start_new_assay())


@app.route("/start_assay")
def start_assay():
    return render_template("start_assay.html")
    

@app.route("/view_assay")
def view_assay():
    global ubc_machine
    return render_template("view_assay.html")

@app.route("/running_assay")
def running_assay():
    global ubc_machine
    return render_template("running_assay.html")

# Non-html
@app.route("/query_assay")
def query_assay():
    global ubc_machine

    ## Fake: simulates progress change    
    #ubc_machine.state["progress"] += 0.05

    return str(round(ubc_machine.state["progress"]*100, 1) ) # Returns a string with the progress percentage value

# Non-html
@app.route("/cancel_assay")
def cancel_assay():
    global ubc_machine

    assay_id = request.args.get("assay_id")

    cancel_status = ubc_machine.cancel_assay(assay_id)

    print "\n"*10 + "CANCEL REQUESTED FOR ASSAY_ID " + str(assay_id) + "with status = " + str(cancel_status) + "\n"*5

   
    return str(cancel_status) 

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
