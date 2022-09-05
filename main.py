import sys
from MasterThread import MasterThread


count_thread_master = int(sys.argv[2])
count = int(sys.argv[1]) / count_thread_master / 10
print("Counter per thread is ", count)

i = 0
while i < count_thread_master:
    i = i + 1
    thread_master = MasterThread(count, i)
    thread_master.run()
print("Threads running!")
