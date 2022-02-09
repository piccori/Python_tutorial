import threading
import time
import datetime


# 複数のスレッドにより処理
# class TestThread(threading.Thread):

#     def run(self):
#         print("=== start sub thread ===")
#         for _ in range(5):
#             time.sleep(5)
#             print(' Sub Thread : ' + str(datetime.datetime.today()))
#         print("=== start sub thread ===")


# th = TestThread()
# th.start()

# time.sleep(1)

# print('=== start main thread ===')
# for i in range(5):
#     time.sleep(10)
#     print('main thread : ' + str(datetime.datetime.today()))
# print('=== end main thread ===')


# デーモンスレッド
class TestThread(threading.Thread):

    def run(self):
        print("=== start sub thread ===")
        for _ in range(5):
            time.sleep(5)
            print(' Sub Thread : ' + str(datetime.datetime.today()))
        print("=== start sub thread ===")


th = TestThread()
th.daemon = True
# th.deamon = False
th.start()

time.sleep(1)

print('=== start main thread ===')
for i in range(5):
    time.sleep(10)
    print('main thread : ' + str(datetime.datetime.today()))
print('=== end main thread ===')
