from tkinter import Tk, Frame, RIGHT, LEFT, TOP, BOTTOM, BOTH, YES, N, S
from widgets.timer import MirrorTimer
from widgets.greeting import MirrorGreeting
from widgets.weather import Weather


class MirrorDisplay:
    def __init__(self):
        self.configuration = {
            "small_text_size": 18,
            "medium_text_size": 28,
            "large_text_size": 48,
            "xlarge_text_size": 94,
            "font": 'Helvetica',
            "background-color": "black",
            "text-color": "white",
        }

        self.window = Tk()
        self.window.title("Smart Mirror Display")
        self.window.configure(background=self.configuration['background-color'])
        self.widgets = []

        self.state = False
        self.window.bind("<Return>", self.toggle_full_screen)
        self.window.bind("<Escape>", self.end_full_screen)

        # define frames from the window
        self.topFrame = Frame(self.window, background=self.configuration['background-color'])
        self.bottomFrame = Frame(self.window, background=self.configuration['background-color'])
        self.topFrame.pack(side=TOP, fill=BOTH, expand=YES)
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)

    def toggle_full_screen(self, event=None):
        """ put the window in fullscreen """
        self.state = not self.state  # Just toggling the boolean
        self.window.attributes("-fullscreen", self.state)
        return "break"

    def end_full_screen(self, event=None):
        """ escape from fullscreen """
        self.state = False
        self.window.attributes("-fullscreen", False)
        return "break"

    def setup_wigets(self, first_name):
        """ Setup the widgets in the mirror """
        timer = MirrorTimer(self.topFrame, background=self.configuration['background-color'])
        timer.mount_widget(self.configuration)
        timer.pack(side=RIGHT, anchor=N, padx=100, pady=60)

        greeting = MirrorGreeting(self.topFrame, background=self.configuration['background-color'])
        greeting.set_user_name(first_name)
        greeting.mount_widget(self.configuration)
        greeting.pack(side=LEFT, anchor=N, padx=100, pady=60)

        weather = Weather(self.bottomFrame, background=self.configuration['background-color'])
        weather.mount_widget(self.configuration)
        weather.pack(side=LEFT, anchor=S, padx=100, pady=60)

    def loop(self):
        """ Run the loop event """
        self.window.mainloop()
