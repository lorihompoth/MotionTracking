import sys 

if len(sys.argv) != 2:
    print("Usage: main.py [01] [01]")
    exit(0)
elif sys.argv[1] == "0":
    from view.Gui import Gui
    print("Gui started")
    with Gui() as g:
        pass
    print("gui terminated")
elif sys.argv[2] == "1":
    from motionTracking.MotionTracking import MotionTracking
    from cameraFeed.Camera import Camera
    from cameraFeed.CameraFeed import CameraFeed
    import cv2
    import time
    import socket
    
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('localhost', 8089))
    serversocket.listen(1)
    
    connection, address = serversocket.accept()
    buf = connection.recv(4096)
    if len(buf) > 0:
        print buf
    serversocket.close()

    #ast.literal_eval("{'1': 2}")

    WIDTH = 432
    HEIGHT = 368
    FRAMERATE = 20l
    ROTATION = 180
    camFeed = CameraFeed(WIDTH, HEIGHT, ROTATION, FRAMERATE)
    #print(self.__destinationFolder[7:])
    mt = MotionTracking(camFeed, None)
    t = time.time()
    while True:
        image = mt.getFinal()
        if image is not None:
            #cv2.imshow("asd", image)
            fps = 1/(time.time() - t)
            print("fps: " + str(int(fps)))


