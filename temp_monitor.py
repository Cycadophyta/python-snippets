import os
import time
from guizero import App, Text

def measure_temp():
    temp = os.popen('vcgencmd measure_temp').readline()
    return (temp.replace('temp=', ''))

print(measure_temp())

app = App(title = 'Temp Monitor')
    
message = Text(app, text='Temp Monitor', size=40, color='gray')
temps = Text(app, text = measure_temp())

time.sleep(5)

app.display()