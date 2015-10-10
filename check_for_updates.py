from datetime import datetime
import os, math
def update_check():
    """ Opens a file named 'last_update' which contains the last time of update. If the 
        current time - last_update time is greater than 2 hours, we pull new projections from
        our source.
    """
    time_now = datetime.now()
    last_update = open('last_update', 'r+')
    
    time_now = datetime.now()
    old_time = last_update.readline()
    last_update_time = datetime.strptime(old_time, '%Y %M %d %H')
    string_time = ''
    time_difference  = int(math.floor(((time_now - last_update_time).seconds) / 3600))
    if time_difference > 2:
        os.system('bash download.sh')       
        string_time = str(time_now.year) + ' ' + str(time_now.month) + ' ' + str(time_now.day) + ' ' + str(time_now.hour)
        last_update.close()
        last_update = open('last_update', 'w')
        last_update.write(string_time)
        last_update.close()
        return str(time_now)
    return str(last_update_time)

