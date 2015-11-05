import subprocess
def med_effort_pass_gen(randfrac):
    dist = "data/rockyou_dist.csv"
    #Read distribution file for appropriate random number range
    lastnum = int(subprocess.check_output(["tail", "-1", dist]).decode("utf-8").split(",")[1])
    randnum = round(randfrac * lastnum)
    f = open(dist)
    #Pick the password corresponding to random number
    for line in f.readlines():
        cumu_num = int(line.split(",")[1])
        if randnum <= cumu_num:
            password = line.split(",")[0]
            break
    f.close()
    return password
