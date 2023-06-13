import tkinter
import tkinter.messagebox
import TimerView


class Settings:
    def __init__(self):
        self.ringtone_dir = ""
        self.window = tkinter.Tk()
        self.window.title("Timer Settings")
        self.window.geometry("440x400")
        self.window.maxsize(440, 400)
        self.window.minsize(440, 400)
        self.form()
        self.window.mainloop()

    def form(self):
        self.hours = tkinter.StringVar()
        self.minutes = tkinter.StringVar()
        self.seconds = tkinter.StringVar()
        self.label = tkinter.Label(self.window, text="Please enter the number of hours you want the timer to count "
                                                     "down from:")
        self.label.pack()
        self.entry = tkinter.Entry(self.window, textvariable=self.hours)
        self.entry.pack()
        self.label2 = tkinter.Label(self.window, text="Please enter the number of minutes you want the timer to count "
                                                      "down from:")
        self.label2.pack()
        self.entry2 = tkinter.Entry(self.window, textvariable=self.minutes)
        self.entry2.pack()
        self.label3 = tkinter.Label(self.window, text="Please enter the number of seconds you want the timer to count "
                                                      "down from:")
        self.label3.pack()
        self.entry3 = tkinter.Entry(self.window, textvariable=self.seconds)
        self.entry3.pack()
        self.submit = tkinter.Button(self.window, text="Submit", command=self.set)
        self.submit.pack()

    def set(self):
        try:
            self.hours_value = int(self.entry.get())
            self.minutes_value = int(self.entry2.get())
            self.seconds_value = int(self.entry3.get())
        except ValueError:
            tkinter.messagebox.showerror("Error", "What you entered is not a number, please try again.")
            self.reset()
            return "Error"
        if self.hours_value > 23:
            tkinter.messagebox.showerror("Error", "The number of hours cannot be bigger than 23, please try again.")
            self.reset()
            return "Error"
        elif self.minutes_value > 59 or self.seconds_value > 59:
            tkinter.messagebox.showerror("Error",
                                         "The number of minutes and hours cannot be over 59, please try again.")
            self.reset()
            return "Error"
        elif self.hours_value == 0 and self.minutes_value == 0 and self.seconds_value == 0:
            tkinter.messagebox.showerror("Error", "The number of seconds cannot be zero when the number of hours and "
                                                  "minutes is zero, please try again.")
            self.reset()
            return "Error"
        try:
            with open("Data\\Ringtone Data.txt", "r", encoding="utf8") as file:
                self.ringtone_dir = file.readlines()[1]
        except FileNotFoundError:
            self.ringtone_dir = "Ringtones\\Chill.wav"
        self.window.destroy()
        TimerView.TimerView(self.hours_value, self.minutes_value, self.seconds_value, self.ringtone_dir)
        return "Success"

    def reset(self):
        self.hours.set("")
        self.minutes.set("")
        self.seconds.set("")
