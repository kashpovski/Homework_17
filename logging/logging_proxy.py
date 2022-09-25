import time

from browsermobproxy import Server, Client

server = Server(r"D:\Mars\QA\OTUS\lesson_17\Homework_17\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat",
                    {"port": 8082})
server.start()
# client = Client("localhost:8082")
# server.create_proxy()
# request.addfinalizer(server.stop)
# client.new_har() #Архив сетевой активнти браузера (список словарей)
# return client
time.sleep(30)
server.stop()
