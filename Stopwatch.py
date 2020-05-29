import time
start = input('To start timer type "start"')
time1 = time.time()
end = input('To stop the timer type "stop"')
time2 = time.time()
time3 = time2 - time1

print('%s' % time3)

