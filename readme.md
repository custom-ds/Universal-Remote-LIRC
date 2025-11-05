# Pi Remote

## Hardware
Display is based on the Raspberry Pi Touch Display 2, which is a 720x1280 pixels.


## Rasperry Pi Configuration

sudo apt install xprintidle brightnessctl
sudo apt install python3-pillow

### Screen Configuration
Resolution will automatically set, but the rotation angle needs to be corrected for the portrait mode.

Inside of the Raspbian GUI, go to Preferences -> Screen Configuration. Select DSI-1 from the screens list, and drill into Orientation and select Right.

Click the Apply button, and the confirm the change.


## LIRC Configurations

LIRC Remote repositories:
 - https://lirc-remotes.sourceforge.net/remotes-table.html

wget https://sourceforge.net/p/lirc-remotes/code/ci/master/tree/remotes/philips/TIVO34.lircd.conf?format=raw -Otivo34.lircd.conf


## 