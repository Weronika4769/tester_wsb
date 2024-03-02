import os
import subprocess
import time

#subprocess.run(['tracert 8.8.8.8 > tracert_result.txt'])
time_start_1 = time.time() #zwraca czas w epoce unixa
os.system('cmd "tracert 8.8.8.8 > tracert-result.txt"')
time_start_2 = time.time()
print (time_start_2 - time_start_1)
print('tracert-result.txt')
