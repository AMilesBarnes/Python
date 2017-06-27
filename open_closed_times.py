from datetime import datetime, timedelta
import time
from pytz import timezone

def portland_time():
    los_angeles = timezone('America/Los_Angeles')   
    p_time = datetime.now(los_angeles)
    rel_time_p = p_time.strftime("%a, %d %b %Y %H:%M:%S")
    open_hrs = "%a %d %b %Y 9 00 00"
    closed_hrs = "%a %d %b %Y 21 00 00"  
    ny_time = p_time + timedelta(hours=3)
    rel_time_ny = ny_time.strftime("%H:%M:%S") 
    london_time = p_time + timedelta(hours=8)
    rel_time_london = london_time.strftime(" %Y %H:%M:%S")
    print 'Time in Portland: %s' % (rel_time_p)
    if rel_time_p >= open_hrs:
        print ('HQ is Open')
    elif rel_time_p <= closed_hrs:
        print ('HQ is Closed')   
    if rel_time_ny >= open_hrs:
        print ('New York branch is Open')
    elif rel_time_ny <= closed_hrs:
        print ('New York branch is Closed')    
    if rel_time_london >= open_hrs:
        print ('London branch is Open')
    elif rel_time_london <= closed_hrs:
        print ('London branch is Closed')       

portland_time()


