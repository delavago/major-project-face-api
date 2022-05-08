from logging import exception
from flask import Flask,request,redirect,url_for,send_from_directory
from flask_cors import CORS
import os
import time
import numpy

# Local imports
import face

IMAGE_DIRECTORY = os.getcwd()

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = IMAGE_DIRECTORY

@app.route('/')
def index():
    return ':)))))) - kinky'

@app.route('/encode', methods=['POST'])
def encode():
    file = request.files['image']
    file_name = 'temp-'+str(int(time.time()*1000000))+'-.jpeg'
    file.save(os.path.join(app.config['UPLOAD_FOLDER'],file_name))
    file_path = os.path.join(app.config['UPLOAD_FOLDER'],file_name)
    image_data = face.load_file(file_path)

    try:
        encodings = face.generate_encodings(image_data)
    except:
        print("Facial encodings failed")

    os.remove(file_path)
    return {'status': '200 OK','encodings':encodings.tolist()}

@app.route('/compare', methods=['POST'])
def compare_encodings():
    known = numpy.array(request.json['known_encodings'])
    incoming = numpy.array(request.json['incoming_encodings'])
    return {'status': '200 OK', 'comparison_result':bool(face.compare_encodings(known, incoming))}

@app.route('/find-match',methods=['POST'])
def find_match():
    known = numpy.array(request.json['known_encodings'])
    customer_face_data_list = request.json['customer_face_data_list']
    result = None
    for record in customer_face_data_list:
        incoming = numpy.array(record['faceData']['encodings'])
        if bool(face.compare_encodings(known, incoming))==True:
            result = record;
            break;
    
    return {'status': '200 OK', 'found_match': result}