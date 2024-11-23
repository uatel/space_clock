try:
  if str(__file__) == "menu/app.py":
    import machine
    fileA = open('/flash/apps/Weather.py', 'rb')
    fileB = open('/flash/main.py', 'wb')
    fileB.write(fileA.read())
    fileA.close()
    fileB.close()
    machine.reset()
except Exception as e:
  print("run weather")
import lvgl as lv
