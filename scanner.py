import cv2
import os

def scan(emp_name):
    face_cascade = cv2.CascadeClassifier(r"C:\Users\Ria\Desktop\RIA\BCA-Study\Sem VI\Software Development\FaceRecognition\Facial-Recognition-Using-FaceNet-Siamese-One-Shot-Learning-master\Facial-Recognition-Using-FaceNet-Siamese-One-Shot-Learning-master\haarcascades\haarcascade_frontalface_default.xml")

    cap = cv2.VideoCapture(0)
    img_counter = 0
    while 1:
        path = r"C:\Users\Ria\Desktop\RIA\BCA-Study\Sem VI\Software Development\FaceRecognition\Facial-Recognition-Using-FaceNet-Siamese-One-Shot-Learning-master\Facial-Recognition-Using-FaceNet-Siamese-One-Shot-Learning-master\images"+"\\"+emp_name
        ret, img = cap.read()

        # convert to gray scale of each frames
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detects faces of different sizes in the input image
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            # To draw a rectangle in a face
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

                # Display an image in a window
        cv2.imshow('img', img)

        # Wait for Esc key to stop
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        elif k % 256 == 32:
            # SPACE pressed
            img_name = emp_name +"{}.png".format(img_counter)
            p = os.path.join(path,img_name)
            cv2.imwrite(p, img)
            print("{} written!".format(img_name))
            img_counter += 1

    # Close the window
    cap.release()
    cv2.destroyAllWindows()
    return True