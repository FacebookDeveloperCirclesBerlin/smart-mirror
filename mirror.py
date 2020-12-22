import os

from window import MirrorDisplay
from dotenv import load_dotenv

load_dotenv()

display = MirrorDisplay()
display.setup_wigets(os.getenv('FIRSTNAME'))
display.loop()
