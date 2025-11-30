import tkinter as tk
import subprocess
import os
from PIL import Image, ImageTk
import time

# Remote constants
PROJECTOR = "Epson_12807990"
TV = "Samsung_BN59-00507A"
HDMI_SWITCH = "REI_HDMI_Switcher"
CAMERA = "Monoprice_PTZ"



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

    # Draw a box around the Input Select
    canvas.create_rectangle(40, 80, 600, 210, outline="#444", width=2)

    # # Draw a box around the Fireplace controls
    # canvas.create_rectangle(600, 422, 1275, 558, outline="#444", width=2)

    # Draw a box around the TV Remote controls
    canvas.create_rectangle(40, 260, 600, 710, outline="#444", width=2)
    canvas.create_text(90, 240, text="Camera", font=("Helvetica", 16), fill="white")     # Label the box
    

    # Load the Power buttons
    btnPowerAll, btnPowerAllImg = draw_image_button(canvas, "power/org_system.png", 945, 20, lambda e: power_all())
    btnPowerTVs, btnPowerTVsImg = draw_image_button(canvas, "power/blu_tvs.png", 945, 160, lambda e: power_tvs())
    btnPowerProjector, btnPowerProjectorImg = draw_image_button(canvas, "power/blu_projector.png", 945, 300, lambda e: power_projector())
    btnPowerCamera, btnPowerCameraImg = draw_image_button(canvas, "power/gra_camera.png", 945, 440, lambda e: power_camera())

    # Camera Buttons
    btnCameraUp, btnCameraUpImg = draw_image_button(canvas, "round/115/blu_up.png", 190, 280, lambda e: send_ir(CAMERA, "KEY_UP"))
    btnCameraDown, btnCameraDownImg = draw_image_button(canvas, "round/115/blu_down.png", 190, 420, lambda e: send_ir(CAMERA, "KEY_DOWN"))
    btnCameraLeft, btnCameraLeftImg = draw_image_button(canvas, "round/115/blu_left.png", 50, 350, lambda e: send_ir(CAMERA, "KEY_LEFT"))
    btnCameraRight, btnCameraRightImg = draw_image_button(canvas, "round/115/blu_right.png", 330, 350, lambda e: send_ir(CAMERA, "KEY_RIGHT"))

    btnCameraZoomIn, btnCameraZoomInImg = draw_image_button(canvas, "round/115/gre_plus.png", 470, 280, lambda e: send_ir(CAMERA, "KEY_PLUS"))
    btnCameraZoomOut, btnCameraZoomOutImg = draw_image_button(canvas, "round/115/gre_minus.png", 470, 420, lambda e: send_ir(CAMERA, "KEY_MINUS"))

    btnCamera1, btnCamera1Img = draw_image_button(canvas, "round/115/blu_1.png", 50, 580, lambda e: send_ir(CAMERA, "KEY_1"))
    btnCamera2, btnCamera2Img = draw_image_button(canvas, "round/115/blu_2.png", 190, 580, lambda e: send_ir(CAMERA, "KEY_2"))
    btnCamera3, btnCamera3Img = draw_image_button(canvas, "round/115/blu_3.png", 330, 580, lambda e: send_ir(CAMERA, "KEY_3"))
    btnCamera4, btnCamera4Img = draw_image_button(canvas, "round/115/blu_4.png", 470, 580, lambda e: send_ir(CAMERA, "KEY_4"))

    # Swap Button
    btnSwapUp, btnSwapUpImg = draw_image_button(canvas, "round/115/org_swap.png", 620, 290, lambda e: send_ir(HDMI_SWITCH, "BTN_INPUT"))
    # btnVolumeDown, btnVolumeDownImg = draw_image_button(canvas, "volume_down.png", 780, 295, lambda e: send_ir(AMPLIFIER, "BTN_VOLUME_DOWN"))

    # btnFireTemp, btnFireTempImg = draw_image_button(canvas, "fireplace_temp.png", 620, 430, lambda e: send_ir(FIREPLACE, "KEY_TEMP"))


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
    time.sleep(0.25)



def exit_app(event=None):
    root.quit()

def power_tvs():
    send_ir(TV, "KEY_POWER")

def power_camera():
    send_ir(CAMERA, "KEY_POWER")

def power_projector():
    send_ir(PROJECTOR, "KEY_POWER")

def power_all():
    power_projector()
    time.sleep(1.00)
    power_projector()       #double-tap the power to turn it back off
    time.sleep(0.25)
    power_tvs()
    time.sleep(0.25)



if __name__ == "__main__":
    main()
