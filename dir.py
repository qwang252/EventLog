import numpy as np
import math
# 1.

def dirc_leng_unit(x1,x2):
  if len(x1) != len(x2):
     print("not valid vector")
     return
  dirc=[]
  leng=0
  for i in range(len(x1)):
     dirc.append(x2[i]-x1[i])
  
  for i in range(len(dirc)):
      leng+=dirc[i]*dirc[i]
  leng=math.sqrt(leng)
  unit=[]
  if leng ==0:
     unit=[0, 0, 0]
     
  else:
     for i in range(len(x1)):
        unit.append(float(x2[i]-x1[i])/leng)
  return dirc,leng,unit 

# a. the distance between two vectors 
length=dirc_leng_unit([8,1,2],[3,4,5])[1]
print("the distance is "+str(length))
# b. the unit vector
unit=dirc_leng_unit([8,1,2],[3,4,5])[2]
print("the unit vector is "+str(unit))
# c. the energy of the particle
def ene(en):
  en=en*10e6
  return en
enr=ene(2.3)
print("the energy is "+str(enr)+"ev.")

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
dir=dirc_leng_unit([8,1,2],loc)[2] #the unit direction of the particle
en=ene(2.3) #energy as it arrived at the collision
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
# positiv z direction
z_hat=[0,0,1]
loc1=evenlog[3].get('location')
loc2=evenlog[8].get('location')
norm1=dirc_leng_unit([0,0,0],loc1)[2]
norm2=dirc_leng_unit([0,0,0],loc2)[2]
# the more aligned unit vector has greater dot product with positiv z-axis
if np.dot(norm1,z_hat) > np.dot(norm2,z_hat):
   print("the more aligned vector is event "+ str(evenlog[3]) )
elif np.dot(norm1,z_hat) == np.dot(norm2,z_hat):
   print("these two events are equally aligned with z-axis.")
else:
   print("the more aligned vector is event "+ str(evenlog[8]))




   





