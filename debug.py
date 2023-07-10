from lib.animal import Animal
from lib.zoo import Zoo

# code here
z1=Zoo("Disney", "Orlando, FL")
z2=Zoo("San Diego Zoo", "San Diego")

a1 = Animal("Lion", 100, "Luke", z1)
a2=Animal("Bear", 200, "Bruno", z1)
a3=Animal("Cheetah", 65, "Chessy", z2)
a4=Animal("Giraffe", 200, "Ginny", z2)
a5=Animal("Giraffe", 250, "Barbara", z2)

# e.g.  

# z1 = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )
# a1 = Animal( 'Lion', 75, 'Luke', z1 )






# ipdb allows us to stop our code & test stuff
import ipdb; ipdb.set_trace()
print( 'Thanks for visiting the zoo!' )