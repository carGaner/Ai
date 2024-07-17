import cv2
import face_recognition
import time
# Load an image of "abhaydev c"
def main(an = True):
    abhaydev_image = face_recognition.load_image_file("abhaydev.jpg")
    abhaydev_encoding = face_recognition.face_encodings(abhaydev_image)[0]
    # Open your webcam
    video_capture = cv2.VideoCapture(0)
    for i in range(0,1000):
        # Capture each frame from the webcam
        ret, frame = video_capture.read()

        # Find all face locations and face encodings in the current frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Check if the face matches "abhaydev c"
            matches = face_recognition.compare_faces([abhaydev_encoding], face_encoding)
            name = "Unknown"
            
            if matches[0]:
                f  = open("a.txt","w")
                f.write("abhaydev")
                f.close()
                name = "Abhaydev c"
            else:
                f  = open("a.txt","w")
                f.write("Unknown person")
                f.close()
                
            # Draw a rectangle around the face and display the name
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if an== False:
            break 
        
    # Release the webcam and close all windows
    
    video_capture.release()
    cv2.destroyAllWindows()
main(True)