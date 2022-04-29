from vidstream import StreamingServer
import threading
servr= StreamingServer('localhost',9999)
x=threading.Thread(target=servr.start_server)
x.start()
while input("") != 'STOP':
    continue

    servr.stop_server()