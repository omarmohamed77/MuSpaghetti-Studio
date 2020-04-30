#importing modules
import cv2
import imutils
import numpy as np
import math
import time
import _thread
import wave
import struct
import simpleaudio as sa
import globals


def music_main():
    music_main.drum = cv2.imread('images/drum.jpg')
    music_main.wave_obj={}
    music_main.wave_obj['snare.wav'] = sa.WaveObject.from_wave_file('sound_tracks/snare.wav')
    music_main.wave_obj['hi_hat.wav'] = sa.WaveObject.from_wave_file('sound_tracks/hi_hat.wav')
    music_main.wave_obj['O-Hi-Hat.wav'] = sa.WaveObject.from_wave_file('sound_tracks/O-Hi-Hat.wav')
    music_main.wave_obj['output.wav'] = sa.WaveObject.from_wave_file('sound_tracks/output.wav')

    music_main.frameCount = 0
    music_main.timeStart = time.time()
    music_main.b1 = (0,0)
    music_main.b2 = (0,0)
    music_main.currentBlueVelocity = 0
    music_main.r1 = (0,0)
    music_main.r2 = (0,0)
    music_main.currentRedVelocity = 0
    
    music_main.booli  = [False for i in range(4)]
    music_main.numDrums = 0
    music_main.drums = [None for i in range(4)]
    
    def playSound(name):
        play_obj = music_main.wave_obj[name].play()


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
        
        blank = np.zeros(music_processing.img.shape[0:2])
        ellipseImage = cv2.ellipse(blank, ellipse, (255, 255, 255), -2)
    
        M = cv2.moments(c)
        if M["m00"] == 0:
            return
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        
        globals.write_lock.acquire()
        cv2.ellipse(globals.main_frame, ellipse, (0,0,0), 2)
        if radius > 10 and radius<100:
            # draw the ellipse and centroid on the frame,
            # then update the list of tracked points
            # cv2.circle(img, (int(x), int(y)), int(radius),(0, 0, 0), 2)
            cv2.circle(globals.main_frame, center, 3, (0, 0, 255), -1)
            cv2.putText(globals.main_frame,text, (center[0]+10,center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0, 0, 0),2)
            cv2.putText(globals.main_frame,"("+str(center[0])+","+str(center[1])+")", (center[0]+10,center[1]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0, 0, 0),1)
        globals.write_lock.release()

        return (center, ellipseImage)

    def detectCollision(imgA, imgB, velocity, touching, name):
        mA = cv2.moments(imgA, False)
        mB = cv2.moments(imgB, False)
        blank = np.zeros(music_processing.img.shape[0:2])
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

    def newDrum_picture(pos, name , drum):
        #cv2.imshow("Resized image", resized)
        alpha =0.2
        width = 100
        height = 100 
        dim = (width, height)
        resized = cv2.resize(drum, dim, interpolation = cv2.INTER_AREA)
        h,w,c = resized.shape
        sub=(width/2,height/2)
        start = tuple(map(lambda i, j:int (i - j), pos, sub))
        end = tuple(map(lambda i, j:int (i + j), pos, sub))
        blank = np.zeros(music_processing.img.shape[0:2])
        drum_image = cv2.rectangle(blank.copy(), start, end, (255,255,255), -5) 
        x,y = start
        globals.write_lock.acquire()
        test = globals.main_frame
        added_image = cv2.addWeighted(test[y:y+h, x:x+w,:],alpha,resized,1-alpha,0)
        test[y:y+h, x:x+w] = added_image
        globals.write_lock.release()
        music_main.numDrums += 1
        return (name, drum_image)
        
    def music_processing(img):
        now = time.time()
        fps = music_main.frameCount / (now - music_main.timeStart)
        music_main.frameCount += 1
        
        music_processing.img = img
        
        globals.write_lock.acquire()
        cv2.putText(globals.main_frame,"FPS: %.2f" % (fps),(10,220),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)
        globals.write_lock.release()
        
        #converting frame(img i.e BGR) to HSV (hue-saturation-value)
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

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

        music_main.b1 = music_main.b2
        music_main.b2 = blueCenter
        bDelta = math.sqrt((music_main.b2[0] - music_main.b1[0])**2 + (music_main.b2[1] - music_main.b1[1])**2)
        bVelocity = bDelta * fps / 100
        globals.write_lock.acquire()
        if (bVelocity - music_main.currentBlueVelocity) > 10:
            cv2.putText(globals.main_frame,str(int(bVelocity)),(10, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
        else:
            cv2.putText(globals.main_frame,str(int(music_main.currentBlueVelocity)),(10, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
        globals.write_lock.release()
        music_main.currentBlueVelocity = bVelocity

        music_main.r1 = music_main.r2
        music_main.r2 = redCenter
        rDelta = math.sqrt((music_main.r2[0] - music_main.r1[0])**2 + (music_main.r2[1] - music_main.r1[1])**2)
        rVelocity = rDelta * fps / 100
        globals.write_lock.acquire()
        if (rVelocity - music_main.currentRedVelocity) > 10:
            cv2.putText(globals.main_frame,str(int(rVelocity)),(70, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
        else:
            cv2.putText(globals.main_frame,str(int(music_main.currentRedVelocity)),(70, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
        globals.write_lock.release()
        music_main.currentRedVelocity = rVelocity
        
        #Add the drums
        music_main.drums[0] = newDrum_picture((450, 400), "snare" , music_main.drum )
        music_main.drums[1] = newDrum_picture((100, 400), "hi_hat",  music_main.drum )
        music_main.drums[2] = newDrum_picture((450, 130), "O-Hi-Hat", music_main.drum )
        music_main.drums[3] = newDrum_picture((100, 130), "output", music_main.drum )

        for i in range(len(music_main.drums)):
            music_main.booli[i] = detectCollision(blueEllipse, music_main.drums[i][1], music_main.currentBlueVelocity, music_main.booli[i], "{0}.wav".format(music_main.drums[i][0]))
            music_main.booli[i] = detectCollision(redEllipse, music_main.drums[i][1], music_main.currentRedVelocity, music_main.booli[i], "{0}.wav".format(music_main.drums[i][0]))
 
    return music_processing
    
    
if __name__ == "__main__":
    # initialize global variables
    globals.initialize()
    # get the reference to the webcam
    camera=cv2.VideoCapture(0)
    # start a named window with cnotrollable size
    window_name = "music_studio"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    # run main function
    music_processing = music_main()
    while(camera.isOpened()):
        # get the current frame
        (grabbed, globals.main_frame) = camera.read()
        # resize the frame
        globals.main_frame = imutils.resize(globals.main_frame, width=700)
        # flip the frame so that it is not the mirror view
        globals.main_frame = cv2.flip(globals.main_frame, 1)
        # start sign processing
        music_processing(globals.main_frame.copy())
        # display the global frame after processing
        cv2.imshow(window_name, globals.main_frame)
        # observe the keypress by the user
        keypress = cv2.waitKey(1) & 0xFF
        # if the user pressed "q", then stop looping
        if keypress == ord("q"):
            break    
    # free up memory
    camera.release()
    cv2.destroyAllWindows()
    