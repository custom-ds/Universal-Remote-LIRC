import tkinter as tk
import subprocess

def send_ir(remote, command):
    subprocess.run(["irsend", "SEND_ONCE", remote, command])

def system_power():
    send_ir("Samsung_BN59-00507A", "KEY_POWER")
    send_ir("SONY_RM-AAU014", "BTN_POWER")

def exit_app(event=None):
    root.quit()

root = tk.Tk()
root.title("Media Remote")
root.geometry("1280x800")
root.overrideredirect(True)

# Ensure key binding works
root.focus_set()
root.bind_all('<Control-x>', exit_app)

# Fonts
button_font = ("Helvetica", 24)
frame_font = ("Helvetica", 28, "bold")
exit_font = ("Helvetica", 14)

# Define buttons
tv_buttons = {
    "TV Power": ("Samsung_BN59-00507A", "KEY_POWER")
}

amp_buttons = {
    "Amp Power": ("SONY_RM-AAU014", "BTN_POWER"),
    "Volume Up": ("SONY_RM-AAU014", "BTN_VOLUME_UP"),
    "Volume Down": ("SONY_RM-AAU014", "BTN_VOLUME_DOWN")
}

# System Power button
system_frame = tk.Frame(root, padx=30, pady=20)
system_frame.pack()
system_btn = tk.Button(system_frame, text="System Power", command=system_power,
                       height=2, width=25, font=button_font, bg="#FF5722", fg="white")
system_btn.pack()

# TV Controls
tv_frame = tk.LabelFrame(root, text="TV Controls", font=frame_font, padx=20, pady=20)
tv_frame.pack(padx=20, pady=10, fill="x")

for i, (label, (remote, cmd)) in enumerate(tv_buttons.items()):
    btn = tk.Button(tv_frame, text=label, command=lambda r=remote, c=cmd: send_ir(r, c),
                    height=2, width=20, font=button_font, bg="#4CAF50", fg="white")
    btn.grid(row=0, column=i, padx=10, pady=10)

# Amp Controls
amp_frame = tk.LabelFrame(root, text="Amp Controls", font=frame_font, padx=20, pady=20)
amp_frame.pack(padx=20, pady=10, fill="x")

for i, (label, (remote, cmd)) in enumerate(amp_buttons.items()):
    btn = tk.Button(amp_frame, text=label, command=lambda r=remote, c=cmd: send_ir(r, c),
                    height=2, width=20, font=button_font, bg="#2196F3", fg="white")
    btn.grid(row=0, column=i, padx=10, pady=10)

# Exit Button in bottom-right corner
exit_frame = tk.Frame(root)
exit_frame.pack(side="bottom", anchor="se", padx=10, pady=10)
exit_btn = tk.Button(exit_frame, text="Exit", command=exit_app,
                     height=1, width=6, font=exit_font, bg="#888", fg="white")
exit_btn.pack()

root.mainloop()
