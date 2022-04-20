import face_recognition

def generate_encodings(image):
    encodings = face_recognition.face_encodings(image);
    print(encodings)
    return encodings[0]

def compare_encodings(known_encodings,incoming_encodings) -> bool:
    return face_recognition.compare_faces([known_encodings],incoming_encodings,tolerance=0.4)[0]

def load_file(path):
    return face_recognition.load_image_file(path)