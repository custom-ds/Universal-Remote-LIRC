# Pi Remote

## Hardware
Display is based on the Raspberry Pi Touch Display 2, which is a 720x1280 pixels.


## Installing on a Pi
There is an installation script that handles most of the setup on the Raspberry Pi.

Use the Raspberry Pi Imager to install the base load of Raspberry Pi OS. This has been tested on a Pi 3 and Pi 4.

 - Install the 64 bit version of the operating system.
 - Set the time zone and keyboard layout as appropriate.
 - Set a hostname
 - Add a username, and set a password on it.
 - Configure the Wifi network.
 - Enable SSH access with password authentication.

Write out the image to the MicroSD card. Insert the card into the Raspberry Pi, then complete the assembly of the screen to the Pi. Attach the Pi daughter board to interface off to the 

Be sure to include the power cable as well as the ribbon cable. Attach the

Once assembly is completed, boot the Pi up

SSH into the new Pi computer using another PC. Update the core operating system before proceeding.

 - sudo apt update
 - sudo apt upgrade -y

RUN THE PACKAGE.PS1

COPY package.zip to the /home/{username}

```
unzip package.zip
chmod u+x install.sh
sudo .\install.sh
```




## Rasperry Pi Configuration
These are the manual steps required. If you use the `install.sh`, then these steps are generally taken care of for you, and you can skip this section. 

Install the required packages
```
sudo apt install xprintidle brightnessctl
sudo apt install python3-pillow
sudo apt install lirc
sudo apt install vim
```


Configure the Pi to use the GPIO port to send and receive IR signals

`sudo vi /boot/firmware/config.txt`

Add these two lines to the bottom of the config.txt file

```
dtoverlay=gpio-ir-tx,gpio_pin=17
dtoverlay=gpio-ir,gpio_pin=18
```

Save the file, then reboot the Raspberry Pi.

`sudo shutdown -r now`

You should be able to test the IR receiver. The basic form of that is to use the mode2 program to read in the gaps between the pulses and spaces.

`mode2 -d /dev/lirc0`

Note that it is possible that the devices have been created in other orders, and you may need to modify the device with something like `mode2 -d /dev/lirc1`. Check the /dev/ directory for possible options.

`ls /dev/lirc*`




### Screen Configuration
Resolution will automatically set, but the rotation angle needs to be corrected for the portrait mode.

Inside of the Raspbian GUI, go to Preferences -> Screen Configuration. Select DSI-1 from the screens list, and drill into Orientation and select Right.

Click the Apply button, and the confirm the change.


## LIRC Configurations

LIRC Remote repositories:
 - https://lirc-remotes.sourceforge.net/remotes-table.html

wget https://sourceforge.net/p/lirc-remotes/code/ci/master/tree/remotes/philips/TIVO34.lircd.conf?format=raw -Otivo34.lircd.conf


## Installing the Daemon
The GUI runs as a daemon that will automatically start when the Pi boots up. If the script crashes for any reason, the daemon will automatically restart itself.

Copy the remote.service file into /etc/systemd/system/ folder.

Configure the daemon to start on boot up.

```
sudo systemctl daemon-reload
sudo systemctl enable remote.service
```

You can start and stop the daemon by running:

```
systemctl start remote
systemctl stop remote
```

## Recording Unknown Remotes

Most of the mainstream remotes can be found in the LIRC repositories around the Internet, but certain less-known remotes either aren't there, or are hidden among random names of companies that might not even be around anymore.

To record, you'll use the Infrared Receiver, along with the irrecord program. irrecord will guide you through the process, which basically involves starting the recording, then pushing the buttons on the remote enough times that it generates templates of the various sequences.

Before you get started though, you should be aware of the standard naming convention for the key presses. It's possible to rename these outstand of the standards, but that requires an extra switch. To get the full list of possible buttons, type:

`irrecord --list-namespace`

To start recording, type `irrecord -d /dev/lirc0 myRemote.conf` and follow the prompts, where myRemote is a descriptive name of the specific remote or product that you are recording for.

Once it is finished recording, move the resulting .conf file into /etc/lirc/lircd.conf.d/, then restart the lirc services.

`systemctl restart lircd`

You should be able to see the new remote when you list the remotes.

`irsend LIST "" ""`

Then you can list the specific buttons available for the new remote, by listing that configuration.

`irsend LIST "myRemote" ""`

