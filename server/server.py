import zerorpc
import dymax

class HelloRPC(object):
    def hello(self, name):
        return "Hello, %s" % name

s = zerorpc.Server(dymax)
s.bind("tcp://0.0.0.0:4242")
s.run()