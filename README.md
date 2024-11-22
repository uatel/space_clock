# Space Clock

 Turn your M5Stack into a space clock
![preview](resources/help.jpg)

## What can they do:
- Animated space wallpaper with a flying astronaut
- Adaptive backlight mode will set the brightness depending on the time of day (Bright screen during the day and dim at night).
- Add up to 4 alarm clocks. You can set up a repeat by day of the week.
- Disable and activate alarms using the alarm clock manager.
- Get notifications from your phone via Bluetooth.
- Using the settings menu, you can synchronize your watch with the time from the Internet, adjust the brightness of the screen, select an alarm ringtone.
- Connect to Wi-Fi using Wi-Fi Manager(No need to reboot your device)
- View the weather using OpenWeather API
- Run the any *.py scripts from app directory(Calculator, Timer, Weather and etc.).
- You can enter debug mode directly from the watch menu.

## Copyright:
- Mentioned project it is fork of https://github.com/pavelprosto94/space_clock project for M5Stack Core2 1.1.

## Installation
- Using M5 Burner, install the current version of UIFlow_Core 2 (If you have a new device)
- Restart your device
- Select Flow > Wi-Fi
- Go to M5Flow (https://flow.m5stack.com /)
- Specify your "API KEY" and device type "Core2"
- Switch to Python mode
- Copy and paste the code to set the clock from the file (https://github.com/uatel/space_clock/blob/main/install.py )
- Click the Run button
![preview](resources/help_1.jpg)
- Wait for the installation to finish. All necessary files will be copied from the GitHub repository
- After restarting the device
- Select App > space_clock.py > Run

A bug may occur, the clock is not drawn, and the Run button is lit blue. Don't worry, M5Stack has already specified this file as the default execution.
- Don't press anything and wait 10 seconds
- After that, the clock will start itself

## Update device
- Restart your device
- Select Flow > Wi-Fi
- Go to M5Flow (https://flow.m5stack.com /)
- Specify your "API KEY" and device type "Core2"
- Switch to Python mode
- Copy and paste **New install** code from the file (https://github.com/uatel/space_clock/blob/main/install.py )
- Click the Run button
![preview](resources/help_1.jpg)
- Wait for the installation to finish. All necessary files will be copied from the GitHub repository
- After restart the device
- Select App > space_clock.py > Run

## Bluetooth support
Using this service, you will be able to connect your **M5Stack** via **Bluetooth** and receive notifications on it.

### on M5Stack device:
- Go to App List(hold down right button)
- Go to Bluetooth
- Enable service
- Save and Restart device
If you need an indication of the connection process, turn on the "Bluetooth LED indicator". With this option, the green LED will light up when connected. If there is no connection, the LED will start flashing. Important, do not connect to the device until the clock is fully incilized (let the "Incilization..." disappear)
