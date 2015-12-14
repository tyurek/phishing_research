import random
import math
import subprocess

#assumes randfrac is between 0 and 1, with sufficient decimal places (e.g. via random.random())
#proportions do not need to add up to a certain number, the program handles that
def gen_last_name(randfrac, prop_white=0, prop_api=0, prop_hisp=0, prop_black=0, prop_china=0, prop_colomb=0, prop_india=0, prop_indo=0, prop_iran=0, prop_malay=0, prop_skorea=0, prop_taiwan=0):
    dist_white="../input/surname_dist_white.csv"
    dist_api="../input/surname_dist_api.csv"
    dist_hisp="../input/surname_dist_hisp.csv"
    dist_black="../input/surname_dist_black.csv"
    dist_china="../input/surname_dist_china.csv"
    dist_colomb="../input/surname_dist_colomb.csv"
    dist_india="../input/surname_dist_india.csv"
    dist_indo="../input/surname_dist_indo.csv"
    dist_iran="../input/surname_dist_iran.csv"
    dist_malay="../input/surname_dist_malay.csv"
    dist_skorea="../input/surname_dist_skorea.csv"
    dist_taiwan="../input/surname_dist_taiwan.csv"
    #these lists must be in the same order
    eth_props = [prop_white, prop_api, prop_hisp, prop_black, prop_china, prop_colomb, prop_india, prop_indo, prop_iran, prop_malay, prop_skorea, prop_taiwan]
    sur_dists = [dist_white, dist_api, dist_hisp, dist_black, dist_china, dist_colomb, dist_india, dist_indo, dist_iran, dist_malay, dist_skorea, dist_taiwan]
    prop_sum = 0
    for i in eth_props:
        prop_sum = prop_sum + i
    rand = randfrac * prop_sum
    cumu_sum = 0
    #default case (i.e. no porportions were given)
    sur_dist = sur_dists[0]
    #Use the random number to pick an ethnicity at random
    for i in range(len(eth_props)):
        cumu_sum = cumu_sum + eth_props[i]
        if rand <= cumu_sum:
            sur_dist = sur_dists[i]
            break
    #Read distribution file for appropriate random number range
    lastnum = int(subprocess.check_output(["tail", "-1", sur_dist]).decode("utf-8").split(",")[1])
    #I'm assuming reusing the seed here won't cause a noticable bias, but it may be better to use a second one
    randnum = round(randfrac * lastnum)
    f = open(sur_dist)
    #Pick the last name corresponding to random number
    for line in f.readlines():
        cumu_num = int(line.split(",")[1])
        if randnum <= cumu_num:
            surname = line.split(",")[0]
            break
    f.close()
    return surname

def gen_first_initial(randfrac):
    dist = "../input/first_initial_dist_all.csv"
    #Read distribution file for appropriate random number range
    lastnum = int(subprocess.check_output(["tail", "-1", dist]).decode("utf-8").split(",")[1])
    randnum = round(randfrac * lastnum)
    f = open(dist)
    #Pick the initial corresponding to random number
    for line in f.readlines():
        cumu_num = int(line.split(",")[1])
        if randnum <= cumu_num:
            initial = line.split(",")[0]
            break
    f.close()
    return initial
    
#random.seed()
#print(gen_last_name(random.random(), prop_white=7, prop_chin=7))
#print(gen_first_initial(random.random()))
