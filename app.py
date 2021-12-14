import os


import schedule
import time

def job(t):
    print("gone")
    os.system('dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 "org.freedesktop.login1.Manager.Reboot" boolean:true')
    os.system("sudo reboot")
    return

schedule.every().day.at("00:00").do(job,'It is 00:00:00')

while True:
    schedule.run_pending()
    time.sleep(10) # wait one minute
