from motionTracking.MotionTracking import MotionTracking
from cameraFeed.Camera import Camera
from cameraFeed.CameraFeed import CameraFeed
from motionTracking.RecordVideo import RecordVideo
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
    serversocket.close()
    
    return ast.literal_eval(buf)

def imageToDisplay(configurables, mt):
    images = {}
    finalImage = mt.getFinal()
    if not configurables["preview"]:
        return images
    if configurables["finalScreen"]:
        images["Final Screen"] = finalImage
    if configurables["phase1"]:
        images["Phase 1"] = mt.getPhase1()
    if configurables["phase2"]:
        images["Phase 2"] = mt.getPhase2()
    if configurables["phase3"]:
        images["Phase 3"] = mt.getPhase3()
    if configurables["phase4"]:
        images["Phase 4"] = mt.getPhase4()
    if configurables["phase5"]:
        images["Phase 5"] = mt.getPhase5()
    return images
        
def getVideoRecorder(configurables):
    videoRecorder = RecordVideo()
    videoRecorder.setDestinationFolder(configurables["destinationFolder"])
    videoRecorder.setPutTimecode(configurables["putTimecode"])    
    videoRecorder.setFontScale(configurables["fontScale"])
    videoRecorder.setRecordMovementOnly(configurables["recordMovementOnly"])
    videoRecorder.setSeparateFiles(configurables["separateFiles"])
    return videoRecorder

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
recorder = getVideoRecorder(configurables)
recorder.setResolution(WIDTH, HEIGHT)
mt.setVideoRecorder(recorder)

t = time.time()
while True:
    images = imageToDisplay(configurables, mt)
    for name in images.keys():
        cv2.imshow(name, images[name])
        fps = 1/(time.time() - t)
        print("fps: " + str(int(fps)))
        t = time.time()
    cv2.waitKey(1)


