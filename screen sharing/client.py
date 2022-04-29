from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient('localhost',9999)
x=threading.Thread(target=sender.start_stream)
x.start()
while input("") != 'STOP':
    continue
    servr.stop_server()