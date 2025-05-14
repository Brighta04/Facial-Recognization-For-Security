import cv2
import os

# Load OpenCV's pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def collect_training_data():
    # Initialize camera
    cap = cv2.VideoCapture(0)

    faces = []
    labels = []
    current_id = 0
    label_dict = {}

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces_detected = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces_detected:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw green rectangle around faces

        # Show the image with detected faces
        cv2.imshow('Face Detection', frame)

        # Add faces to training data (example, assuming you press 'c' to capture data)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):  # Capture on pressing 'c'
            faces.append(gray[y:y + h, x:x + w])
            labels.append(current_id)
            label_dict[current_id] = f"Person_{current_id}"
            print(f"Captured face for {label_dict[current_id]}")

        # Exit on pressing 'q'
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    return faces, labels, label_dict

def main():
    faces, labels, label_dict = collect_training_data()

    if faces:
        print("Training on collected data...")
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces, np.array(labels))

        # Save the recognizer to a file
        recognizer.save('trainer.yml')
        print("Model trained and saved as 'trainer.yml'")
        print("Label dictionary:", label_dict)
    else:
        print("No faces collected!")

if __name__ == "__main__":
    main()
