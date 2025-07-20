from Path import get_path
import tkinter
import tkinter.messagebox
import pygame.mixer
from functools import partial
import Startpage


class Ringtone:
    def __init__(self):
        pygame.mixer.init()
        self.Ringtone_dir = ""
        self.Ringtone_num = None
        self.Ringtones = ["Chill",
                          "Bossa Nova",
                          "Buzz Whir",
                          "Alert",
                          "Classical Piano",
                          "Dance Around",
                          "Dance Celebrate",
                          "Dance Energetic",
                          "Dance Slow Mo",
                          "Movie 2",
                          "Ring Tone",
                          "Windows 10 Alarm"]
        self.window = tkinter.Tk()
        self.window.title("Ringtone Settings")
        self.window.geometry("400x400")
        self.window.maxsize(400, 400)
        self.window.minsize(400, 400)
        self.ContentFrame = tkinter.Frame(self.window, width="400", height="370")
        self.ContentFrame.pack()
        self.play_buttons = []
        self.set_buttons = []
        for i in range(0, len(self.Ringtones)):
            tkinter.Label(self.ContentFrame, text=self.Ringtones[i]).place(x=10, y=25 * i)
            self.set_buttons.append(tkinter.Button(self.ContentFrame, text="Set As Ringtone",
                                                   command=partial(self.set, i)))
            self.set_buttons[i].place(x=170, y=25 * i)
            self.play_buttons.append(tkinter.Button(self.ContentFrame, text="Play Ringtone",
                                                    command=partial(self.play_ringtone, i)))
            self.play_buttons[i].place(x=300, y=25 * i)
        self.submit = tkinter.Button(self.window, text="Apply", command=self.submit)
        self.submit.pack()
        self.window.mainloop()

    def submit(self):
        if self.Ringtone_dir == "":
            tkinter.messagebox.showerror("Error", "You did not select a ringtone.")
        else:
            with open(get_path("Data/Ringtone Data.txt"), "w", encoding="utf8") as file:
                file.write("Ringtone selected:\n" + self.Ringtone_dir)
            if pygame.mixer.get_busy():
                self.window.after_cancel(self.id)
                self.sound.stop()
            pygame.mixer.quit()
            self.window.destroy()
            Startpage.Startpage()

    def set(self, number):
        self.set_buttons[number].config(text="Current Ringtone", state="disabled")
        if self.Ringtone_num is not None:
            self.set_buttons[self.Ringtone_num].config(text="Set As Ringtone", state="normal")
        self.Ringtone_num = number
        self.Ringtone_dir = get_path("Ringtones/%s.wav" % (self.Ringtones[number],))

    def play_ringtone(self, number):
        self.play_buttons[number].config(text="Stop Ringtone", command=partial(self.stop_ringtone, number))
        self.sound = pygame.mixer.Sound(get_path("Ringtones/%s.wav" % (self.Ringtones[number],)))
        for i in range(0, len(self.Ringtones)):
            if i == number:
                continue
            else:
                self.play_buttons[i].config(state="disabled")
        self.sound.play()
        self.number = number
        self.wait()

    def wait(self):
        if not pygame.mixer.get_busy():
            self.stop_ringtone(self.number)
            return None
        self.id = self.window.after(10, self.wait)

    def stop_ringtone(self, number):
        self.play_buttons[number].config(text="Play Ringtone", command=partial(self.play_ringtone, number))
        for i in range(0, len(self.Ringtones)):
            if i == number:
                continue
            else:
                self.play_buttons[i].config(state="normal")
        self.sound.stop()
