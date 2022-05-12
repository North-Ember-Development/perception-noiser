import types, threading, time
from tools import create_thread_method
import logging
from pynput.keyboard import Key, Listener

logging.basicConfig(filename="log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

KeyLoggingEventStarted = False

class Hotkeys(threading.Thread):

    def __init__(self):
        pass

    def run(self):
        pass

PressedKeys_Status = []
______Hotkeys_Data = []

def check_callback_is_pressed():
    for hotkeyd in ______Hotkeys_Data:
        for k1, k2 in zip(hotkeyd['keys'], PressedKeys_Status):
            if k1 != k2:
                return

        if len(PressedKeys_Status) != len(hotkeyd['keys']):
            return

        logging.info(f"Hotkey {'+'.join(hotkeyd['keys'])} pressed.")

        return hotkeyd['callb']()

def clear_prefix(key):
    key = str(key)
    if (key).startswith("Key."):
        key = (key)[4:]
    return key.lower().strip("'")

KeyloggingListener = None
KeyLoggingEventStarted = False
KeyloggingPassThreadData = None

from Classes.Thread import Thread as _Thread

def start_keylogging_events():
    global KeyLoggingEventStarted
    if KeyLoggingEventStarted is True:
        return
    KeyLoggingEventStarted = True

    def on_press(key):  # The function that's called when a key is pressed
        key = clear_prefix(key)
        if key in PressedKeys_Status:
            return
        PressedKeys_Status.append(key)

        check_callback_is_pressed()

    def on_release(key):  # The function that's called when a key is released
        key = clear_prefix(key)
        if key in PressedKeys_Status:
            del PressedKeys_Status[PressedKeys_Status.index(key)]

    def start_listener(*args, **kwargs):
        global KeyloggingListener
        with Listener(on_press=on_press, on_release=on_release) as listener:  # Create an instance of Listener
            KeyloggingListener = listener
            listener.join()
            listener.wait()

    global KeyloggingPassThreadData
    KeyloggingPassThreadData = _Thread(start_listener).start()

def bind_hotkey_function(short_cuts : str, callback : types.FunctionType):

    start_keylogging_events()

    data_i = {'keys' : short_cuts.lower().split('+'), 'callb' : callback}

    ______Hotkeys_Data.append(data_i)

def stop_hotkeys_listener():
    print("Exiting hotkeys listener.", KeyloggingListener)
    logging.info("Stopping hotkeys handler.")
    KeyloggingListener.stop()
    KeyloggingPassThreadData.stop()

if __name__ == "__main__":

    bind_hotkey_function("Ctrl+M", stop_hotkeys_listener)