
import time
import cv2
import numpy as np
import math  # for sqrt
import mechanics

class MotionTracking:
    def __init__(self, cameraFeed):
        self.__cameraFeed = cameraFeed
        self.__mechanics = mechanics
        self.__THRESHOLD = 20
        self.__WIDTH = 432
        self.__HEIGHT = 368
        self.__BLUR = 40
        self.__BLUR_SQUARED = self.__BLUR * self.__BLUR
        self.__VIEW_ANGLE_H = 180
        self.__VIEW_ANGLE_V = 180
        self.__MIN_MOVE_TRIGGER_ANGLE = 75
        self.__STANDBY_AFTER_MOVE_MILLIS = 500
        self.__centerX = self.__WIDTH / 2
        self.__centerY = self.__HEIGHT / 2
        self.__frameCount = 0
        self.__blackImage = np.zeros((self.__HEIGHT, self.__WIDTH, 3), np.uint8)

        self.__phase0Prev = cameraFeed.getFrame()
        self.__phase1Prev = self.__blackAndWhite(self.__phase0Prev)
        self.__moveRestrictionStart = time.time()
        self.__mechanics.moveToMiddle()


    def getFinal(self):
        self.__phase0 = self.__cameraFeed.getFrame()
        self.__phase1 = self.__blackAndWhite(self.__phase1)
        self.__finalImg = self.__phase0.copy()

        self.__phase0Prev = self.__phase0
        self.__phase1Prev = self.__phase1

        self.__phase2 = self.__diff(self.__phase1, self.__phase1Prev)
        self.__phase3 = self.__binarizeOtsu(self.phase2)

        if self.__phase3 is None:
            self.__phase3 = self.__blackImage
            self.__phase4 = self.__blackImage
            self.__phase5 = self.__blackImage
        else:
            self.__phase4 = self.__blur(self.__phase3)
            self.__phase5 = self.__binarizeSimple(self.__phase4)

            if self.__frameCount > 3 and not self.__isMoveForbidden():
                closest = self.__pointOutMovingSpots(self.__phase5, self.__finalImg)
                self.__mechanicsProceed(closest)

        self.__frameCount += 1

    def __blackAndWhite(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def __diff(self, image1, image2):
        return cv2.absdiff(image1, image2)

    def __binarizeOtsu(self, image):
        resultTuple = cv2.threshold(image, 128, 255, cv2.THRESH_OTSU)
        threshValue = resultTuple[0]
        if threshValue > self.__THRESHOLD:
            return resultTuple[1]
        return None

    def __blur(self, image):
        kernel = np.ones((self.__BLUR, self.__BLUR), np.float32) / (self.__BLUR_SQUARED)
        return cv2.filter2D(image, -1, kernel)

    def __binarizeSimple(self, image):
        return cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)[1]

    def __isMoveForbidden(self):
        return not time.time() - self.__moveRestrictionStart > self.__STANDBY_AFTER_MOVE_MILLIS / 1000.0


    def __getClosestToCenter(self, centroids):
        minDistance = float("inf")
        closestCentroid = None

        for i in range(len(centroids)):
            pointX = centroids[i][0]
            pointY = centroids[i][1]
            distance = (self.__centerX - pointX) * \
                       (self.__centerX - pointX) + \
                       (self.__centerY - pointY) * \
                       (self.__centerY - pointY)
            distance = math.sqrt(distance)

            if distance < minDistance:
                closestCentroid = i
                minDistance = distance

        return closestCentroid


    def __pointOutMovingSpots(self, image, originalImage):
        connectivity = 8
        output = cv2.connectedComponentsWithStats(image, connectivity, cv2.CV_32S)

        # center coordinates of regions
        centroids = output[3][1:]
        closest = self.__getClosestToCenter(centroids)

        for i in range(len(centroids)):
            font = cv2.FONT_HERSHEY_SIMPLEX
            xCoordinate = centroids[i][0]
            yCoordinate = centroids[i][1]
            coordinates = ((int)(xCoordinate) - 15, (int)(yCoordinate) + 10)
            fontScale = 1

            fontColor = (0, 255, 255)
            if i == closest:
                fontColor = (255, 0, 0)
            lineType = 2

            cv2.putText(originalImage, '+',
                        coordinates,
                        font,
                        fontScale,
                        fontColor,
                        lineType)

        return centroids[closest]

    def __mechanicsProceed(self, closest):
        horizontalDiff = self.__centerX - closest[0]  # in pixels
        verticalDiff = self.__centerY - closest[1]

        horizontalAngleDiff = horizontalDiff * self.__VIEW_ANGLE_H / self.__WIDTH
        verticalAngleDiff = verticalDiff * self.__VIEW_ANGLE_V / self.__HEIGHT

        if abs(horizontalDiff) >= self.__MIN_MOVE_TRIGGER_ANGLE:
            if horizontalDiff > 0:
                mechanics.move("LEFT", horizontalAngleDiff)
            else:
                mechanics.move("RIGHT", -horizontalAngleDiff)
            self.__moveRestrictionStart = time.time()
        if abs(verticalDiff) >= self.__MIN_MOVE_TRIGGER_ANGLE:
            if verticalDiff > 0:
                mechanics.move("UP", verticalAngleDiff)
            else:
                mechanics.move("DOWN", -verticalAngleDiff)
                self.__moveRestrictionStart = time.time()
