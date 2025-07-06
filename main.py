import rainbowhat as rh
import asyncio
import time

async def load():
  for pixel in range(7):
    rh.rainbow.clear()
    rh.rainbow.set_pixel(pixel,255,255,255)
    rh.rainbow.show()
    await asyncio.sleep(0.1)

async def song():
  song = [68,68,69,69,70,70,71,71]
  for note in song:
    rh.buzzer.midi_note(note,.5)
    await asyncio.sleep(1)

  rh.buzzer.midi_note(40,2)

asyncio.run(song())
time.sleep(9.3)
asyncio.run(load())

temp = rh.weather.temperature()

while True:
  rh.weather.update()
  rh.display.clear()
  rh.display.print_float(temp)
  rh.display.show()
  time.sleep(.5)
