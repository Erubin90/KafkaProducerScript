from TenThread import TenThread


class MasterThread:
    count = 0
    thread_name = 0

    def __init__(self, count, name):
        self.count = count
        self.thread_name = name

    def run(self):
        thread1 = TenThread("Thread", 1, self.count)
        thread2 = TenThread("Thread", 2, self.count)
        thread3 = TenThread("Thread", 3, self.count)
        thread4 = TenThread("Thread", 4, self.count)
        thread5 = TenThread("Thread", 5, self.count)
        thread6 = TenThread("Thread", 6, self.count)
        thread7 = TenThread("Thread", 7, self.count)
        thread8 = TenThread("Thread", 8, self.count)
        thread9 = TenThread("Thread", 9, self.count)
        thread10 = TenThread("Thread", 10, self.count)

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
        thread6.start()
        thread7.start()
        thread8.start()
        thread9.start()
        thread10.start()
