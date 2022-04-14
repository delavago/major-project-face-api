import cv2
import face_recognition

cap = cv2.VideoCapture(0)

known_image = face_recognition.load_image_file('./known/known.jpg')
known_image2 = face_recognition.load_image_file('./known/known2.jpg')
known_image3 = face_recognition.load_image_file('./known/known3.jpg')
known_face_encodings = face_recognition.face_encodings(known_image)[0]
known_face_encodings2 = face_recognition.face_encodings(known_image2)[0]
known_face_encodings3 = face_recognition.face_encodings(known_image3)[0]

known_faces = [known_face_encodings,known_face_encodings2,known_face_encodings3]

while(True):
    ret, frame = cap.read()
    cv2.imshow('feed', frame)
    found_encodings = face_recognition.face_encodings(frame)
    for encoding in found_encodings:
        matches = face_recognition.compare_faces(known_faces, encoding,tolerance=0.4)
        print(matches)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()