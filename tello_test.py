import sys
import time
from datetime import datetime

from starter.tello.tello import Tello

start_time = str(datetime.now())

tello = Tello()
finish = False

while not finish:
    for line in sys.stdin:
        if line != '' and line != '\n':
            line = line.rstrip()
        if line == "stop":
            finish = True
            break
        if line.find('delay') != -1:
            sec = float(line.partition('delay')[2])
            print('delay %s' % sec)
            time.sleep(sec)
            pass
        else:
            sys.stdout.write(line + "\n")
            sys.stdout.flush()
            tello.send_command(line)

log = tello.get_log()

for stat in log:
    stat.print_stats()
    str = stat.return_stats()
