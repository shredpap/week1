# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is 24 students, since this is the
# number of PCs in a lab. Write a program that calculates how many groups are
# needed for the following number of students: 113, 175, 12. Display how many full
# groups there will be, and how many students will be in the smaller "left over"
# group.
l=24
d,e,f=113,175,12
def numned(labgrp,a,b,c):
    sub=0
    sub+=a%labgrp
    sub+=b%labgrp
    sub+=c%labgrp
    
    print(a//labgrp)                                        k
    print(b//labgrp)
    print(c//labgrp)
    print((sub+c)//labgrp)
numned(l,d,e,f)