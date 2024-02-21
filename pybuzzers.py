import machine
import time
class Music:
    def __init__(self, bpm=0, vol=0, pin=0):  #at initialization, enter the BPM for the song, the volume the buzzer should be at, and the GPIO pin number
        self.t = 60/bpm
        self.v = vol
        self.pin = machine.PWM(machine.Pin(corr))
        self.pin.duty_u16(self.v)
    def rest(self, beats):  #the rest of the commands just need a value for how long a note should be held
        self.pin.duty_u16(0)
        time.sleep(self.t*beats)
        self.pin.duty_u16(self.v)
    def c0(self, beats):
        self.pin.freq(16)
        time.sleep(self.t*beats)
    def cs0(self, beats):
        self.pin.freq(17)
        time.sleep(self.t*beats)
    def d0(self, beats):
        self.pin.freq(18)
        time.sleep(self.t*beats)
    def ds0(self, beats):
        self.pin.freq(19)
        time.sleep(self.t*beats)
    def e0(self, beats):
        self.pin.freq(21)
        time.sleep(self.t*beats)
    def f0(self, beats):
        self.pin.freq(22)
        time.sleep(self.t*beats)
    def fs0(self, beats):
        self.pin.freq(23)
        time.sleep(self.t*beats)
    def g0(self, beats):
        self.pin.freq(25)
        time.sleep(self.t*beats)
    def gs0(self, beats):
        self.pin.freq(26)
        time.sleep(self.t*beats)
    def a0(self, beats):
        self.pin.freq(28)
        time.sleep(self.t*beats)
    def as0(self, beats):
        self.pin.freq(29)
        time.sleep(self.t*beats)
    def b0(self, beats):
        self.pin.freq(31)
        time.sleep(self.t*beats)
    def c1(self, beats):
        self.pin.freq(33)
        time.sleep(self.t*beats)
    def cs1(self, beats):
        self.pin.freq(35)
        time.sleep(self.t*beats)
    def d1(self, beats):
        self.pin.freq(37)
        time.sleep(self.t*beats)
    def ds1(self, beats):
        self.pin.freq(39)
        time.sleep(self.t*beats)
    def e1(self, beats):
        self.pin.freq(41)
        time.sleep(self.t*beats)
    def f1(self, beats):
        self.pin.freq(44)
        time.sleep(self.t*beats)
    def fs1(self, beats):
        self.pin.freq(46)
        time.sleep(self.t*beats)
    def g1(self, beats):
        self.pin.freq(49)
        time.sleep(self.t*beats)
    def gs1(self, beats):
        self.pin.freq(52)
        time.sleep(self.t*beats)
    def a1(self, beats):
        self.pin.freq(55)
        time.sleep(self.t*beats)
    def as1(self, beats):
        self.pin.freq(58)
        time.sleep(self.t*beats)
    def b1(self, beats):
        self.pin.freq(62)
        time.sleep(self.t*beats)
    def c2(self, beats):
        self.pin.freq(65)
        time.sleep(self.t*beats)
    def cs2(self, beats):
        self.pin.freq(69)
        time.sleep(self.t*beats)
    def d2(self, beats):
        self.pin.freq(73)
        time.sleep(self.t*beats)
    def ds2(self, beats):
        self.pin.freq(78)
        time.sleep(self.t*beats)
    def e2(self, beats):
        self.pin.freq(82)
        time.sleep(self.t*beats)
    def f2(self, beats):
        self.pin.freq(87)
        time.sleep(self.t*beats)
    def fs2(self, beats):
        self.pin.freq(93)
        time.sleep(self.t*beats)
    def g2(self, beats):
        self.pin.freq(98)
        time.sleep(self.t*beats)
    def gs2(self, beats):
        self.pin.freq(104)
        time.sleep(self.t*beats)
    def a2(self, beats):
        self.pin.freq(110)
        time.sleep(self.t*beats)
    def as2(self, beats):
        self.pin.freq(117)
        time.sleep(self.t*beats)
    def b2(self, beats):
        self.pin.freq(123)
        time.sleep(self.t*beats)
    def c3(self, beats):
        self.pin.freq(131)
        time.sleep(self.t*beats)
    def cs3(self, beats):
        self.pin.freq(139)
        time.sleep(self.t*beats)
    def d3(self, beats):
        self.pin.freq(146)
        time.sleep(self.t*beats)
    def ds3(self, beats):
        self.pin.freq(156)
        time.sleep(self.t*beats)
    def e3(self, beats):
        self.pin.freq(165)
        time.sleep(self.t*beats)
    def f3(self, beats):
        self.pin.freq(175)
        time.sleep(self.t*beats)
    def fs3(self, beats):
        self.pin.freq(185)
        time.sleep(self.t*beats)
    def g3(self, beats):
        self.pin.freq(196)
        time.sleep(self.t*beats)
    def gs3(self, beats):
        self.pin.freq(208)
        time.sleep(self.t*beats)
    def a3(self, beats):
        self.pin.freq(220)
        time.sleep(self.t*beats)
    def as3(self, beats):
        self.pin.freq(233)
        time.sleep(self.t*beats)
    def b3(self, beats):
        self.pin.freq(246)
        time.sleep(self.t*beats)
    def c4(self, beats):
        self.pin.freq(262)
        time.sleep(self.t*beats)
    def cs4(self, beats):
        self.pin.freq(277)
        time.sleep(self.t*beats)
    def d4(self, beats):
        self.pin.freq(294)
        time.sleep(self.t*beats)
    def ds4(self, beats):
        self.pin.freq(311)
        time.sleep(self.t*beats)
    def e4(self, beats):
        self.pin.freq(330)
        time.sleep(self.t*beats)
    def f4(self, beats):
        self.pin.freq(349)
        time.sleep(self.t*beats)
    def fs4(self, beats):
        self.pin.freq(370)
        time.sleep(self.t*beats)
    def g4(self, beats):
        self.pin.freq(392)
        time.sleep(self.t*beats)
    def gs4(self, beats):
        self.pin.freq(415)
        time.sleep(self.t*beats)
    def a4(self, beats):
        self.pin.freq(440)
        time.sleep(self.t*beats)
    def as4(self, beats):
        self.pin.freq(466)
        time.sleep(self.t*beats)
    def b4(self, beats):
        self.pin.freq(494)
        time.sleep(self.t*beats)
    def c5(self, beats):
        self.pin.freq(523)
        time.sleep(self.t*beats)
    def cs5(self, beats):
        self.pin.freq(554)
        time.sleep(self.t*beats)
    def d5(self, beats):
        self.pin.freq(587)
        time.sleep(self.t*beats)
    def ds5(self, beats):
        self.pin.freq(622)
        time.sleep(self.t*beats)
    def e5(self, beats):
        self.pin.freq(659)
        time.sleep(self.t*beats)
    def f5(self, beats):
        self.pin.freq(698)
        time.sleep(self.t*beats)
    def fs5(self, beats):
        self.pin.freq(740)
        time.sleep(self.t*beats)
    def g5(self, beats):
        self.pin.freq(784)
        time.sleep(self.t*beats)
    def gs5(self, beats):
        self.pin.freq(831)
        time.sleep(self.t*beats)
    def a5(self, beats):
        self.pin.freq(880)
        time.sleep(self.t*beats)
    def as5(self, beats):
        self.pin.freq(932)
        time.sleep(self.t*beats)
    def b5(self, beats):
        self.pin.freq(988)
        time.sleep(self.t*beats)
    def c6(self, beats):
        self.pin.freq(1047)
        time.sleep(self.t*beats)
    def cs6(self, beats):
        self.pin.freq(1109)
        time.sleep(self.t*beats)
    def d6(self, beats):
        self.pin.freq(1175)
        time.sleep(self.t*beats)
    def ds6(self, beats):
        self.pin.freq(1245)
        time.sleep(self.t*beats)
    def e6(self, beats):
        self.pin.freq(1319)
        time.sleep(self.t*beats)
    def f6(self, beats):
        self.pin.freq(1397)
        time.sleep(self.t*beats)
    def fs6(self, beats):
        self.pin.freq(1480)
        time.sleep(self.t*beats)
    def g6(self, beats):
        self.pin.freq(1568)
        time.sleep(self.t*beats)
    def gs6(self, beats):
        self.pin.freq(1661)
        time.sleep(self.t*beats)
    def a6(self, beats):
        self.pin.freq(1760)
        time.sleep(self.t*beats)
    def as6(self, beats):
        self.pin.freq(1865)
        time.sleep(self.t*beats)
    def b6(self, beats):
        self.pin.freq(1975)
        time.sleep(self.t*beats)
    def c7(self, beats):
        self.pin.freq(2093)
        time.sleep(self.t*beats)
    def cs7(self, beats):
        self.pin.freq(2217)
        time.sleep(self.t*beats)
    def d7(self, beats):
        self.pin.freq(2349)
        time.sleep(self.t*beats)
    def ds7(self, beats):
        self.pin.freq(2489)
        time.sleep(self.t*beats)
    def e7(self, beats):
        self.pin.freq(2637)
        time.sleep(self.t*beats)
    def f7(self, beats):
        self.pin.freq(2794)
        time.sleep(self.t*beats)
    def fs7(self, beats):
        self.pin.freq(2960)
        time.sleep(self.t*beats)
    def g7(self, beats):
        self.pin.freq(3136)
        time.sleep(self.t*beats)
    def gs7(self, beats):
        self.pin.freq(3322)
        time.sleep(self.t*beats)
    def a7(self, beats):
        self.pin.freq(3520)
        time.sleep(self.t*beats)
    def as7(self, beats):
        self.pin.freq(3729)
        time.sleep(self.t*beats)
    def b7(self, beats):
        self.pin.freq(3951)
        time.sleep(self.t*beats)
    def c8(self, beats):
        self.pin.freq(4186)
        time.sleep(self.t*beats)
    def cs8(self, beats):
        self.pin.freq(4435)
        time.sleep(self.t*beats)
    def d8(self, beats):
        self.pin.freq(4699)
        time.sleep(self.t*beats)
    def ds8(self, beats):
        self.pin.freq(4978)
        time.sleep(self.t*beats)
    def e8(self, beats):
        self.pin.freq(5274)
        time.sleep(self.t*beats)
    def f8(self, beats):
        self.pin.freq(5588)
        time.sleep(self.t*beats)
    def fs8(self, beats):
        self.pin.freq(5920)
        time.sleep(self.t*beats)
    def g8(self, beats):
        self.pin.freq(6272)
        time.sleep(self.t*beats)
    def gs8(self, beats):
        self.pin.freq(6645)
        time.sleep(self.t*beats)
    def a8(self, beats):
        self.pin.freq(7040)
        time.sleep(self.t*beats)
    def as8(self, beats):
        self.pin.freq(7459)
        time.sleep(self.t*beats)
    def b8(self, beats):
        self.pin.freq(7902)
        time.sleep(self.t*beats)
    def stop(self):
        self.pin.deinit()
    

        
