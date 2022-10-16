# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is 24 students, since this is the
# number of PCs in a lab. Write a program that calculates how many groups are
# needed for the following number of students: 113, 175, 12. Display how many full
# groups there will be, and how many students will be in the smaller "left over"
# group.
l=24
list=[113,175,12]
def main(a,l=24):
    print("class with",a,"students will have",a//l,"groups")
# def sub(a,l=24):
    # sub=0
    # sub+=i%labgrp
    # sub+=b%labgrp
    # sub+=c%labgrp
    # print(sub//l)
for i in range(len(list)):
    main(list[i])
    # sub(list[i])

sub=0
sub+=list[0]%l
sub+=list[1]%l
sub+=list[2]%l
print("leftover group will have",sub,"students",)
# print("total groups needed: ",)
if sub>l:
    print("smaller leftover group will have",sub-l,"students")

