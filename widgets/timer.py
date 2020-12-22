import time
from tkinter import Label, Frame, TOP, E
from widgets.abstract_widget import AbstractWidget


class MirrorTimer(AbstractWidget):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.dateFormat24 = "%H:%M"
        self.dateFormat12 = "%I:%M %p"
        self.dayFormat = '%a %d %B'
        self.configuration = {}
        self.window = False
        self.timeDisplay = False
        self.dayDisplay = False

    def mount_widget(self, configuration):
        """ add text to display """
        self.timeDisplay = Label(self, fg=configuration['text-color'], bg=configuration['background-color'],
                                 font=(configuration['font'], configuration['xlarge_text_size']))
        self.timeDisplay.pack(side=TOP, anchor=E)

        self.dayDisplay = Label(self, fg=configuration['text-color'], bg=configuration['background-color'],
                                font=(configuration['font'], configuration['medium_text_size']))
        self.dayDisplay.pack(side=TOP, anchor=E)
        self.tick()
        self.update_date()

    def tick(self):
        """ recursive function to display real time """
        if isinstance(self.timeDisplay, Label):
            self.timeDisplay.config(text=time.strftime(self.dateFormat24))
            self.timeDisplay.after(200, self.tick)

    def update_date(self):
        """ recursive function to display the updated day """
        if isinstance(self.dayDisplay, Label):
            self.dayDisplay.config(text=time.strftime(self.dayFormat))
            self.dayDisplay.after(1000, self.update_date)
