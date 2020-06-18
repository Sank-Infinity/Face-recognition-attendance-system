# Face-recognition-attendance-system
OpenCV, Python, face-recognition


 Simple OpenCV project for practice purpose.
 In this project, we are going to handle basic fuction in python and libraries like opencv, face-recognition, date time etc.

# How it works ?

system has its own folder where existing images are present.
system takes input through live webcam.
system encodes input and compare with existing encoded images.
If input matches with existing images then system will store information in csv file.
Inforation detail are like NAME, TIME, STATUS

  Name, Time, status
  
  BILLGATES, 19:49:39, Present 
  
  JACK MA, 19:49:48, Present 
  
  SUSHANT, 19:49:58, Present
  
  DICAPRIO, 19:50:01, Present
  
  ELON-MUSK, 19:50:08, Present
  
  MARK, 19:50:15, Present
  
  SHRADDHA, 19:50:19, Present

At the same time system avoid double entry of image.
In the end it gives us proper report in the form of CSV file.

# Environment 

Pycharm

Python 3.6.8

Pillow	7.1.2	

click	7.1.2	7.1.2

cmake	3.17.2	3.17.3

dlib	19.8.1	19.20.0

face-recognition	1.3.0	

face-recognition-models	0.3.0	

facerecognition	0.1.1	

numpy	1.18.5	

opencv-contrib-python	4.2.0.32	

opencv-python	4.2.0.32	

pip	20.1.1	

setuptools	40.6.2	
