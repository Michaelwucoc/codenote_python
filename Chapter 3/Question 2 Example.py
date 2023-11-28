import time
rain = 0 # Outputs "1" when it's raining and "0" when it's not
soil = 1 # Outputs "1" when the soil is dry and "0" when it's moist
timer = 1 # Outputs "1" at specific times of the day to water the crops
startWatering = 0 # 0 for turn off the watering system
if timer and soil and not rain:
    startWatering = 1
else:
    startWatering = 0
if startWatering:
    print('NOW the watering system is ON!!')
for _ in range(11):
    print('###### Watering the crops now ######')
    time.sleep(1)