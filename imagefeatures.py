#coding: latin-1

# OpenCV basic code.
# Saving/Storing keypoints https://isotope11.com/blog/storing-surf-sift-orb-keypoints-using-opencv-in-python
#
#

import cv2
import numpy as np

import pickle

def pickle_keypoints(keypoints, descriptors):
    i = 0
    temp_array = []
    for point in keypoints:
        temp = (point.pt, point.size, point.angle, point.response, point.octave,
        point.class_id, descriptors[i])     
        i+=1
        temp_array.append(temp)
    return temp_array

def unpickle_keypoints(array):
    keypoints = []
    descriptors = []
    for point in array:
        temp_feature = cv2.KeyPoint(x=point[0][0],y=point[0][1],_size=point[1], _angle=point[2], _response=point[3], _octave=point[4], _class_id=point[5])
        temp_descriptor = point[6]
        keypoints.append(temp_feature)
        descriptors.append(temp_descriptor)
    return keypoints, np.array(descriptors)

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('/Users/rramele/Documents/AppleStore.Subiendo.I.mov')
#cap = cv2.VideoCapture('tcp://192.168.1.1:5555')
#cap = cv2.VideoCapture('tcp://192.168.0.3/cgi-bin/fwstream.cgi?FwModId=0&PortId=1&PauseTime=0&FwCgiVer=0x0001')
#cap = cv2.VideoCapture('rtsp://192.168.0.3/cam0_0')
#cap = cv2.VideoCapture('tcp://192.168.0.110:10000')

print ("Connecting..")

for i in range(1,10):
   # Capture frame-by-frame
   ret, frame = cap.read()

   #frame = cv2.flip(frame,0)
   ##frame = cv2.flip(frame,1)

   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   #cv2.imwrite('01.png', gray)

   #gray = frame;

   #Using AKAZE descriptors.
   detector = cv2.AKAZE_create()
   (kps, descs) = detector.detectAndCompute(gray, None)
   print("keypoints: {}, descriptors: {}".format(len(kps), descs.shape))


   # draw the keypoints and show the output image
   cv2.drawKeypoints(frame, kps, frame, (0, 255, 0))

   cv2.imshow("Computer Eye", frame)


   if cv2.waitKey(1) & 0xFF == ord('q'):
      break


temp_array = []

for i in range(1,2):
   # Capture frame-by-frame
   ret, frame = cap.read()

   ##frame = cv2.flip(frame,0)
   ##frame = cv2.flip(frame,1)

   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   #cv2.imwrite('01.png', gray)

   #gray = frame;

   #Using AKAZE descriptors.
   detector = cv2.AKAZE_create()
   (kps, descs) = detector.detectAndCompute(gray, None)
   print("keypoints: {}, descriptors: {}".format(len(kps), descs.shape))

   #Store and Retrieve keypoint features
   temp = pickle_keypoints(kps, descs)
   temp_array.append(temp)

   # draw the keypoints and show the output image
   cv2.drawKeypoints(frame, kps, frame, (0, 255, 0))

   cv2.imshow("Computer Eye", frame)


   if cv2.waitKey(1) & 0xFF == ord('q'):
      break

print ('Done.')
pickle.dump(temp_array, open("data/kd1.p", "wb"))

#When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


