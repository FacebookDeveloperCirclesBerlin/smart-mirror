from tkinter import Frame, Label
import time
from widgets.abstract_widget import AbstractWidget


class MirrorGreeting(AbstractWidget):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.userName = ''
        self.configuration = {}
        self.window = False
        self.greetingDisplay = False

    def set_user_name(self, name):
        """Set up the user name from configuration"""
        self.userName = name

    def mount_widget(self, configuration):
        """ add text to display """
        self.greetingDisplay = Label(self, fg=configuration['text-color'],
                                     bg=configuration['background-color'],
                                     font=(configuration['font'], configuration['medium_text_size']))
        self.update_display()
        self.greetingDisplay.pack()

    def get_greeting_text(self):
        """ get greeting text depending on the time of the day """
        if time.strftime('%p') == 'AM':
            return 'Good morning %s !' % self.userName
        return 'Hello %s !' % self.userName

    def update_display(self):
        """ recursive function to display the updated greetings """
        if isinstance(self.greetingDisplay, Label):
            self.greetingDisplay.config(text=self.get_greeting_text())
            self.greetingDisplay.after(1000, self.update_display)
