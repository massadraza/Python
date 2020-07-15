import threading

class Massads_iMessage(threading.Thread):
    def run(self): 
        for _ in range(10):
            print(threading.currentThread().getName())

a = Massads_iMessage(name="Type a Message")
b = Massads_iMessage(name="Delievered")
c = Massads_iMessage(name="Read")
a.start
b.start
c.start 

# Learning what threads are and when/why we need to use them.
