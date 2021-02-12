import os
import time
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
xs = 20
temp_range = [40, 60]

# Create figure
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_ylim(temp_range)
temps = []
times = []

# Measure temperature
def measure_temp():
    temp = os.popen('vcgencmd measure_temp').readline()
    temp = temp.replace('temp=', '')
    temp = temp.replace('\'C', '')
    return float(temp)

# Animate figure
def animate(i, times, temps):
    times.append(dt.datetime.now().strftime("%H:%M:%S"))
    temps.append(measure_temp())
    
    times = times[-20:]
    temps = temps[-20:]
    
    ax.clear()
    ax.plot(times, temps)
    
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature')
    plt.ylabel('Temperature (deg C)')
    plt.ylim(40, 80)

ani = animation.FuncAnimation(fig,
    animate,
    fargs=(times, temps),
    interval=5000)
plt.show()