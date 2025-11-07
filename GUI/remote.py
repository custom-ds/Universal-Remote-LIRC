import tkinter as tk
import subprocess
import os
from PIL import Image, ImageTk

# Remote constants
AMPLIFIER = "SONY_RM-AAU014"
#TV = "Samsung_BN59-00507A"
TV = "SAMSUNG-C750"
FIREPLACE = "tivo"



root = tk.Tk()
root.attributes('-fullscreen', True)  # Fullscreen mode covering taskbar
root.overrideredirect(True)  # Remove title bar and window decorations
root.attributes('-topmost', True)  # Keep window on top
canvas = tk.Canvas(root, width=1280, height=720)
canvas.pack()

def main():



    # Load gradient background
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pathFilename = os.path.join(script_dir, "assets", "background.png")
    bg_img = ImageTk.PhotoImage(Image.open(pathFilename))
    canvas.create_image(0, 0, anchor="nw", image=bg_img)

    # Load the buttons
    btnPowerAll, btnPowerAllImg = draw_image_button(canvas, "power_all.png", 840, 30, lambda e: power_all())
    btnPowerTV, btnPowerTVImg = draw_image_button(canvas, "power_tv.png", 840, 180, lambda e: power_tv())
    btnPowerAmp, btnPowerAmpImg = draw_image_button(canvas, "power_amp.png", 840, 330, lambda e: power_amp())
    btnPowerFireplace, btnPowerFireplaceImg = draw_image_button(canvas, "power_fireplace.png", 840, 480, lambda e: power_fireplace())

    # TV Remote Buttons
    btnTVUp, btnTVUpImg = draw_image_button(canvas, "tv_up.png", 200, 80, lambda e: send_ir(TV, "KEY_UP"))
    btnTVDown, btnTVDownImg = draw_image_button(canvas, "tv_down.png", 200, 410, lambda e: send_ir(TV, "KEY_DOWN"))
    btnTVLeft, btnTVLeftImg = draw_image_button(canvas, "tv_left.png", 30, 245, lambda e: send_ir(TV, "KEY_LEFT"))
    btnTVRight, btnTVRightImg = draw_image_button(canvas, "tv_right.png", 370, 245, lambda e: send_ir(TV, "KEY_RIGHT"))
    btnTVEnter, btnTVEnterImg = draw_image_button(canvas, "tv_enter.png", 200, 245, lambda e: send_ir(TV, "KEY_ENTER"))
    btnTVBack, btnTVBackImg = draw_image_button(canvas, "tv_back.png", 40, 410, lambda e: send_ir(TV, "KEY_EXIT"))
    btnTVHome, btnTVHomeImg = draw_image_button(canvas, "tv_home.png", 370, 410, lambda e: send_ir(TV, "KEY_BACK"))

    # Volume Buttons
    btnVolumeUp, btnVolumeUpImg = draw_image_button(canvas, "volume_up.png", 620, 250, lambda e: send_ir(AMPLIFIER, "BTN_VOLUME_UP"))
    btnVolumeDown, btnVolumeDownImg = draw_image_button(canvas, "volume_down.png", 620, 450, lambda e: send_ir(AMPLIFIER, "BTN_VOLUME_DOWN"))





    # Exit Button in bottom-right corner
    exit_font = ("Helvetica", 14)
    exit_frame = tk.Frame(root)
    exit_frame.pack(side="bottom", anchor="se", padx=10, pady=10)
    exit_btn = tk.Button(exit_frame, text="Exit", command=exit_app, height=1, width=6, font=exit_font, bg="#888", fg="white")
    exit_btn.pack()

    root.mainloop()


def draw_image_button(canvas, image_filename, x, y, event_handler):
    """
    Draw a PNG image on the canvas at the given position and bind an event handler.
    
    Args:
        canvas: The tkinter Canvas widget
        image_path: Path to the .png image file
        x: X-coordinate position
        y: Y-coordinate position
        event_handler: Function to call when the image is clicked
        
    Returns:
        tuple: (image_id, image_reference) - The canvas item ID and image reference
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pathFilename = os.path.join(script_dir, "assets", image_filename)
    img = ImageTk.PhotoImage(Image.open(pathFilename))
    img_id = canvas.create_image(x, y, anchor="nw", image=img)
    canvas.tag_bind(img_id, "<Button-1>", event_handler)
    return img_id, img

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


if __name__ == "__main__":
    main()