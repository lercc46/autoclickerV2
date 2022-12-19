import time
import threading
import customtkinter as ctk
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode


run = True
clicking = False

# thread for actual clicker
def autoclicker():

    mouse = Controller()

    def clicker():

        global clicking
        global speed_entry

        speed = speed_entry.get()
        speed = 1 / int(speed)

        while True:
            if clicking:
                mouse.click(Button.left, 1)
            time.sleep(speed)

    def toggle_event(key):

        global run
        global clicking
        global toggle_entry
        global quit_entry

        if run:
            toggle = toggle_entry.get()
            quit = quit_entry.get()

            toggle_key = KeyCode(char=toggle)
            quit_key = KeyCode(char=quit)

            if key == toggle_key:
                clicking = not clicking
            elif key == quit_key:
                run = False

    threading.Thread(target=clicker).start()

    with Listener(on_press=toggle_event) as listener:
        listener.join()

autoclicker_thread = threading.Thread(target=autoclicker, daemon=True)

def start():
    global run
    run = True

    if not autoclicker_thread.is_alive():
        autoclicker_thread.start()

def reset():
    global run
    run = False

    toggle_entry.delete(0, 'end')
    quit_entry.delete(0, 'end')
    speed_entry.delete(0, 'end')


# customtkinter GUI
WIDTH = 500
HEIGHT = 350

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry(f"{WIDTH}x{HEIGHT}")

frame = ctk.CTkFrame(master=root)
frame.pack(padx=60, pady=20, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Luke's Autoclicker", font=("Roboto", 12))
label.pack(padx=10, pady=12)

toggle_entry = ctk.CTkEntry(master=frame, placeholder_text="toggle key")
toggle_entry.pack(padx=10, pady=12)

quit_entry = ctk.CTkEntry(master=frame, placeholder_text="quit key")
quit_entry.pack(padx=10, pady=12)

speed_entry = ctk.CTkEntry(master=frame, placeholder_text="speed (CPS)")
speed_entry.pack(padx=10, pady=12)

run_button = ctk.CTkButton(master=frame, text="Run", command=start)
run_button.pack(padx=20, pady=12)

reset_button = ctk.CTkButton(master=frame, text="Reset", command=reset)
reset_button.pack(padx=20, pady=12)

root.mainloop()