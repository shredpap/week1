# In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014
# times, was not out 162 times, and scored 48426 runs. Write a program to calculate
# and display Boycott's batting average.
# Note: A batting average is the number of runs scored divided by the number of
# completed innings (i.e. the total times batted minus the times not out).
mach=609
bat=1014
noto=162
runn=48426
def batavg(m,b,n,r):
    cinn=b-n
    print (r/cinn)

batavg(mach,bat,noto,runn)
