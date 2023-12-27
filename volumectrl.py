# for sound
# For Acessing Speakers
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math

#for brightness
import screen_brightness_control as sbc

# Code for Sound Control
# Code for Volume Increase
def VolumeIncrease():
    currentVolumeDb = volume.GetMasterVolumeLevel()
    if currentVolumeDb + 5 >= 0:
        currentVolumeDb = 0
    else:
        currentVolumeDb += 5
    volume.SetMasterVolumeLevel(currentVolumeDb, None)

# Code for Volume Decrease
def VolumeDecrease():
    currentVolumeDb = volume.GetMasterVolumeLevel()
    if currentVolumeDb - 5 <= -65.25:
        currentVolumeDb = -65.25
    else:
        currentVolumeDb -= 5
    volume.SetMasterVolumeLevel(currentVolumeDb, None)

# Code for Volume Mute
def VolumeMute():
    volume.SetMute(0, None)


# Code for Increase Brightness
def BrightnessIncrease():
    current_brightness = sbc.get_brightness()
    current_brightness[0] += 5
    sbc.set_brightness(current_brightness[0])

# Code for Decrease Brightness
def BrightnessDecrease():
    current_brightness = sbc.get_brightness()
    current_brightness[0] -= 5
    sbc.set_brightness(current_brightness[0]) 



devices = AudioUtilities.GetSpeakers()
interface = devices.Activate( IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Get current volume 
currentVolumeDb = volume.GetMasterVolumeLevel()
print(currentVolumeDb)
current_bright = sbc.get_brightness()
print(current_bright)
def volume(vol):
    if(vol ==1):
        VolumeIncrease()
    elif(vol == 2):
        VolumeDecrease()
    elif(vol == 3):
        BrightnessIncrease()
    elif(vol == 4):
        BrightnessDecrease()
