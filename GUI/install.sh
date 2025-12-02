#!/bin/bash

#Prompt the user for the account they want to install the application for
echo "Please enter the username of the account you want to install Universal Remote for:"
read USERNAME

# Check to see if the lirc package is installed, and if not, install it
if ! dpkg -s lirc >/dev/null 2>&1; then
    echo "lirc package is not installed. Installing lirc..."
    sudo apt-get update
    sudo apt-get install -y lirc
else
    echo "lirc package is already installed."
fi

echo "Setting up application files..."
# Create the install directory if it doesn't exist
INSTALL_DIR="/opt/universal-remote"

if [ ! -d "$INSTALL_DIR" ]; then
    sudo mkdir -p "$INSTALL_DIR"
fi
# Unzip the assets.zip into the install directory
sudo unzip -o assets.zip -d "$INSTALL_DIR"
# Delete the original assets.zip file
sudo rm -f assets.zip

# move the remote.py to the install directory
sudo mv -f remote.py "$INSTALL_DIR/remote.py"

# Set the appropriate permissions
sudo chmod -R 755 "$INSTALL_DIR"


echo "Setting up lircd configuration files..."
# Copy the lircd config files to /etc/lirc/lircd.conf.d/
if [ ! -d "/etc/lirc/lircd.conf.d" ]; then
    sudo mkdir -p "/etc/lirc/lircd.conf.d"
fi

# Unzip the lircd.zip into the lircd.conf.d directory
sudo unzip -o lircd.zip -d "/etc/lirc/lircd.conf.d"
# Delete the original lircd.zip file
sudo rm -f lircd.zip

# prompt the user if the boot/config.txt should be updated
echo "Do you want to update /boot/config.txt to enable the IR transmitter and receiver? (y/n)"
read UPDATE_CONFIG
if [ "$UPDATE_CONFIG" == "y" ] || [ "$UPDATE_CONFIG" == "Y" ]; then
    # Check if dtoverlay=gpio-ir,gpio_pin=18 already exists in /boot/config.txt
    if ! grep -q "dtoverlay=gpio-ir" /boot/config.txt; then
        echo "Updating /boot/config.txt to enable the IR transmitter and receiver..."
        echo "dtoverlay=gpio-ir,gpio_pin=17" | sudo tee -a /boot/config.txt
        echo "dtoverlay=gpio-ir-tx,gpio_pin=18" | sudo tee -a /boot/config.txt
        echo ""
        echo "/boot/config.txt has been updated."
        echo "!!! A reboot may be required for the changes to take effect !!!"
        echo ""
    else
        echo "/boot/config.txt already contains the necessary configuration."
    fi
else
    echo "Skipping update of /boot/config.txt."
fi

# Do you want to rotate the Raspberry pi screen 90 degrees? (y/n)
echo "Do you want to rotate the Raspberry Pi screen 90 degrees? (y/n)"
read ROTATE_SCREEN
if [ "$ROTATE_SCREEN" == "y" ] || [ "$ROTATE_SCREEN" == "Y" ]; then
    # Check if display_lcd_rotate=1 already exists in /boot/config.txt
    if ! grep -q "display_lcd_rotate" /boot/config.txt; then
        echo "Rotating the Raspberry Pi screen 90 degrees..."
        echo "display_lcd_rotate=3" | sudo tee -a /boot/config.txt
        echo ""
        echo "/boot/config.txt has been updated to rotate the screen."
        echo "!!! A reboot may be required for the changes to take effect !!!"
        echo ""
    else
        echo "/boot/config.txt already contains the screen rotation configuration."
    fi
else
    echo "Skipping screen rotation."
fi

# Restart lircd service to apply new configurations
echo "...restarting lircd service to apply new configurations"
sudo systemctl restart lircd


echo "Setting up the remote control service..."
# Update the remote.service file to use the correct USERNAME
sudo sed -i "s/USERNAME/$USERNAME/g" remote.service

# Move the remote.service file to /etc/systemd/system/
sudo mv -f remote.service /etc/systemd/system/remote.service

# Reload systemd to recognize the new service
sudo systemctl daemon-reload

# Enable the remote service to start on boot
echo "...enabling remote service to start on boot"
sudo systemctl enable remote.service










# Start the remote service immediately
sudo systemctl start remote.service