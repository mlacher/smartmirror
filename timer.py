import schedule
import time

def switch_on(t):
    print ("Display On", t)
    return

def switch_off(t):
    print ("Display Off", t)
    return


schedule.every().day.at("06:30").do(switch_on,'display is on')
schedule.every().day.at("09:30").do(switch_on,'display is off')
schedule.every().day.at("16:30").do(switch_on,'display is on')
schedule.every().day.at("22:30").do(switch_on,'display is off')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
