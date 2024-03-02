import os
import time
import datetime
import shutil

os.chdir('C:\\Users\\User\\Desktop')

if os.path.exists('./time'):
    shutil.rmtree('time')
    #os.rmdir('time')
os.mkdir('time')
os.chdir('./time')

for i in range(10):
    time_now = datetime.datetime.now() #epoka unixa
    time_now_f = time_now.strftime('%H%M%S')
    f = open(f'report {time_now_f}.txt', 'w')
    f.close()
    time.sleep(3)
