import cv2
import os

def register_student():
    # Load the pre-trained face detection model (Haar Cascade)
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Get Student Info
    student_id = input("Enter Student ID (e.g., 22UG3-0248): ")
    student_name = input("Enter Student Name: ")

    # Create directory for the student if it doesn't exist
    path = f"datasets/{student_id}_{student_name}"
    if not os.path.exists(path):
        os.makedirs(path)

    # Initialize Webcam
    cap = cv2.VideoCapture(0)
    count = 0

    print(f"Starting capture for {student_name}. Please look at the camera...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            # Crop the face and save it
            face = frame[y:y+h, x:x+w]
            face_path = f"{path}/{count}.jpg"
            cv2.imwrite(face_path, face)
            
            # Draw rectangle on the live feed
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"Captured: {count}", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Registering Student", frame)

        # Stop after 50 samples or if 'q' is pressed
        if cv2.waitKey(1) == ord('q') or count >= 50:
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"Successfully captured 50 samples for {student_name}.")

if __name__ == "__main__":
    register_student()