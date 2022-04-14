from flask import Flask,request,redirect,url_for,send_from_directory
import os
import time
import numpy

# Local imports
import face

IMAGE_DIRECTORY = os.getcwd()

app = Flask(__name__)
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
    encodings = face.generate_encodings(image_data)
    os.remove(file_path)
    return {'encodings':encodings.tolist()}

@app.route('/compare', methods=['POST'])
def compare_encodings():
    known = numpy.array(request.json['known_encodings'])
    incoming = numpy.array(request.json['incoming_encodings'])
    return {'comparison_result':bool(face.compare_encodings(known, incoming))}