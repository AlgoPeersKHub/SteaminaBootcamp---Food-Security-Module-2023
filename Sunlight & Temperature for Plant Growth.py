"""
## Introduction
   Step into the future of farming with your Plant Growth Monitor! 🌱🚀 
   This project, powered by micro:bit technology, makes it a breeze for farmers to keep an eye on light, and temperature. 
   
## Parts of the Micro:bit Used & other resources
   
   Pins: To connect the external sensors to the micro:bit.
   Light sensor : To measue the amount f sunlight the crop or plant is receiving from the environment.
   Temperature sensor: To measure the soil temperature.
   
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
temperature = 0
light_level = 0
light_level_percentage = 0

# Display temperature on button press
def on_button_pressed_a():
    global temperature
    basic.show_number(temperature)
input.on_button_pressed(Button.A, on_button_pressed_a)

# Main loop
def on_forever():
    global light_level_percentage, light_level
    light_level = pins.analog_read_pin(AnalogPin.P0)
    light_level_percentage = (light_level) / (1023) * 100
    light_level_rounded = Math.round(light_level_percentage)
    temperature = input.temperature()

# Light level check
    if light_level_percentage < 50:
        basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        # # # # #
        . . . . .
        """)
        basic.show_string("I need sunlight")
        music.start_melody(music.built_in_melody(Melodies.PRELUDE), MelodyOptions.ONCE)
    
    elif light_level_percentage > 70:
            basic.show_string("I have enough sunlight")

datalogger.log(datalogger.create_cv("temp", temperature),
            datalogger.create_cv("light_level", light_level))

basic.forever(on_forever)

