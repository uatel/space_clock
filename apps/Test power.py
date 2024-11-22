from m5stack import *
from m5stack_ui import *
from uiflow import *
from easyIO import *


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x000000)






bar0 = M5Bar(x=245, y=224, w=70, h=12, min=0, max=100, bg_c=0xa0a0a0, color=0x068eff, parent=None)


if power.getChargeState():
  bar0.set_hidden(True)
else:
  bar0.set_hidden(False)
bar0.set_value((power.getBatPercent()))
power.setBusPowerMode(0)
power.setChargeCurrent(power.CURRENT_100MA)
