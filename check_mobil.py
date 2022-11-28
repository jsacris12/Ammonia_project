T = ['428','438','448','458','468','478','488','498','508','518','K']
import matplotlib.pyplot as plt
import numpy as np
import math
M_list = []
for iz in range(len(T)):
  MSD = [[],[],[],[],[]]
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
  for it in range(5):
    
    timestep = []
    
    count = 0
    place = 0
    if it == 0:
      with open('test_428.lammpstrj', 'r') as f:
        lines = f.readlines()
        for line in lines:
          l = line.split(' ')
          #print(l)
          if len(l) == 13:
            if l[1] == '2':
              #print(1)
              Ox.append(float(l[2]))
              Oy.append(float(l[3]))
              Oz.append(float(l[4]))
              Ox_h.append(float(l[2]))
              Oy_h.append(float(l[3]))
              Oz_h.append(float(l[4]))
              count += 1 
            elif l[1] == '1':
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
          if count == 84:
            Ox_w.append(sum(Ox_h)/len(Ox_h))
            Ox_h = []
            Oy_w.append(sum(Oy_h)/len(Oy_h))
            Oy_h = []
            Oz_w.append(sum(Oz_h)/len(Oz_h))
            Oz_h = []
            count = 0
          
    if it > 0:
      no = str(it + 1)
      
      with open('test_428' + '_' + no + '.lammpstrj', 'r') as f:

        lines = f.readlines()
        for line in lines:
          l = line.split(' ')
          #print(l)
          if len(l) == 13:
            if l[1] == '2':
              #print(1)
              Ox.append(float(l[2]))
              Oy.append(float(l[3]))
              Oz.append(float(l[4]))
              Ox_h.append(float(l[2]))
              Oy_h.append(float(l[3]))
              Oz_h.append(float(l[4]))
              count += 1
            elif l[1] == '1':
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
          if count == 84:
            Ox_w.append(sum(Ox_h)/len(Ox_h))
            Ox_h = []
            Oy_w.append(sum(Oy_h)/len(Oy_h))
            Oy_h = []
            Oz_w.append(sum(Oz_h)/len(Oz_h))
            Oz_h = []
            count = 0

  h = np.array([math.floor(5*NH3x[0]),math.floor(5*NH3y[0]),math.floor(5*NH3z[0])])
  hold = []
  hold.append(h)
  c = 1


  for i in range(1,len(NH3x)):
    rel = np.array([math.floor(5*NH3x[i]),math.floor(5*NH3y[i]),math.floor(5*NH3z[i])])
    c = 1
    for h in range(len(hold)):
      if np.array_equal(rel,hold[h]):
        c = 0
        break
      
    if c == 1:
      hold.append(rel)
    


  print(T[iz])
  print(len(hold))
  n = 27 * 24 * 18
  mobil = len(hold)/n
  print(mobil)
  