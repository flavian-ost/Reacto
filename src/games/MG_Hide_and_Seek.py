def Hide_and_Seek():
    from lcd_i2c import LCD
    from time import sleep_ms
    from machine import I2C

    ADDR = 0x20   # LCD-Adresse
    lcd = LCD(ADDR, 16, 2, i2c=I2C(1))
    lcd.begin()

    buttons = ModulinoButtons()
    buttons.set_led_status(True, False, False)

    text = "Hide and Seek, you have 5 seconds to hide REACTO!   "

    for i in range(len(text)):
        lcd.clear()
        lcd.print(text[i:i+16])
        sleep_ms(400)

    lcd.clear()
    lcd.set_cursor(0,0)
    lcd.print("Press b")

    while True: 
        buttons_state_changed = buttons.update()
        # LANGSAMER Autoscroll
        for i in range(len(text)):
            lcd.clear()
            lcd.print(text[i:i+16])
            sleep_ms(400)

        if(buttons_state_changed):    
            led_b_status = buttons.is_pressed(1) # Turn LED B on if button B is pressed
            buttons.set_led_status(False, True, False)

        while led_b_status == True:
            lcd.clear()
            lcd.set_cursor(8, 0)
            lcd.print("5")
            sleep_ms(1000)
            lcd.print("4")
            sleep_ms(1000)
            lcd.print("3")
            sleep_ms(1000)
            lcd.print("2")
            sleep_ms(1000)
            lcd.print("1")
            sleep_ms(1000)
            lcd.print("0")
            sleep_ms(250)
            lcd.clear()

      
Hide_and_Seek()