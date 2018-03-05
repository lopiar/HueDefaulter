# !/usr/bin/python

from phue import Bridge
import time
import json

default_temp = 366
ideal_temp = 275  # Enter the desired colour temp here.
bridge_ip = '192.168.1.64'  # Enter bridge IP here.
sleep_time = 30

b = Bridge(bridge_ip)

# If running for the first time, press button on bridge and run with b.connect() uncommented
b.connect()

lights = b.get_light_objects()
try:
    while True:
        # Version 1:
        # lights_to_change = []
        # for light in lights:
        #     if light.colortemp == default_temp:
        #         lights_to_change.append(light)
        # if lights_to_change:
        #     print('Fixing: ',lights_to_change)
        #     for l in lights_to_change:
        #         l.colortemp = ideal_temp

        # Version 2: 
        # lights = json.dumps(b.get_api().get('lights'))
        # lights = json.loads(lights)
        # lights_to_change = [int(d) for d in lights if lights[d]['state']['ct'] == default_temp]
        # if lights_to_change:
        #     b.set_light(lights_to_change, 'ct', ideal_temp)
        #     print('Fixing: ',lights_to_change)

        # Version 3:
        for light in lights:
            if light.colortemp == default_temp:
                light.colortemp = ideal_temp
                print('Fixing: ', light.light_id)

        # Version 4: 
        # for light in lights:
        #     light.colortemp = ideal_temp


        time.sleep(sleep_time)
except KeyboardInterrupt:
    print('interrupted!')
