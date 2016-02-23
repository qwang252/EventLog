import numpy as np
import math
# 1.
def dir(x1,x2):
  if len(x1) != len(x2):
     print("not valid vector")
     return
  dir=[]
  for i in range(len(x1)):
     dir.append(x2[i]-x1[i])
  return dir

def leng(x1,x2):
  dirc=dir(x1,x2)
  if len(x1) != len(x2):
     print("not valid vector")
     return
  leng=0
  for i in range(len(dirc)):
      leng+=dirc[i]*dirc[i]
  leng=math.sqrt(leng)
  return leng

def unitdir(x1,x2):
  length=leng(x1,x2)
  if len(x1) != len(x2):
     print("not valid vector")
     return
  unit=[]
  if length ==0 
     unit=[0 0 0]
     return unit
  for i in range(len(x1)):
     unit.append(float(x2[i]-x1[i])/length)
  return unit

# a. the distance between two vectors 
length=leng([8,1,2],[3,4,5])  
print("the distance is "+str(length))
# b. the unit vector
unit=unitdir([8,1,2],[3,4,5])
print("the unit vector is "+str(unit))
# c. the energy of the particle
#def ene(en):
#  en=en*10e6
#  return en

enr=2.3*10e6
print("energy is "+str(enr)+"ev.")

# 2.
# The best container to store information about an event is dictionary. 
# If tuple is used, the container is fixed and it is very inconvenient 
# to revise the container if there are some mistakes. For example, if 
# the user mistakenly write (7,1,2) instead of (8,1,2), he or she has to 
# reassign the tuple with (8,1,2). But with list, I may just change the 
# wrong index from 7 to 8. If list is used, it is confusing what each index 
# is representing. And it is hard to read which are ID numbers, which are
# energy and etc. So the best choice is to assign each piece of info with 
# its corresponding key name. And list are ideal to store the info of location
# and direction. Tuple is good for atomic type since its size is fixed (2), 
# and the value of atomic number and atomic mass are fixed as well.
 
# example:
ID_num=43 #ID number
loc=[3,4,5] #location of the event
dir=unitdir([8,1,2],loc) #the unit direction of the particle
en=2.3*10e6 #energy as it arrived at the collision
aty=(1,2) #atomic number of D is 1; atomic mass of D is 2
rty=102 #reaction type is 102

event={'ID':ID_num,'location':loc,'unitdir':dir,'eneg':en,'aty':aty,'rty':rty}

# 3.
# List is good to store many events in a log. Since events are represented 
# by their event number, list is convenient to store these event numbers
# Tuple cannot be changed once it is constructed. Therefore it is not handy
# if the user wants to add or remove some events. The dictionary is not 
# good as well since there are just event numbers.

# example:
evenlog=[event,event,event]

# 4. 
# a.

change_en=evenlog[5].get('eneg')-evenlog[4].get('eneg')

# b.

dist=leng(evenlog[6].get('location'),evenlog[7].get('location'))

# c.

z_hat=[0,0,1]
loc1=evenlog[1].get('location')
loc2=evenlog[2].get('location')
norm1=unitdir([0,0,0],loc1)
norm2=unitdir([0,0,0],loc2)
if np.dot(norm1,z_hat) > np.dot(norm2,z_hat):
   print("the more aligned vector is event "+ str(evenlog[3]) )
elif np.dot(norm1,z_hat) == np.dot(norm2,z_hat):
   print("these two events are equally aligned with z-axis.")
else:
   print("the more aligned vector is event "+ str(evenlog[8]))




   





