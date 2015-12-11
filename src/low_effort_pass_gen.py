import random
import subprocess
def low_effort_pass_gen(randfrac):
    #The password file used here is every 250th line of the regular rockyou password file
    #It would have been over 100 MB otherwise
    passfile = "../input/rockyou_reduced_unweighted.txt"
    #The number of lines is appended at the end of the file for speed reasons
    lastnum = int(subprocess.check_output(["tail", "-1", passfile]).decode("utf-8"))
    rand = round(randfrac * lastnum)
    #use shell commands to grab desired line. I figured this would be faster
    heads = subprocess.Popen(["head", "-" + str(rand), passfile], stdout=subprocess.PIPE)
    output = subprocess.check_output(["tail", "-1"], stdin=heads.stdout).decode("utf-8")
    heads.wait()
    output = output[:len(output) -1]
    return(output)

