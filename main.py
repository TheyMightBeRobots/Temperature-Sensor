import rainbowhat as sh
import asyncio
import time

async def load():
  for pixel in range(7):
    rh.rainbow.clear()
    rh.rainbow.set_pixel(pixel,255,255,255)
    rh.rainbow.show()
    time.sleep(0.1)

async def song():
  song = [68,68,69,69,70,70,71,71]
  for note in song:
    rh.buzzer.midi_note(note,.5)
    time.sleep(1)

  rh.buzzer.midi_note(40,2)

song()
time.sleep(9.3)
load()

temp = rh.weather.temperature()

while True:
  rh.temperature.update()
  rh.display.clear()
  rh.display.print_float(temp)
  rh.display.show()
  time.sleep(.5)
