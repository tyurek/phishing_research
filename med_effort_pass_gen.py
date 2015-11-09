#import random
import subprocess
def med_effort_pass_gen(randfrac):
    dist = "data/rockyou_dist.csv"
    #Read distribution file for appropriate random number range
    lastnum = int(subprocess.check_output(["tail", "-1", dist]).decode("utf-8").split(",")[1])
    randnum = round(randfrac * lastnum)
    f = open(dist)
    #Pick the password corresponding to random number
    for line in f.readlines():
        #Like splitting on comma, but accounts for passwords containing one or more commas
        part = line.rpartition(",")
        cumu_num = int(part[2])
        if randnum <= cumu_num:
            password = part[0]
            break
    f.close()
    return password
#random.seed()
#print(med_effort_pass_gen(random.random()))
