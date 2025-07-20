from Path import get_path
import tkinter
import Timer
import pygame.mixer
import math
import win10toast


class TimerView:
    def __init__(self, hours, minutes, seconds, ring_tone_dir):
        pygame.mixer.init()
        self.timerRun = False
        self.timer_start = False
        self.secs = 1
        self.delay = 0
        self.remaining_secs = hours * 3600 + minutes * 60 + seconds + 1
        self.hours = str(hours)
        self.minutes = str(minutes)
        self.seconds = str(seconds)
        self.ring_tone_dir = ring_tone_dir
        self.toast = win10toast.ToastNotifier()
        if len(self.hours) < 2:
            self.hours = "0" + self.hours
        if len(self.minutes) < 2:
            self.minutes = "0" + self.minutes
        if len(self.seconds) < 2:
            self.seconds = "0" + self.seconds
        self.window = tkinter.Tk()
        self.window.title("Countdown Timer")
        self.window.geometry("400x400")
        self.window.maxsize(400, 400)
        self.window.minsize(400, 400)
        self.timer = tkinter.Label(self.window, text=self.hours + ":" + self.minutes + ":" + self.seconds,
                                   font=("TkDefaultFont", 30, "normal"))
        self.timer.pack()
        self.btn = tkinter.Button(self.window, text="Start", command=self.start)
        self.btn.pack()
        self.window.mainloop()
        if pygame.mixer.get_busy():
            self.sound.stop()

    def start(self):
        if not self.timer_start:
            self.counter = Timer.Timer()
            self.counter.reset()
            self.timer_start = True
            self.timerRun = True
            self.btn.config(text="Stop", command=self.stop)
            self.loop()
            return None
        self.delay = self.delay + (self.counter.get_time() - self.stop_time)
        self.timerRun = True
        self.btn.config(text="Stop", command=self.stop)

    def loop(self):
        self.hours = int(self.hours)
        self.minutes = int(self.minutes)
        self.secs = int(self.secs)
        if self.timerRun:
            self.second_difference = (self.remaining_secs - self.counter.get_time()) + self.delay
            self.hours = math.floor(self.second_difference // 3600)
            self.minutes = math.floor((self.second_difference % 3600) // 60)
            self.secs = math.floor((self.second_difference % 3600) % 60)
            self.hours = str(self.hours)
            self.minutes = str(self.minutes)
            self.secs = str(self.secs)
            self.length()
            self.timer.config(text=self.hours + ":" + self.minutes + ":" + self.secs)
        if self.hours == "00" and self.minutes == "00" and self.secs == "00":
            self.ring_tone()
            return None
        self.window.after(1, self.loop)

    def stop(self):
        self.timerRun = False
        self.stop_time = self.counter.get_time()
        self.btn.config(text="Start", command=self.start)

    def length(self):
        if len(self.hours) < 2:
            self.hours = "0" + self.hours
        if len(self.minutes) < 2:
            self.minutes = "0" + self.minutes
        if len(self.secs) < 2:
            self.secs = "0" + self.secs

    def ring_tone(self):
        self.btn.destroy()
        self.done = tkinter.Button(self.window, text="Exit", command=self.stop_ring_tone)
        self.done.pack()
        self.toast.show_toast(
            "Countdown Timer", "Time's up!",
            icon_path=get_path("Images/python.ico"),
            duration=10, threaded=True
        )
        self.sound = pygame.mixer.Sound(self.ring_tone_dir)
        self.sound.play(-1)

    def stop_ring_tone(self):
        self.sound.stop()
        self.window.destroy()
