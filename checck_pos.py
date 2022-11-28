import matplotlib.pyplot as plt
import numpy as np
import math
Ox = []
Six = []
NH3x = []
Oy = []
Siy = []
NH3y = []
Oz = []
Siz = []
NH3z = []
H1x = []
H1y = []
H1z = []
H2x = []
H2y = []
H2z = []
H3x = []
H3y = []
H3z = []
Ox_w = []
Ox_h = []
Oy_w = []
Oy_h = []
Oz_w = []
Oz_h = []

timestep = []

MSD = []

place = 0
x = '628_nomin.lammpstrj'
with open(x, 'r') as f:
#with open('init_pos_523K.txt', 'r') as f:
  lines = f.readlines()
  for line in lines:
    l = line.split(' ')
    #print(l)
    if len(l) == 13:
      if l[1] == '1':
        #print(1)
        Ox.append(float(l[2]))
        Oy.append(float(l[3]))
        Oz.append(float(l[4]))
      elif l[1] == '2':
        Six.append(float(l[2]))
        Siy.append(float(l[3]))
        Siz.append(float(l[4]))
      elif l[1] == '3':
        NH3x.append(float(l[2]))
        NH3y.append(float(l[3]))
        NH3z.append(float(l[4]))
      elif l[1] == '4':
        H1x.append(float(l[2]))
        H1y.append(float(l[3]))
        H1z.append(float(l[4]))
      elif l[1] == '5':
        H2x.append(float(l[2]))
        H2y.append(float(l[3]))
        H2z.append(float(l[4]))
      elif l[1] == '6':
        H3x.append(float(l[2]))
        H3y.append(float(l[3]))
        H3z.append(float(l[4]))
    if place == 1:
      timestep.append(int(line))
      place = 0
    if len(l) == 2 and l[1] == 'TIMESTEP\n': 
      place = 1



ax = plt.axes(projection ='3d')
ax.plot3D(Ox,Oy,Oz, linestyle = ' ',marker = 'o', color = 'r') 
ax.plot3D(Six,Siy,Siz, linestyle = ' ',marker = 'o', color = 'g')
ax.plot3D(NH3x,NH3y,NH3z, linestyle = ' ',marker = 'o', color = 'b')
#ax.plot3D(H1x,H1y,H1z, linestyle = ' ',marker = 'o', color = 'y')
#ax.plot3D(H2x,H2y,H2z, linestyle = ' ',marker = 'o', color = 'y')
#ax.plot3D(H3x,H3y,H3z, linestyle = ' ',marker = 'o', color = 'y')

plt.show()
NH3x = np.array(NH3x) - NH3x[0]
NH3y = np.array(NH3y) - NH3y[0]
NH3z = np.array(NH3z) - NH3z[0]
H1x = np.array(H1x) - H1x[0]
H1y = np.array(H1y) - H1y[0]
H1z = np.array(H1z) - H1z[0]
H2x = np.array(H2x) - H2x[0]
H2y = np.array(H2y) - H2y[0]
H2z = np.array(H2z) - H2z[0]
H3x = np.array(H3x) - H3x[0]
H3y = np.array(H3y) - H3y[0]
H3z = np.array(H3z) - H3z[0]

np.delete(NH3x,0)
np.delete(NH3y,0)
np.delete(NH3z,0)
np.delete(H1x,0)
np.delete(H1y,0)
np.delete(H1z,0)
np.delete(H3x,0)
np.delete(H3y,0)
np.delete(H3z,0)
np.delete(H2x,0)
np.delete(H2y,0)
np.delete(H2z,0)


timestep = np.array(timestep)



for i in range(len(NH3x)):
  dotN = np.dot([NH3x[i],NH3y[i],NH3z[i]],[NH3x[i],NH3y[i],NH3z[i]])
  #dotH1 = np.dot([H1x[i],H1y[i],H1z[i]],[H1x[i],H1y[i],H1z[i]])
  #dotH2 = np.dot([H2x[i],H2y[i],H2z[i]],[H2x[i],H2y[i],H2z[i]])
  #dotH3 = np.dot([H3x[i],H3y[i],H3z[i]],[H3x[i],H3y[i],H3z[i]])
  #summ = ((dotN + dotH1 + dotH2 + dotH3)*1*(10**-16))
  summ = ((dotN )*1*(10**-16))
  MSD.append(summ)
a,b = np.polyfit(timestep,MSD,1)
plt.scatter(timestep,MSD)
plt.plot(timestep,a*timestep+b)
plt.show()
print('T = ', x)
print(a) 


