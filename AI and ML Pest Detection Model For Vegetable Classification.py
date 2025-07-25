"""
## Introduction
   Imagine a garden where technology acts as a vigilant guardian, detecting potential threats to your veggies before they can do harm. 
   Our project is here to make your plants flourish, ensuring a bountiful harvest with each season

## Parts of the micro:bit Used
   
    LED Matrix: Used to display icons indicating the health status of the vegetable plants.

    Serial Communication Pins (USB_TX, USB_RX): Utilized to establish communication between the micro:bit and an external device.

    Servo Motor Pin (P0): Controls the movement of a servo motor to visually represent the health status of the vegetable plants.


## Programming Concept
   
   Communication Setup: It sets up communication between the micro:bit and an external device using serial communication.

   Variable : It uses a variable (vegetable) to store information received from the external device.

   Forever Loop: The code runs a continuous loop to process information.

   Conditions Check (if-elif): Based on the received information, it takes different actions, like showing icons and moving a servo motor.


## Programming Language
   Python

## Coding Environment or Text Editor
   Microsoft Makecode for micro:bit (https://makecode.microbit.org/#editor)

## Feel free to comment or contribute

## Note: Use this project together with the pest detection model.

"""

## Project Code or Program

# an instruction to establish communication between micro:bit and AI
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, 9600) 
basic.show_icon(IconNames.HEART)
basic.clear_screen()

#create an empty variable to be receiving information from AI glitch

vegetable = " "

#Create forever loop to run program forever
def on_forever():
    global vegetable
    vegetable = serial.read_string() # an instruction for vegetable variable to receive information from AI
    if vegetable == "Healthy Cabbage Plant":
        basic.show_icon(IconNames.YES)
        servos.P0.set_angle(180)
        basic.pause(5000)
    elif vegetable == "Unhealthy Cabbage Plant - Worm":
        basic.show_icon(IconNames.NO)
        servos.P0.set_angle(0)
        basic.pause(5000)
    elif vegetable == "Unhealthy Cabbage Plant - Aphids":
        basic.show_icon(IconNames.NO)
        servos.P0.set_angle(0)
        basic.pause(5000)
    elif vegetable == "Unhealthy Cabbage Plant - Looper":
        basic.show_icon(IconNames.NO)
        servos.P0.set_angle(0)
        basic.pause(5000)
    elif vegetable == "Unhealthy Tomato Plant -Aphids":
        basic.show_icon(IconNames.No)
        servos.P0.set_angle(0)
        basic.pause(5000)
    elif vegetable == "Unhealthy Tomato Plant - Whiteflies":
        basic.show_icon(IconNames.NO)
        servos.P0.set_angle(0)
        basic.pause(5000)
    elif vegetable == "Unhealthy Tomato Plant- Hookworm":
        basic.show_icon(IconNames.NO)
        servos.P0.set_angle(0)
        basic.pause(5000)
    elif vegetable == "Healthy Tomato Plant":
        basic.show_icon(IconNames.YES)
        servos.P0.set_angle(180)
        basic.pause(5000)
    basic.forever(on_forever)
