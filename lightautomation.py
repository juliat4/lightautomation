
import requests
import lifxlan
import sys
from lifxlan import LifxLAN, BLUE, GREEN
from time import sleep
#from gpiozero import Button

def main():
    num_lights = 2
    
    # instantiate lifxLAN client
    print("Discovering lights...")
    lifx = LifxLAN(num_lights)  #creating an object to represent the local network, LifxLAN is a class (previously defined)

    #get devices
    devices = lifx.get_lights()
    bulb = devices[0]

    print("\nFound {} light(s):\n".format(bulb.get_label()))
    
    if bulb.get_label() == "Lamp":
        Lamp = devices[0]
    else: 
        Lamp = devices[1]

    #for d in devices:
        #try:
            #print(d)
        #except:
            #pass

    #get original state of lights
    original_power = Lamp.get_power()
    print(original_power)
    
    #button = Button(2)
    # if button.when_pressed():
    #     toggle_light(Lamp, original_power)

    #check for button press
    if input():
        toggle_light(Lamp, original_power)

def toggle_light(device, original_state):
    if original_state == 0:
        device.set_power("on")
    else:
        device.set_power("off")


if __name__ == "__main__":
    main()
    
    