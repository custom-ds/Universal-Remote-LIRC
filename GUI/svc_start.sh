[Unit]
Description=Touchscreen Media Remote
After=graphical.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/pi/media_remote.py
WorkingDirectory=/home/pi
User=pi
Environment=DISPLAY=:0
Environment=XAUTHORITY=/home/pi/.Xauthority
Restart=on-failure

[Install]
WantedBy=graphical.target