# !/usr/bin/python

from phue import Bridge
import time
import json

default_temp = 366
ideal_temp = 275  # Enter the desired colour temp here.
bridge_ip = '192.168.1.64'  # Enter bridge IP here.

b = Bridge(bridge_ip)

# If running for the first time, press button on bridge and run with b.connect() uncommented
b.connect()

lights = b.get_light_objects()
try:
    while True:
        # Version 1: This checks all the lights individually and then fixes them all in one go. It is joint second fastest and joint worst performance.
        # lights_to_change = []
        # for light in lights:
        #     if light.colortemp == default_temp:
        #         lights_to_change.append(light)
        # if lights_to_change:
        #     print('Fixing: ',lights_to_change)
        #     for l in lights_to_change:
        #         l.colortemp = ideal_temp

        # Version 2: This gets the data for all the lights in one go, then checks which need to be fixed and fixes them in one go. It is the slowest but the best for performance.
        # lights = json.dumps(b.get_api().get('lights'))
        # lights = json.loads(lights)
        # lights_to_change = [int(d) for d in lights if lights[d]['state']['ct'] == default_temp]
        # if lights_to_change:
        #     b.set_light(lights_to_change, 'ct', ideal_temp)
        #     print('Fixing: ',lights_to_change)

        # Version 3: This checks each light invidiually then fixes the light before moving to the next one. It is joint second fastest and joint worst performance.
        for light in lights:
            if light.colortemp == default_temp:
                light.colortemp = ideal_temp
                print('Fixing: ', light.light_id)

        # Version 4: This doesn't check the lights at all, it just tells them all to go to the right temp over and over. It is the fastest and second best performance, but it means that all bulbs will be set to the same hue.
        # for light in lights:
        #     if light.colortemp == default_temp:
        #         light.colortemp = ideal_temp
        #         print('Fixing: ', light.light_id)

        time.sleep(1)  # Change this to whatever you like. Higher number improves performance but slows down the fixing
except KeyboardInterrupt:
    print('interrupted!')
