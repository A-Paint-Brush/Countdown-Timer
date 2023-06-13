import tkinter
import Ringtone
import Timer_Settings


class Startpage:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Settings")
        self.window.geometry("400x400")
        self.window.maxsize(400, 400)
        self.window.minsize(400, 400)
        self.timer = tkinter.Label(self.window, text="00:00:00", font=("TkDefaultFont", 30, "normal"))
        self.timer.pack()
        self.set_time = tkinter.Button(self.window, text="Set Time", command=self.set_time)
        self.set_time.pack()
        self.Ringtone = tkinter.Button(self.window, text="Change Ringtone", command=self.set_ringtone)
        self.Ringtone.pack()
        self.window.mainloop()

    def set_time(self):
        self.window.destroy()
        Timer_Settings.Settings()

    def set_ringtone(self):
        self.window.destroy()
        Ringtone.Ringtone()
