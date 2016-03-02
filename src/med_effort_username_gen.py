import subprocess
def med_effort_username_gen(randfrac):
    passfile = "../input/usernames.txt"
    #The number of lines is appended at the end of the file for speed reasons
    lastnum = int(subprocess.check_output(["tail", "-1", passfile]).decode("utf-8"))
    rand = round(randfrac * lastnum)
    #use shell commands to grab desired line. I figured this would be faster
    heads = subprocess.Popen(["head", "-" + str(rand), passfile], stdout=subprocess.PIPE)
    output = subprocess.check_output(["tail", "-1"], stdin=heads.stdout).decode("utf-8")
    heads.wait()
    output = output[:len(output) -1]
    return(output)
