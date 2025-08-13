soil_moisture_level = 0
led.set_brightness(64)

def on_forever():
    global soil_moisture_level
    soil_moisture_level = pins.analog_read_pin(AnalogPin.P0)
    led.plot_bar_graph("soil_moisture_level (ml)", soil_moisture_level)
    datalogger.log (datalogger.create_cv("soil_moisture_level (ml)", soil_moisture_level))
    basic.pause(5000)
    if soil_moisture_level < 450:
       basic.show_icon(IconNames.SAD)
       basic.show_string("I'm dry and thirsty!!")
       serial.write_number(soil_moisture_level)
       music.start_melody(music.built_in_melody(Melodies.PRELUDE), MelodyOptions.ONCE)
    else:
        basic.show_icon(IconNames.HAPPY)
    if input.button_is_pressed(Button.A):
        basic.number(soil_moisture_level)
        
    basic.forever(on_forever)
