import machine
import time
from pybuzzer import Music
buzzer1=Music(147, 10000, 0) #initialize the object
buzzer1.c3(2) 
buzzer1.e3(1)
buzzer1.g3(1)
buzzer1.a3(.9)  #when transitioning notes, it sometimes sounds better to put a small rest
buzzer1.rest(.1)
buzzer1.a3(2)
buzzer1.g3(1)
buzzer1.a3(1.9)
buzzer1.rest(.1)
buzzer1.a3(1)
buzzer1.g3(1)
buzzer1.e3(2)
buzzer1.rest(1)
buzzer1.g3(1)
buzzer1.a3(1.9)
buzzer1.rest(.1)
buzzer1.a3(1)
buzzer1.g3(1)
buzzer1.e3(1)
buzzer1.d3(.9)
buzzer1.rest(.1)
buzzer1.d3(1)
buzzer1.c3(.5)
buzzer1.d3(1)
buzzer1.c3(.5)
buzzer1.e3(1)
buzzer1.d3(.9)
buzzer1.rest(.1)
buzzer1.d3(1)
buzzer1.c3(1)
buzzer1.rest(1)
buzzer1.c3(.4)
buzzer1.rest(.1)
buzzer1.c3(.4)
buzzer1.rest(.1)
buzzer1.c3(.4)
buzzer1.rest(.1)
buzzer1.c3(1.5)
buzzer1.e3(1)
buzzer1.g3(1)
buzzer1.a3(2.9)
buzzer1.rest(.1)
buzzer1.a3(.4)
buzzer1.rest(.1)
buzzer1.a3(2.4)
buzzer1.rest(.1)
buzzer1.a3(1)
buzzer1.g3(1)
buzzer1.e3(2)
buzzer1.rest(1)
buzzer1.g3(.5)
buzzer1.a3(1.9)
buzzer1.rest(.1)
buzzer1.a3(.4)
buzzer1.rest(.1)
buzzer1.a3(1)
buzzer1.g3(1)
buzzer1.e3(2)
buzzer1.d3(1)
buzzer1.c3(.5)
buzzer1.d3(1.5)
buzzer1.c3(.5)
buzzer1.d3(1.4)
buzzer1.rest(.1)
buzzer1.d3(1)
buzzer1.a2(2)
buzzer1.rest(6)
buzzer1.a3(1.9)
buzzer1.rest(.1)
buzzer1.a3(.5)
buzzer1.g3(.4)
buzzer1.rest(.1)
buzzer1.g3(.9)
buzzer1.rest(.1)
buzzer1.e3(.9)
buzzer1.rest(.1)
buzzer1.e3(.9)
buzzer1.rest(.1)
buzzer1.e3(1)
buzzer1.rest(1)
buzzer1.d3(.4)
buzzer1.rest(.1)
buzzer1.d3(.4)
buzzer1.rest(.1)
buzzer1.d3(.4)
buzzer1.rest(.1)
buzzer1.d3(.4)
buzzer1.rest(.1)
buzzer1.d3(.5)
buzzer1.c3(.5)
buzzer1.b2(.5)
buzzer1.c3(.5)
buzzer1.e3(1)
buzzer1.g3(1)
buzzer1.e3(1)
buzzer1.rest(1)
buzzer1.a3(1.9)
buzzer1.rest(.1)
buzzer1.a3(.5)
buzzer1.g3(.4)
buzzer1.rest(.1)
buzzer1.g3(1)
buzzer1.e3(.9)
buzzer1.rest(.1)
buzzer1.e3(.9)
buzzer1.rest(.1)
buzzer1.e3(1)
buzzer1.rest(1)
buzzer1.e3(.9)
buzzer1.rest(.1)
buzzer1.e3(1)
buzzer1.d3(.9)
buzzer1.rest(.1)
buzzer1.d3(.9)
buzzer1.rest(.1)
buzzer1.d3(2)
buzzer1.stop()
