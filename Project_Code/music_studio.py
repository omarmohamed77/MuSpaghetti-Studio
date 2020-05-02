import cv2
import threading
import imutils
from source import globals
from source.color_tracking import *
from source.recognize import *


def studio_main():
    # initialize global variables
    globals.initialize()
    # get the reference to the webcam
    camera=cv2.VideoCapture(0)
    # start a named window with FULLSCREEN size
    window_name = "music_studio"
    #cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    # run main functions
    directory = ""  # set directory variable to the current path of the project 
    music_data = [[directory+'sound_tracks/snare.wav', directory+'images/drum_1.jpg', 2],
                  [directory+'sound_tracks/hi_hat.wav', directory+'images/drum_2.jpg', 1],
                  [directory+'sound_tracks/O-Hi-Hat.wav', directory+'images/drum_3.jpg', 0],
                  [directory+'sound_tracks/output.wav', directory+'images/drum_4.jpg', 0]]
    filename = "records/output.wav"
    background_music = directory + "sound_tracks/ana_gad3.mp3"
    sign_processing = sign_main(filename, background_music)
    music_processing = music_main(music_data)
    while(camera.isOpened()):
        # get the current frame
        (grabbed, globals.main_frame) = camera.read()
        # resize the frame
        globals.main_frame = imutils.resize(globals.main_frame, width=700)
        # flip the frame so that it is not the mirror view
        globals.main_frame = cv2.flip(globals.main_frame, 1)
        # creating threads 
        t1 = threading.Thread(target=sign_processing, args=(globals.main_frame.copy(),)) 
        t2 = threading.Thread(target=music_processing, args=(globals.main_frame.copy(),))   
        # starting threads 
        t1.start() 
        t2.start()
        # wait until all threads finish 
        t1.join() 
        t2.join() 
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


if __name__=='__main__':
    studio_main()
    