# adafruit-trinkey-ptt
Creating a PTT(Push-To-Talk) button through the use of an Adafruit NeoKey trinkey.
By default the NeoKey is configured to output 'T'.

It is necessary to configure the NeoKey before being able to use the given Python script.
Go to the following link to download the STABLE drivers: https://circuitpython.org/board/adafruit_neokey_trinkey_m0/.

Make sure the NeoKey is connected to the device.
Once these drivers are installed, reset the NeoKey by putting it in bootmode.
Press the reset button underneath the key TWICE and a drive will appear. This is the boot drive.
Now, to install the drivers, drag the .uf2 file onto the drive and the drive will disappear and reappear again.

The NeoKey is now correctly configured, drag the Python script inside the drive.

Sometimes the script will run automatically, sometimes it will not. It is however, good practice to follow the following steps either way:

Before the Python script is active, the NeoKey needs to be 'reloaded': this is done through the PuTTY software: https://www.putty.org/.
Download and install the stable release and execute it afterwards.

While PuTTY is active, make way to device manager -> ports(COM & LPT) and check which port the NeoKey occupies.
Note this down and head to the PuTTY configuration window.

Fill in the following fields with these values:
    Serial line     :   COM(whatever the NeoKey occupies on the device)
    Speed           :   115200
    Connection Type :   Serial; Telnet

Now connect the serial console and press the following commands: CTRL+C and then CTRL+D.

The code is now correctly 'halted' and 'reloaded' and thus now ready for use.



