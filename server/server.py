import zerorpc
import dymax

s = zerorpc.Server(dymax)
s.bind("tcp://0.0.0.0:4242")
s.run()