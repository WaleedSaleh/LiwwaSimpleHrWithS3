from flask import ( Flask, jsonify, render_template, request,
                    redirect, send_file, jsonify, abort)
from flask_cors import CORS
from helpers import download_file, upload_file, list_files
from werkzeug.utils import secure_filename
import secrets
import  os
import mariadb
import sys
from flask_file_upload import FileUpload
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt


#initiating the app
app = Flask(__name__)
#Connnecction URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/liwwa_simple_hr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Instantiating the database object
db = SQLAlchemy(app)


file_upload = FileUpload(app, db)
#adding the secret key
app.config['SECRET_KEY'] = secrets.token_hex(32)

#Allowed Extensions
app.config["ALLOWED_EXTENSIONS"] = ["pdf","docx"]


AWS_ACCESS_KEY_ID = "SECRET!"

AWS_SECERET_ACCESS_KEY = "SECRET!"


#Conffigure the file content length
# 4MB max-limit.
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024

#add the upload folder ()
app.config['UPLOAD_FOLDER'] = "uploads"

UPLOAD_FOLDER = 'uploads'

#S3 Bucket name
BUCKET = "liwwa-hr-test"


#enable the cors issue
CORS(app=app,resources={r'/*': {'origins': '*'}})

#Json Encoder




def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]

#Models
#Creating the models
#User Admin Model
class UserAdmin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean,default=True)
    created_at = db.Column(db.DateTime, default=dt.utcnow)


#Applicant Model
@file_upload.Model
class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), unique=True, nullable=False)
    date_of_birth = db.Column(db.DateTime)
    years_of_experience = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'),
        nullable=False)
    attachment = file_upload.Column()
    created_at = db.Column(db.DateTime, default=dt.utcnow)

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'         : self.id,
           'full_name': self.full_name,
           'date_of_birth': self.date_of_birth,
           'years_of_experience': self.years_of_experience,
           'department_id': self.department_id,
           'attachment' : self.attachment__file_name,
           'created_at': self.created_at
       }

#department Model
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    applicant_id = db.relationship('Applicant', backref='department', lazy=True)
    created_at = db.Column(db.DateTime, default=dt.utcnow)

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id': self.id,
           'name': self.name,
       }



#storage_view
@app.route("/index")
def index():
    files_list = list_files(BUCKET) if list_files(BUCKET) is not None else None
    return render_template("index.html", files_list=files_list)

#upload_view
@app.route("/upload", methods=['POST'])
def upload():
    try:
        if request.method == "POST":
            print("Entered Here => ", file=sys.stdout)
            full_name = request.form.get("full_name",'')
            date_of_birth = request.form.get("date_of_birth")
            years_of_experience = request.form.get("years_of_experience")
            department_id = request.form.get("department_id")
            attachment = request.files['attachment']
            if attachment is None:
                return jsonify({"404":"File not found"})
            if attachment.filename == "":
                return jsonify({"404":"File not found"})
            if attachment and allowed_file(attachment.filename):
                attachment.save(os.path.join(UPLOAD_FOLDER, attachment.filename))
                upload_file(f"uploads/{attachment.filename}", BUCKET)
                file_type = allowed_file(attachment.filename)
                applicant = Applicant(full_name = full_name, date_of_birth= date_of_birth,
                years_of_experience=5,department_id=department_id,
                attachment__file_name=attachment.filename, attachment__file_type = file_type)
                db.session.add(applicant)
                db.session.commit()
                return jsonify({"status":201, "filename":f"{attachment.filename}"})
            else:
                return jsonify({"type_error":"please check your file extension!"})
        elif request.method == "GET":
            return jsonify({"405":"Method Not allowed"})
    except Exception as e:
        print(f"The error in upload {e} => ", file=sys.stderr)
        return jsonify({'500':'Something went wrong'})


@app.route("/download/<path:filename>", methods=['GET'])
def download(filename):
    try:
        if request.method == 'GET':
            print("In the get download", file=sys.stdout)
            output = download_file(filename, BUCKET)
            return send_file(filename, as_attachment=True)
    except Exception as e:
        print(f"error in download => {e}", file=sys.stdout)
        return jsonify({"error": "something went wrong"})

#For making the login route
@app.route("/login")
def login():
    pass

#Get departments
@app.route('/get-departments', methods=['GET'])
def get_departments():
    return jsonify(json_list = [i.serialize for i in Department.query.all()])

@app.route("/get-applicants", methods=['POST'])
def get_all_applicants():
    return jsonify(json_list = [i.serialize for i in Applicant.query.all()])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


if __name__ == "__main__":
    app.run(debug= True)
