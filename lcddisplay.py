#!/usr/bin/python

import time 

import Adafruit_CharLCD as LCD 

#lcd_rs = 26
#lcd_en = 19
#lcd_d4 = 13
#lcd_d5 = 6
#lcd_d6 = 5 
#lcd_d7 = 11


#lcd_rs,lcd_en,lcd_d4,lcd_d5,lcd_d5,lcd_d6,lcd_d7,cols,rows,GPIO=None

lcd = LCD.Adafruit_CharLCD(26,19,13,6,5,11,7,2,None)

lcd.clear()

#lcd.show_cursor(True)

message = 'Scroll'
lcd.message(message)

for i in range(16-len(message)):
    time.sleep(0.5)
    lcd.move_right()
for i in range(16-len(message)):
    time.sleep(0.5)
    lcd.move_left()


lcd.clear()






