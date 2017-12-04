# !/usr/bin/python

from phue import Bridge
import time

ideal_temp = 275
bridge_ip = '192.168.1.64' # Enter bridge IP here.

b = Bridge(bridge_ip)

# If running for the first time, press button on bridge and run with b.connect() uncommented
b.connect()

lights = b.get_light_objects()
try:
    while True:
        # lights_to_change = []
        # for light in lights:
        #     if light.colortemp == 366:
        #         lights_to_change.append(light)
        # if lights_to_change:
        #     print('Changing these lights: ',lights_to_change)
        #     for l in lights_to_change:
        #         l.colortemp = 275
        #         l.on = False

        for light in lights:
            if light.colortemp == 366:
                light.colortemp = ideal_temp
                print('Fixed light: ', light.light_id)

        time.sleep(1)
except KeyboardInterrupt:
    print('interrupted!')



