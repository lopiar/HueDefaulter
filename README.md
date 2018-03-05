# HueDefaulter
A Python script to fix the default settings on Hue bulbs that have been power cycled.

## Usage
1. Set bridge_ip to be the IP of your Hue Bridge.
2. Set ideal_temp to be the preferred colour temperature in [mireds](https://en.wikipedia.org/wiki/Mired).
3. Set sleep_time to be your preferred delay in seconds. Higher delay means slower fixing of the lights but less stress on the bridge.
4. Choose your version of the script to run by uncommenting it. 
5. If running for the first time, press the button on your Hue bridge.
6. Run hue.py

### Version 1
This will check all of the bulbs individually to see which are at the default colour temperature, and then changes them all to the ideal temp.

### Version 2
This checks all of the bulbs at once and then changes them to the ideal temp. This puts the lightest load on the bridge.

### Version 3
This will check all of the bulbs individually and then fix them as it finds default colour temperature bulbs.

### Version 4
This doesn't check anything and just sets all bulbs to the ideal temperature over and over. Not recommended.
