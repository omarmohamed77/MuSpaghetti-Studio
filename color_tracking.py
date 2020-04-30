#importing modules
import cv2
import numpy as np
import math
import time
import _thread
import wave
import struct
import simpleaudio as sa
def playSound(name):
    global wave_obj
    play_obj = wave_obj[name].play()


    ####CRASHES ON FAST INPUT####
    # import pyglet
    # player = pyglet.media.Player()
    # src = pyglet.media.load(name)
    # player.volume = 0.1
    # player.queue(src)
    # player.play()

    #####VERY SLOW####
    # import pygame.mixer
    # pm = pygame.mixer
    # pm.init()
    # sound = pm.Sound(name)
    # sound.set_volume(0.5)
    # sound.play()



def drawEllipse(contours, text):
    if(contours == None or len(contours) == 0):
        return ((-100,-100), None)
    c = max(contours, key=cv2.contourArea)
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    if(cv2.contourArea(c) < 500):
        return ((-100,-100), None)
    ellipse = cv2.fitEllipse(c)
    cv2.ellipse(img, ellipse, (0,0,0), 2)

    blank = np.zeros(img.shape[0:2])
    ellipseImage = cv2.ellipse(blank, ellipse, (255, 255, 255), -2)
    # cv2.imshow("ell",ellipseImage)

    M = cv2.moments(c)
    if M["m00"] == 0:
        return
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

    if radius > 10 and radius<100:
        # draw the ellipse and centroid on the frame,
        # then update the list of tracked points
        # cv2.circle(img, (int(x), int(y)), int(radius),(0, 0, 0), 2)
        cv2.circle(img, center, 3, (0, 0, 255), -1)
        cv2.putText(img,text, (center[0]+10,center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0, 0, 0),2)
        cv2.putText(img,"("+str(center[0])+","+str(center[1])+")", (center[0]+10,center[1]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0, 0, 0),1)

    return (center, ellipseImage)

def detectCollision(imgA, imgB, velocity, touching, name):
    mA = cv2.moments(imgA, False)
    mB = cv2.moments(imgB, False)
    blank = np.zeros(img.shape[0:2])
    if type(imgA) == type(None) or type(imgB) == type(None):
        return
    intersection = cv2.bitwise_and(imgA, imgB)
    area = cv2.countNonZero(intersection)
    if area < 20:
        touching = False
    if area > 100 and not touching:
        # print(int(mA["m01"] / mA["m00"])< int(mB["m01"] / mB["m00"]))
        # print(area)
        if int(mA["m01"] / mA["m00"])< int(mB["m01"] / mB["m00"]):
            if velocity > 10:
                _thread.start_new_thread(playSound, (name,))
                # playSound(name)
        touching = True
    return touching

def newDrum(pos, name):
    # pos = (x, y)
    drum = cv2.circle(img,pos, 50,(0,0, 0),1)
    sub=(25,0)
    res = tuple(map(lambda i, j:int (i - j), pos, sub)) 
    #cv2.putText(drum,name,res,cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
    blank = np.zeros(img.shape[0:2])
    drum_image = cv2.circle(blank.copy(), pos, 50, (255, 255, 255), -5)
    global numDrums
    numDrums += 1
    return (name, drum_image)

def newDrum_picture(pos, name):
    #cv2.imshow("Resized image", resized)
    global resized
    h,w,c = resized.shape
    sub=(width/2,height/2)
    start = tuple(map(lambda i, j:int (i - j), pos, sub))
    end = tuple(map(lambda i, j:int (i + j), pos, sub))
    blank = np.zeros(img.shape[0:2])
    drum_image = cv2.rectangle(blank.copy(), start, end, (255,255,255), -5) 
    #if p==40:
    #    cv2.imshow('drum',drum_image)
    x,y = start
    test = img
    added_image = cv2.addWeighted(test[y:y+h, x:x+w,:],alpha,resized,1-alpha,0)
    test[y:y+h, x:x+w] = added_image
    global numDrums
    numDrums += 1
    return (name, drum_image)
    #cv2.imshow("test", test)


drum = cv2.imread('drum.jpg')
#cv2.imshow('yarab',drum)
alpha =0.2
width = 100
height = 100 
dim = (width, height)
# resize image
resized = cv2.resize(drum, dim, interpolation = cv2.INTER_AREA)
p=0
wave_obj={}
wave_obj['snare.wav'] = sa.WaveObject.from_wave_file('snare.wav')
wave_obj['hi_hat.wav'] = sa.WaveObject.from_wave_file('hi_hat.wav')
wave_obj['O-Hi-Hat.wav'] = sa.WaveObject.from_wave_file('O-Hi-Hat.wav')
    #capturing video through webcam


cap=cv2.VideoCapture(0)
frameCount = 0
timeStart = time.time()
b1 = (0,0)
b2 = (0,0)
currentBlueVelocity = 0
r1 = (0,0)
r2 = (0,0)
currentRedVelocity = 0
blueAndSnare = False
blueAndHiHat = False
redAndSnare = False
redAndHiHat = False
booli  = [False for i in range(4)]
numDrums = 0
drums = [None for i in range(4)]

while(1):
    now = time.time()
    fps = frameCount / (now - timeStart)
    frameCount += 1

    _, img = cap.read()
    img = cv2.flip(img, 1)
    #if p==40:
    #       cv2.imshow('ima',img)
    # cv2.putText(img,"FPS : ",(10,100),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2)
    cv2.putText(img,"FPS: %.2f" % (fps),(10,200),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2)

    # Add the drums
    #drums[0] = newDrum((450, 400), "snare")
    #drums[1] = newDrum((100, 400), "hi_hat")
    #drums[2] = newDrum((450, 110), "O-Hi-Hat")
    #drums[3] = newDrum((100, 110), "hi_hat")
    
    #converting frame(img i.e BGR) to HSV (hue-saturation-value)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    #if p==40:
    #    cv2.imshow('im',img)
    #    cv2.imwrite('omar'+str(p)+'.png', img)
    p+=1
    ###############################
    #test
    red_lower=np.array([ 0, 222 , 55] ,np.uint8)
    red_upper=np.array([ 12 , 251 , 140],np.uint8)
    blue_lower=np.array([105, 186 , 85],np.uint8)
    blue_upper=np.array([125 ,206 ,165],np.uint8)
    ###############################

    #finding the range of red,blue color in the image
    red1=cv2.inRange(hsv, red_lower, red_upper)
    blue=cv2.inRange(hsv,blue_lower,blue_upper)
    red_lower=np.array([ 169 , 222 , 55] ,np.uint8)
    red_upper=np.array([ 189 , 251 , 130],np.uint8)
    red2=cv2.inRange(hsv, red_lower, red_upper)
    red = red1 + red2
    #Morphological transformation, Dilation
    kernal = np.ones((5 ,5), "uint8")

    red=cv2.dilate(red, kernal)
    res=cv2.bitwise_and(img, img, mask = red)

    blue=cv2.dilate(blue,kernal)
    res1=cv2.bitwise_and(img, img, mask = blue)


    #Tracking the Red Color
    (contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    (redCenter, redEllipse) = drawEllipse(contours, "Red")
    # cv2.drawContours(img, contours, -1 , (0,0,255), 2)


    #Tracking the Blue Color
    (contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(img, contours, -1 , (255,0,0), 2)
    (blueCenter, blueEllipse) = drawEllipse(contours, "Blue")

    b1 = b2
    b2 = blueCenter
    bDelta = math.sqrt((b2[0] - b1[0])**2 + (b2[1] - b1[1])**2)
    bVelocity = bDelta * fps / 100
    if (bVelocity - currentBlueVelocity) > 10:
        cv2.putText(img,str(int(bVelocity)),(10, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
    else:
        cv2.putText(img,str(int(currentBlueVelocity)),(10, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
    currentBlueVelocity = bVelocity

    r1 = r2
    r2 = redCenter
    rDelta = math.sqrt((r2[0] - r1[0])**2 + (r2[1] - r1[1])**2)
    rVelocity = rDelta * fps / 100
    if (rVelocity - currentRedVelocity) > 10:
        cv2.putText(img,str(int(rVelocity)),(70, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
    else:
        cv2.putText(img,str(int(currentRedVelocity)),(70, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
    currentRedVelocity = rVelocity

    drums[0] = newDrum_picture((450, 400), "snare")
    drums[1] = newDrum_picture((100, 400), "hi_hat")
    drums[2] = newDrum_picture((450, 110), "O-Hi-Hat")
    drums[3] = newDrum_picture((100, 110), "hi_hat")

    for i in range(len(drums)):
        # print(booli)
        #if p==40:
        #    cv2.imshow('imag',blueEllipse)
        booli[i] = detectCollision(blueEllipse, drums[i][1], currentBlueVelocity, booli[i], "{0}.wav".format(drums[i][0]))
        booli[i] = detectCollision(redEllipse, drums[i][1], currentRedVelocity, booli[i], "{0}.wav".format(drums[i][0]))
    # blueAndSnare = detectCollision(blueEllipse, drums[0][1], blueAndSnare, "snare.wav")
    # blueAndHiHat = detectCollision(blueEllipse, drums[1][1], blueAndHiHat, "hi_hat.wav")

    # blueAndSnare = detectCollision(blueEllipse, snare_image, blueAndSnare, "snare.wav")
    # blueAndHiHat = detectCollision(blueEllipse, hi_hat_image, blueAndHiHat, "Closed-Hi-Hat.wav")
    #
    # redAndSnare = detectCollision(redEllipse, snare_image, redAndSnare, "snare.wav")
    # redAndHiHat = detectCollision(redEllipse, hi_hat_image, redAndHiHat, "Closed-Hi-Hat.wav")



    #cv2.imshow("Redcolour",red)
    cv2.imshow("Color Tracking",img)
    #cv2.imshow("red",res)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

