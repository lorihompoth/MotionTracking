from motionTracking.MotionTracking import MotionTracking
from cameraFeed.Camera import Camera
from cameraFeed.CameraFeed import CameraFeed
import cv2
import time
import socket
import ast


def receiveConfigurables():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('localhost', 8089))
    serversocket.listen(1)
    connection, address = serversocket.accept()
    buf = connection.recv(4096)
    time.sleep(1)
    serversocket.close()
    
    return ast.literal_eval(buf)


configurables = receiveConfigurables()

resolution = configurables["resolution"].split()
WIDTH = int(resolution[0])
HEIGHT = int(resolution[2])
camFeed = CameraFeed()
camFeed.setResolution(WIDTH, HEIGHT)
camFeed.setRotation(180)
mt = MotionTracking(camFeed)
mt.setResolution(WIDTH, HEIGHT)
mt.setAimTowardsMotion(configurables["aimTowardsMotion"])
mt.setAimWithArrowKeys(configurables["aimWithArrowKeys"])
mt.setBlur(configurables["blur"])
mt.setThreshold(configurables["threshold"])
mt.setStandbyBetweenMovements(configurables["standbyBetweenMovements"])
mt.setCameraFieldOfView(configurables["cameraFieldOfView"])
mt.setMinTrigger(configurables["minTrigger"])


t = time.time()
while True:
    #input("type a number: ")
    image = mt.getFinal()
    if image is not None:
        cv2.imshow("asd", image)
        cv2.waitKey(1)
        fps = 1/(time.time() - t)
        #print("fps: " + str(int(fps)))


