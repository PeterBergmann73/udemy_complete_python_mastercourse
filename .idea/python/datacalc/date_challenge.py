import time

print("clock:\t\t\t",  time.get_clock_info('clock'))
print("monotonic:\t\t", time.get_clock_info('monotonic'))
print("perf_counter:\t", time.get_clock_info('perf_counter'))
print("process_time:\t", time.get_clock_info('process_time'))
print("time:\t\t\t", time.get_clock_info('time'))