import cv2
import threading
import imutils
import pygame
from source import globals
from source.recognize import sign_main
from source.color_tracking import music_main


def studio_main(music_data, background_music, device_name, filename):
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
    sign_processing = sign_main(filename, device_name, background_music)
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
            pygame.mixer.quit()
            if sign_main.flag:
                sign_main.canceled=True
                sign_main.flag=False
                sign_processing.recording_thread.join()
            break    
    # free up memory
    camera.release()
    cv2.destroyAllWindows()
    # return record canceled save flag
    return sign_main.recorded


if __name__=='__main__':
    music_data = [['sound_tracks/snare.wav', 'images/drum_1.jpg', 1],
                  ['sound_tracks/hi_hat.wav', 'images/drum_2.jpg', 2],
                  ['sound_tracks/O-Hi-Hat.wav', 'images/drum_3.jpg', 0],
                  ['sound_tracks/output.wav', 'images/drum_4.jpg', 0]]
    background_music = "sound_tracks/ana_gad3.wav"
    filename = "records/output.wav"
    device_name = "Stereo Mix (Realtek(R) Audio)"
    studio_main(music_data, background_music, device_name, filename)
    