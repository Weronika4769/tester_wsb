import os
import time

print(os.getcwd())
os.chdir('C:\\Users\\User\\Desktop')
time.sleep(3)
os.mkdir('tester')
time.sleep(3)
os.rmdir('tester')


