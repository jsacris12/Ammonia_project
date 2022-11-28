import lammps_logfile
import matplotlib.pyplot as plt
import numpy as np


# Edit the path and name of logfile to be read
log = lammps_logfile.File("test.log")

# Edit the strings to get the values you want from the logfile
x = log.get("Step")
y = log.get("TotEng")
'''
log2 = lammps_logfile.File("ethanol_nvt_223.log")

# Edit the strings to get the values you want from the logfile
x2 = log2.get("Step")
y2 = log2.get("TotEng")

log3 = lammps_logfile.File("ethanol_nvt_298.log")

# Edit the strings to get the values you want from the logfile
x3 = log3.get("Step")
y3 = log3.get("TotEng")

log4 = lammps_logfile.File("ethanol_nvt_348.log")

# Edit the strings to get the values you want from the logfile
x4 = log4.get("Step")
y4 = log4.get("TotEng")

fig, ax = plt.subplots(1, 1)
ax.set_xlabel('step')
ax.set_ylabel('TotE 173K')
ax.set_xlim([0, 600000])

fig1, ax1 = plt.subplots(1, 1)
ax1.set_xlabel('step')
ax1.set_ylabel('TotE 223K')
ax1.set_xlim([0, 600000])

fig2, ax2 = plt.subplots(1, 1)
ax2.set_xlabel('step')
ax2.set_ylabel('TotE 298K')
ax2.set_xlim([0, 600000])

fig3, ax3 = plt.subplots(1, 1)
ax3.set_xlabel('step')
ax3.set_ylabel('TotE 348K')
ax3.set_xlim([0, 400000])
'''

plt.plot(x,y)
plt.show()