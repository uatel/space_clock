from m5stack import touch, lv
rootLoading = lv.obj()
label = lv.label(rootLoading)
label.align(rootLoading,lv.ALIGN.CENTER, -20, 0)
label.set_text('Loading...')
lv.disp_load_scr(rootLoading)
from uiflow import wait
wait(0.01)
import os, sys, time
run,touched_time,touched_cord,protect_mode=True,0,[0,0],False
while run:
    if touch.status():
    if touched_time==0: touched_time,touched_cord=time.ticks_ms(),touch.read()
    elif (touch.read()[1]) > 240:
      if touched_time!=-1:
        if time.ticks_ms()-touched_time>250:
          if distance(touched_cord,touch.read())<3:
            touched_time=-1
            if (touch.read()[0])<315 and (touch.read()[0])>225:
              vibrating()
              if not protect_mode: run=False
              else:
                protect_mode,rootLoading=False,lv.obj()
                label = lv.label(rootLoading)
                label.set_text('Loading...')
                label.align(rootLoading,lv.ALIGN.CENTER, 0, 0)
                label_close = lv.label(root)
                label_close.set_pos(238,220)
                label_close.add_style(lv.label.PART.MAIN, label_shadow_style)
                label_close.set_text(lv.SYMBOL.CLOSE+" close")
                lv.disp_load_scr(root)
  else touched_time!=0: touched_time=0
wait(0.1)
label.set_text('')
lv.disp_load_scr(rootLoading)






















from m5stack import *
from m5stack_ui import *
from uiflow import *
from easyIO import *


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x000000)






bar0 = M5Bar(x=245, y=224, w=70, h=12, min=0, max=100, bg_c=0xa0a0a0, color=0x068eff, parent=None)


bar0.set_value((power.getBatPercent()))
power.setBusPowerMode(0)
power.setChargeCurrent(power.CURRENT_100MA)
