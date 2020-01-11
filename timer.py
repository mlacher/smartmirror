import schedule
import time
import subprocess
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
 
RELAIS_1_GPIO = 17
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen

def switch_on(t):
    print ("Display On", t)
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # aus
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # an
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # aus
    subprocess.call("app.py", shell=True)
    return

def switch_off(t):
    print ("Display Off", t)
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # aus
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # an
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # aus
    return


schedule.every().day.at("06:30").do(switch_on,'display is on')
schedule.every().day.at("09:30").do(switch_on,'display is off')
schedule.every().day.at("17:18").do(switch_on,'display is on')
schedule.every().day.at("22:30").do(switch_on,'display is off')

while True:
    schedule.run_pending()
    time.sleep(30) # wait one minute
