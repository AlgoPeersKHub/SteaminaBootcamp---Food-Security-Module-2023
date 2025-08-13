"""
## Introduction
   Step into the future of farming with Smart Irrigation System! 🌱🚀 
   This project, powered by micro:bit technology, makes it a breeze for farmers to keep an eye on soil moisture. 
   The micro:bit logs data, and the smart irrigation system kicks in to water the crops precisely when needed. 
   
  🌾💡 Note: Cocopeat, a sustainable soil alternative made from coconut husks, was used. 

## Parts of the Micro:bit Used & other resources
   
   Pins: To connect the external sensors to the micro:bit.
   Soil Moisture Sensor: To measure the soi moisture sensor.
   Water pump: A pump to irrigate the crops or plants when needed.


## Programming Concepts
   
   Variables: Storage containers for data, like holding information about moisture levels, temperature, and light intensity.
   Functions: Blocks of code that perform specific tasks, such as displaying temperature on button press or managing the main program loop.
   Conditional Statements: If-else statements decide which actions to take based on conditions. For example, if the moisture level is below 50%, it displays a message about needing water.
   Loops: The on_forever function represents a continuous loop that repeatedly checks and responds to sensor data.
   Math Operations: Mathematical calculations, like calculating the percentage of moisture level or rounding the value.
   Logging: Storing information systematically, demonstrated by logging moisture, temperature, and light level data.
   Control Flow: The flow of execution, moving from one part of the code to another based on conditions and loops.

## Programming Language: Python

## Coding Environment or Text Editor
   Microsoft Makecode (https://makecode.microbit.org/#editor)

## Feel free to comment or contribute

"""


## Project Code or Program

# Variables to store sensor readings
cocopeats_moisture_level = 0
cocopeats_moisture_level_in_percentage = 0
cocopeats_moisture_level_rounded = 0

# Main loop
def on_forever():
    global cocopeats_moisture_level, cocopeats_moisture_level_in_percentage, cocopeats_moisture_level_rounded
    cocopeats_moisture_level = pins.analog_read_pin(AnalogPin.P0)
    cocopeats_moisture_level_in_percentage = ((cocopeats_moisture_level - 0) / (1023 - 0)) * 100
    cocopeats_moisture_level_rounded = Math.round(cocopeats_moisture_level_in_percentage)
     

    # Moisture level check
    if cocopeats_moisture_level_rounded < 50:
        basic.show_string("I need water!!")
        pins.digital_write_pin(DigitalPin.P2, 1)
        basic.pause(5000)
        pins.digital_write_pin(DigitalPin.P2, 0) 
    else:
        basic.show_string("I have enough water")
        datalogger.log(datalogger.create_cv("moisture(%)", cocopeats_moisture_level_rounded), 
            
basic.forever(on_forever)
