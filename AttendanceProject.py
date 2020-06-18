# import required libraries
import cv2 as cv
import numpy as np
import face_recognition
import os
from datetime import datetime

# Path of existing images
path = 'AttendanceResourcesImages'
images = []
classStudents = []

# creating list of name of existing images
myList = os.listdir(path)
print(myList)

# read all images from folder and load into list
for i in myList:
    currentImage = cv.imread(f'{path}/{i}')
    images.append(currentImage)
    classStudents.append(os.path.splitext(i)[0])

print(classStudents)


# funtion for encoding every images that has been loaded
def findEncodings(images):
    # list for encoded image
    encodeList = []
    for img in images:
        # conver image format BGR 2 RGB
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        # encode image
        encode = face_recognition.face_encodings(img)[0]
        # append encoded list in encodelist
        encodeList.append(encode)
        print('*')
    #return all encoded images list
    return encodeList


# function for marking attendance
def markAttendance(name):
    # we want to read and write simultaneously
    with open('Attendance.csv','r+') as f:
        myAttendanceSheet = f.readlines() # read through line
        nameList = []  # list for cross verifation because we don't want double entry
        # iterate through added names and cross check with current name for avoid double entry
        for line in myAttendanceSheet:
            # split string because our formate is ' NAME, TIME, STATUS '
            entry = line.split(',')
            # WE just want 1st entry which is name
            nameList.append(entry[0])
        # if name is already in list then system will not going to write it in file
        if name not in nameList:
            now = datetime.now()                       # take input of current time
            dtString = now.strftime('%H:%M:%S')        # set format and store it into a string
            f.writelines(f'\n{name},{dtString},Present')   # write name and time in the csv file


encode_List_for_Known_faces = findEncodings(images)   # encode all existing images
print(' Encoding has Completed !!! ')

cap = cv.VideoCapture(0)         # start taking images from web cam
# 0 for default webcam if you have another wecam then use 1

# for continuous image capturing through webcam
while True:
    success, img = cap.read() # read each image
    # img = captureScreen()
    imgS = cv.resize(img, (0, 0), None, 0.25, 0.25) # reduce scale
    imgS = cv.cvtColor(imgS, cv.COLOR_BGR2RGB) # convert image

    # locate face location of current image
    facesCurFrame = face_recognition.face_locations(imgS)
    # encode current image
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    # iterate throught existing face location and encoding list with current image face location and current encoding of image
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encode_List_for_Known_faces, encodeFace)
        faceDis = face_recognition.face_distance(encode_List_for_Known_faces, encodeFace)
        #print(faceDis)

        # returning which image index is matching with current images
        matchesIndex = np.argmin(faceDis)

        # check which image match with existing images
        if matches[matchesIndex]:
            # storing name of matching image with uppercase
            name =  classStudents[matchesIndex].upper()
            #print(name)
            # Getting co-ordinates of matched face for drawing rectangle
            y1, x2, y2, x1 = faceLoc
            # multiply by 4 to each co-ordinate because we reduced scale by 4 initially
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            # Draw rectangle around recognized face
            cv.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            # put name text below the rectangle
            cv.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv.FILLED)
            cv.putText(img,name,(x1+6,y2-6),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
            # call mark attendance function
            markAttendance(name)

    # show webcam
    cv.imshow('webcam', img)
    cv.waitKey(1)





