import pydirectinput
import threading
import time
import keyboard
import tkinter as tk
import traceback

pydirectinput.PAUSE = 0
keys = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','q','r','s','t','u','v','w','x','y','z',
    '0','1','2','3','4','5','6','7','8','9','-','=','[',']',
    ';',"'",',','.','/','`','\\',' ','~','!','@','#','$','%',
    '^','&','*','(',')','_','+','{','}','|',':','"','<','>',
    '?','é','è','ç','à','ù','²','µ','¨','£','§'
]

Interval = 0.01
per_key_hold = 0.02
toggle_key = 'p'
running = False
lock = threading.Lock()

def key_worker(key):
    global running
    try:
        while True:
            with lock:
                is_running = running

            if is_running:
                try:
                    pydirectinput.keyDown(key)
                    time.sleep(per_key_hold)
                    pydirectinput.keyUp(key)
                except Exception as e:
                    print(f"[{key}] Error: {e}")

            time.sleep(Interval)
    except Exception:
        print(f"[{key}] Thread Crashed:")
        traceback.print_exc()

debounce_seconds = 0.5
_last_toggle_time = 0.0

def handle_toggle_key(event):
    global running, _last_toggle_time
    now = time.time()
    if now - _last_toggle_time < debounce_seconds:
        return
    with lock:
        running = not running
        state = running
    _last_toggle_time = now
    print("Running" if state else "Stopped")

keyboard.on_press_key(toggle_key, handle_toggle_key)

def exit_on_esc():
    keyboard.wait('esc')
    print("\nClosing Program...")
    try:
        root.destroy()
    except:
        pass
    try:
        root.quit()
    except:
        pass

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    for key in keys:
        threading.Thread(target=key_worker, args=(key,), daemon=True).start()
    threading.Thread(target=exit_on_esc, daemon=True).start()
    print("Press \"p\" to Start/Stop. Press \"ESC\" to close.")
    root.mainloop()