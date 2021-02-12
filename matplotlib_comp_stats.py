# Imports
import os
import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Parameters
time_frame = 50
temp_range = [40, 60]
time_interval = 2
#ram_limit = 


# Create figure
fig, (ax_temp, ax_ram, ax_cpu) = plt.subplots(3)
fig.tight_layout()
ax_temp.set_ylim(temp_range)
ax_temp.set_xlim(time_frame, 0)
ax_ram.set_ylim(0, 4)
ax_ram.set_xlim(time_frame, 0)
ax_cpu.set_ylim(0, 100)
ax_cpu.set_xlim(time_frame, 0)


# Add labels
plt.xlabel('Seconds ago')
ax_temp.set_title('Temperature', loc='left')
ax_temp.set(ylabel='Temp (deg C)')
ax_ram.set_title('RAM', loc='left')
ax_ram.set(ylabel='RAM (GB)')
ax_cpu.set_title('CPU', loc='left')
ax_cpu.set(ylabel='CPU (%)')

for ax in fig.get_axes():
    ax.label_outer()


# Initialise variables
times = list(range(time_frame * time_interval, 0, -time_interval))  # (x_len * time_interval), 0, -(x_len / 10)
temps = [0] * time_frame
rams = [0] * time_frame
cpus = [0] * time_frame


# Initialise lines
temp_line, = ax_temp.plot(times, temps)
ram_line, = ax_ram.plot(times, rams)
cpu_line, = ax_cpu.plot(times, cpus)


# Measurement functions
def measure_temp():
    temp = os.popen('vcgencmd measure_temp').readline()
    return float(temp[temp.index('=') + 1:temp.rindex("'")])

def measure_ram():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return round(int(line.split()[2]) / 1000 ** 2, 2)

def measure_cpu():
    return psutil.cpu_percent()


# Animate functions
def animate_temp(self, temps):
    temp_c = measure_temp()
    temps.append(temp_c)
    temps = temps[-time_frame:]
    temp_line.set_ydata(temps)
    return temp_line,

def animate_ram(self, rams):
    ram = measure_ram()
    rams.append(ram)
    rams = rams[-time_frame:]
    ram_line.set_ydata(rams)
    return ram_line,

def animate_cpu(self, cpus):
    cpu = measure_cpu()
    cpus.append(cpu)
    cpus = cpus[-time_frame:]
    cpu_line.set_ydata(cpus)
    return cpu_line,


# Set up plot to call animate() function periodically
ani_temp = animation.FuncAnimation(
    fig,
    animate_temp,
    fargs=(temps,),
    interval=(time_interval * 1000),
    blit=True
)

ani_ram = animation.FuncAnimation(
    fig,
    animate_ram,
    fargs=(rams,),
    interval=(time_interval * 1000),
    blit=True
)

ani_cpu = animation.FuncAnimation(
    fig,
    animate_cpu,
    fargs=(cpus,),
    interval=(time_interval * 1000),
    blit=True
)


plt.show()