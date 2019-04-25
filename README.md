# Face_Recognition_Attendance_System_Using_FaceNet_Siamese_NeuralNetwork
<h1>How to Run:</h1>
Store images in ‘images’ folder, where each person’s images are stored in a folder of their own name, inside ‘images’ folder. Make sure you put approximately 25-30 pictures per person to get accurate results.
Run call_preprocess.py  to create a ‘pre_images’ folder, which will have pre-processed images.
Then run face_recognizer.py to start with face recognition. Press the key ‘n’ to scan another person’s face, and key ‘esc’ to exit the window. The attendance will be updated in the attendance table inside attendance.db database. The attendance table contains four columns, namely EmpName(name of the employee),Date, Status(Present or absent), and the time of entry. 
 <img src="images/ImagesFilePath.png"></img>
View of the ‘images’ folder

<h1>Techniques Used:</h1>
This project works on the concept of Siamese Neural Network. It is a special type of Convolutional Neural Network which is used to calculate the distance of the new image from the ones in the database. It has benefits over traditional CNN, as it is not required to retrain the entire model every time a new image directory is added to the database, which significantly reduces the training time. Also, compared to the traditional CNNs, Siamese Networks require lesser number of pictures for the purpose of training. 
<h1>Requirements:</h1>
o	<b>Language</b>: Python 3.6
o	<b>Libraries</b>: Keras, Tensorflow, OpenCV_python, Numpy, SciPy

<h1>References:</h1>
https://github.com/mohitwildbeast/Facial-Recognition-Using-FaceNet-Siamese-One-Shot-Learning
https://github.com/davidsandberg/facenet
https://lhdasysdrjyazmigojjvml.coursera-apps.org/tree/week4/Face%20Recognition (Convolution Neural Networks course by Deeplearning.ai on Coursera)

