from machine import Pin, SPI
from st7789_170x320 import *
from time import sleep
 

spi = SPI(1, baudrate=40000000, sck=Pin(4), mosi=Pin(3), miso=None)

reset = Pin(2, Pin.OUT)
cs    = Pin(0, Pin.OUT)
dc    = Pin(1, Pin.OUT)
bl    = Pin(5, Pin.OUT)

st = ST7789(spi, cs, dc, reset, bl, height=320, width=120, disp_mode=0)

colors = (RED, GREEN, CYAN, MAGENTA, YELLOW, ORANGE, WHITE, BLUE, BLACK)

for c in colors:
    st.clear(c)
    sleep(1)

st.clear()
st.rect(20, 20, 130, 280, WHITE)
sleep(0.5)
st.rect(40, 40, 90, 240, YELLOW)
sleep(0.5)
st.rect(60, 60, 50, 200, GREEN)
sleep(0.5)
st.fill_rect(80, 80, 10, 160, RED)
sleep(2)

st.clear()
import vga1_8x8 as font
st.text(font, '8x8', 10, 10, WHITE)
sleep(0.5)
import vga1_8x16 as font
st.text(font, '8x16', 10, 35, CYAN)
sleep(0.5)
import vga1_16x16 as font
st.text(font, '16x16', 10, 60, RED)
sleep(0.5)
import vga1_16x32 as font
st.text(font, '16x32', 10, 85, GREEN)
sleep(0.5)
import vga1_bold_16x16 as font
st.text(font, 'bold_16x16', 10, 120, YELLOW)
sleep(0.5)
import vga1_bold_16x32 as font
st.text(font, 'bold_16x32', 10, 145, MAGENTA)
sleep(3)

st.clear()
import vga1_bold_16x16 as font
for mode in range(0,8,2):
    st.mode = mode
    st.set_frame()
    st.text(font, 'mode='+str(mode), 10, 10, colors[mode])
    sleep(0.5)