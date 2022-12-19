import customtkinter as ctk


run = True
configuring=True

def toggle_configuring():
    global configuring
    configuring = not configuring

def start():
    global run
    run = True

    toggle_configuring()

def reset():
    global run
    run = False

    toggle_configuring()

    toggle_entry.delete(0, 'end')
    quit_entry.delete(0, 'end')
    speed_entry.delete(0, 'end')


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("500x350")

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