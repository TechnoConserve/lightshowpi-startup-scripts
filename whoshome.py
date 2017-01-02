#!/usr/bin/python

import bluetooth
import time
import os
import datetime

start = datetime.time(9, 00)
end = datetime.time(21, 30)
partytime = False

while True:
    now = datetime.datetime.now().time()
    day = datetime.datetime.now().weekday()
    print("The time is: " + str(now))

    # If it is a weekday where Monday = 0; Sunday = 6
    if start <= now <= end or partytime:
        print("Checking if my master is within range...")
        try:
            result = bluetooth.lookup_name('24:4B:81:1F:33:E4', timeout=5)
            print("Result: ", result)

            if result is not None or partytime:
                print ("...he's here...Muahahahahaha")
                os.system("python ~/RPi-LPD8806/party.py")
            else:
                print("No one home. A pity.")
                time.sleep(10)

        except bluetooth.btcommon.BluetoothError as error:
            print("Could not connect: {}. Retrying in 30 seconds.".format(error))
            time.sleep(30)

    else:
        os.system("python ~/RPi-LPD8806/off.py")
        time.sleep(10)
