import tkinter as tk
import subprocess
import os
from PIL import Image, ImageTk

# Remote constants
AMPLIFIER = "SONY_RM-AAU014"
#TV = "Samsung_BN59-00507A"
TV = "SAMSUNG-C750"
FIREPLACE = "tivo"

def send_ir(remote, command):
    subprocess.run(["irsend", "SEND_ONCE", remote, command])

def system_power():
    send_ir(TV, "KEY_POWER")
    send_ir(AMPLIFIER, "BTN_POWER")

def exit_app(event=None):
    root.quit()

def power_tv():
    send_ir(TV, "KEY_POWER")

def power_amp():
    send_ir(AMPLIFIER, "BTN_POWER")

def power_fireplace():
    send_ir("FIREPLACE", "TIVO")

def power_all():
    power_tv()
    power_amp()
    power_fireplace()


root = tk.Tk()
root.title("Media Remote")
root.geometry("1280x720")
root.overrideredirect(True)

# Load and set background image
script_dir = os.path.dirname(os.path.abspath(__file__))
bg_image_path = os.path.join(script_dir, "assets", "background.png", bg="black")
bg_image = Image.open(bg_image_path)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = bg_photo  # Keep a reference to prevent garbage collection


# Power buttons down right side
# Master Power button
master_icon_path = os.path.join(script_dir, "assets", "power_all.png")
master_icon = Image.open(master_icon_path)
master_photo = ImageTk.PhotoImage(master_icon)
master_btn = tk.Label(root, image=master_photo, borderwidth=0, highlightthickness=0, bg="black")
master_btn.place(x=840, y=30)
master_btn.bind("<Button-1>", lambda e: power_all())
master_btn.image = master_photo  # Keep a reference to prevent garbage collection

# TV Power button
tv_icon_path = os.path.join(script_dir, "assets", "power_tv.png")
tv_icon = Image.open(tv_icon_path)
tv_photo = ImageTk.PhotoImage(tv_icon)
tv_btn = tk.Label(root, image=tv_photo, borderwidth=0, highlightthickness=0, bg="black")
tv_btn.place(x=840, y=180)
tv_btn.bind("<Button-1>", lambda e: power_tv())
tv_btn.image = tv_photo  # Keep a reference to prevent garbage collection

# Amp power button
amp_icon_path = os.path.join(script_dir, "assets", "power_amp.png")
amp_icon = Image.open(amp_icon_path)
amp_photo = ImageTk.PhotoImage(amp_icon)
amp_btn = tk.Label(root, image=amp_photo, borderwidth=0, highlightthickness=0, bg="black")
amp_btn.place(x=840, y=330)
amp_btn.bind("<Button-1>", lambda e: power_amp())
amp_btn.image = amp_photo  # Keep a reference to prevent garbage collection

# Fireplace power button
fireplace_icon_path = os.path.join(script_dir, "assets", "power_fireplace.png")
fireplace_icon = Image.open(fireplace_icon_path)
fireplace_photo = ImageTk.PhotoImage(fireplace_icon)
fireplace_btn = tk.Label(root, image=fireplace_photo, borderwidth=0, highlightthickness=0, bg="black")
fireplace_btn.place(x=840, y=480)
fireplace_btn.bind("<Button-1>", lambda e: power_fireplace())
fireplace_btn.image = fireplace_photo  # Keep a reference to prevent garbage collection



# Volume Buttons
volume_up_icon_path = os.path.join(script_dir, "assets", "volume_up.png")
volume_up_icon = Image.open(volume_up_icon_path)
volume_up_photo = ImageTk.PhotoImage(volume_up_icon)
volume_up_btn = tk.Label(root, image=volume_up_photo, borderwidth=0, highlightthickness=0, bg="black")
volume_up_btn.place(x=620, y=250)
volume_up_btn.bind("<Button-1>", lambda e: send_ir(AMPLIFIER, "BTN_VOLUME_UP"))
volume_up_btn.image = volume_up_photo  # Keep a reference to prevent garbage collection

volume_down_icon_path = os.path.join(script_dir, "assets", "volume_down.png")
volume_down_icon = Image.open(volume_down_icon_path)
volume_down_photo = ImageTk.PhotoImage(volume_down_icon)
volume_down_btn = tk.Label(root, image=volume_down_photo, borderwidth=0, highlightthickness=0, bg="black")
volume_down_btn.place(x=620, y=450)
volume_down_btn.bind("<Button-1>", lambda e: send_ir(AMPLIFIER, "BTN_VOLUME_DOWN"))
volume_down_btn.image = volume_down_photo  # Keep a reference to prevent garbage collection



# Fireplace Buttons
fireplace_temp_icon_path = os.path.join(script_dir, "assets", "fireplace_temp.png")
fireplace_temp_icon = Image.open(fireplace_temp_icon_path)
fireplace_temp_photo = ImageTk.PhotoImage(fireplace_temp_icon)
fireplace_temp_btn = tk.Label(root, image=fireplace_temp_photo, borderwidth=0, highlightthickness=0, bg="black")
fireplace_temp_btn.place(x=620, y=20)
fireplace_temp_btn.bind("<Button-1>", lambda e: send_ir(FIREPLACE, "BTN_TEMP"))
fireplace_temp_btn.image = fireplace_temp_photo  # Keep a reference to prevent garbage collection


# TV Remote Buttons
tv_up_icon_path = os.path.join(script_dir, "assets", "tv_up.png")
tv_up_icon = Image.open(tv_up_icon_path)
tv_up_photo = ImageTk.PhotoImage(tv_up_icon)
tv_up_btn = tk.Label(root, image=tv_up_photo, borderwidth=0, highlightthickness=0)
tv_up_btn.place(x=200, y=80)
tv_up_btn.bind("<Button-1>", lambda e: send_ir(TV, "KEY_UP"))
tv_up_btn.image = tv_up_photo  # Keep a reference to prevent garbage collection

tv_down_icon_path = os.path.join(script_dir, "assets", "tv_down.png")
tv_down_icon = Image.open(tv_down_icon_path)
tv_down_photo = ImageTk.PhotoImage(tv_down_icon)
tv_down_btn = tk.Label(root, image=tv_down_photo, borderwidth=0, highlightthickness=0, bg="black")
tv_down_btn.place(x=200, y=410)
tv_down_btn.bind("<Button-1>", lambda e: send_ir(TV, "KEY_DOWN"))
tv_down_btn.image = tv_down_photo  # Keep a reference to prevent garbage collection

tv_left_icon_path = os.path.join(script_dir, "assets", "tv_left.png")
tv_left_icon = Image.open(tv_left_icon_path)
tv_left_photo = ImageTk.PhotoImage(tv_left_icon)
tv_left_btn = tk.Label(root, image=tv_left_photo, borderwidth=0, highlightthickness=0, bg="black")
tv_left_btn.place(x=30, y=245)
tv_left_btn.bind("<Button-1>", lambda e: send_ir(TV, "KEY_LEFT"))
tv_left_btn.image = tv_left_photo  # Keep a reference to prevent garbage collection

tv_right_icon_path = os.path.join(script_dir, "assets", "tv_right.png")
tv_right_icon = Image.open(tv_right_icon_path)
tv_right_photo = ImageTk.PhotoImage(tv_right_icon)
tv_right_btn = tk.Label(root, image=tv_right_photo, borderwidth=0, highlightthickness=0, bg="black")
tv_right_btn.place(x=370, y=245)
tv_right_btn.bind("<Button-1>", lambda e: send_ir(TV, "KEY_RIGHT"))
tv_right_btn.image = tv_right_photo  # Keep a reference to prevent garbage collection

tv_enter_icon_path = os.path.join(script_dir, "assets", "tv_enter.png")
tv_enter_icon = Image.open(tv_enter_icon_path)
tv_enter_photo = ImageTk.PhotoImage(tv_enter_icon)
tv_enter_btn = tk.Label(root, image=tv_enter_photo, borderwidth=0, highlightthickness=0, bg="black")
tv_enter_btn.place(x=200, y=245)
tv_enter_btn.bind("<Button-1>", lambda e: send_ir(TV, "KEY_ENTER"))
tv_enter_btn.image = tv_enter_photo  # Keep a reference to prevent garbage collection

tv_back_icon_path = os.path.join(script_dir, "assets", "tv_back.png")
tv_back_icon = Image.open(tv_back_icon_path)
tv_back_photo = ImageTk.PhotoImage(tv_back_icon)
tv_back_btn = tk.Label(root, image=tv_back_photo, borderwidth=0, highlightthickness=0, bg="black")
tv_back_btn.place(x=40, y=410)
tv_back_btn.bind("<Button-1>", lambda e: send_ir(TV, "KEY_EXIT"))
tv_back_btn.image = tv_back_photo  # Keep a reference to prevent garbage collection

tv_home_icon_path = os.path.join(script_dir, "assets", "tv_home.png")
tv_home_icon = Image.open(tv_home_icon_path)
tv_home_photo = ImageTk.PhotoImage(tv_home_icon)
tv_home_btn = tk.Label(root, image=tv_home_photo, borderwidth=0, highlightthickness=0, bg="black")
tv_home_btn.place(x=370, y=410)
tv_home_btn.bind("<Button-1>", lambda e: send_ir(TV, "KEY_BACK"))
tv_home_btn.image = tv_home_photo  # Keep a reference to prevent garbage collection


# Fonts
button_font = ("Helvetica", 24)
frame_font = ("Helvetica", 28, "bold")
exit_font = ("Helvetica", 14)





# Exit Button in bottom-right corner
exit_frame = tk.Frame(root)
exit_frame.pack(side="bottom", anchor="se", padx=10, pady=10)
exit_btn = tk.Button(exit_frame, text="Exit", command=exit_app, height=1, width=6, font=exit_font, bg="#888", fg="white")
exit_btn.pack()

root.mainloop()
