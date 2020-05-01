from threading import Lock

def initialize():
    global main_frame
    global write_lock
    main_frame = None
    write_lock = Lock()