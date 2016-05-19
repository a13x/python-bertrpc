import bertrpc
import time
service = bertrpc.Service('localhost', 10001, 600)
service.connect()
print service.call().example.adder(102,201)
#time.sleep(4)
print service.call().example.adder(202,404)
#time.sleep(4)
print service.call().example.adder(202,404)
print service.call().dictoid.to_dict("something", "something", "dark side")
options = dict(cache=["validation", "BlaBla"])
#time.sleep(4)
#print service.call(options).dictoid.see(100,200)
service.close()

with bertrpc.Service('localhost', 10001, 600) as svc:
    print svc.call().example.adder(303,606)
    print svc.call().example.adder(202,101)

