vegetable = ""
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE9600)
basic.show_icon(IconNames.HEART)
basic.clear_screen()

def on_forever():
    global vegetable
    vegetable = serial.read_string()
    if vegetable == "Healthy Cabbage Plant":
        basic.show_icon(IconNames.YES)
        servos.P0.set_angle(180)
        basic.pause(500)
    elif vegetable == "Unhealthy Cabbage Plant - Worm":
        basic.show_icon(IconNames.NO)
        servos.P0.set_angle(0)
        basic.pause(500)
    elif vegetable == "Unhealthy Cabbage Plant - Aphids":
        basic.show_icon(IconNames.NO)
        servos.P0.set_angle(0)
        basic.pause(500)
    elif vegetable == "Unhealthy Cabbage Plant - Looper":
        basic.show_icon(IconNames.NO)
        servos.P0.set_angle(0)
        basic.pause(500)
    elif vegetable == "Unhealthy Tomato Plant -Aphids":
        basic.show_icon(IconNames.NO)
        servos.P0.set_angle(0)
        basic.pause(500)
    elif vegetable == "Unhealthy Tomato Plant - Whiteflies":
        basic.show_icon(IconNames.NO)
        servos.P0.set_angle(0)
        basic.pause(500)
    elif vegetable == "Unhealthy Tomato Plant- Hookworm":
        basic.show_icon(IconNames.NO)
        servos.P0.set_angle(0)
        basic.pause(500)
    elif vegetable == "Healthy Tomato Plant":
        basic.show_icon(IconNames.YES)
        servos.P0.set_angle(180)
        basic.pause(500)
    elif vegetable == "Unhealthy Lettuce - Aphids":
        basic.show_icon(IconNames.NO)
        servos.P0.set_angle(0)
        basic.pause(500)
    elif vegetable == "Unhealthy Lettuce - Cutworms":
        basic.show_icon(IconNames.NO)
        servos.P0.set_angle(0)
        basic.pause(500)
    elif vegetable == "Unhealthy Lettuce - Leafminers":
        basic.show_icon(IconNames.NO)
        servos.P0.set_angle(0)
        basic.pause(500)
    elif vegetable == "Healthy Lettuce Plant":
        basic.show_icon(IconNames.NO)
        servos.P0.set_angle(180)
        basic.pause(500)
    else:
        basic.show_string("No image detected!")
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        basic.pause(500)
basic.forever(on_forever)
