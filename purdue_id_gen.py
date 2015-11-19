import name_gen
import random

def gen_id_list(id_list_filename, new_entry_count):
    f = open(id_list_filename, "a+")
    for i in range(new_entry_count):
        random.seed()
        first_initial = name_gen.gen_first_initial(random.random())
        random.seed()
        last_name = name_gen.gen_last_name(random.random(), prop_white=.4, prop_api=.2, prop_chin=.2, prop_black=.1, prop_hisp=.1)
        current_id = gen_next_id(first_initial, last_name)
        #This method is not optimized at all.
        #I shudder to think how long it would take to come up with something like zhang984
        f.seek(0)
        for line in f:
            if line[0:len(line)-1] == current_id:
                current_id = gen_next_id(first_initial, last_name, current_id)
        f.write(current_id + "\n")

def gen_next_id(first_initial, last_name, current_id=""):
    if len(last_name) > 8:
        last_name = last_name[0:8]
    if current_id == "":
        return last_name
    if current_id == last_name:
        if len(last_name) > 7:
            last_name = last_name[0:7]
        return (last_name + first_initial)
    if len(last_name) > 7:
        last_name = last_name[0:7]
    if current_id == (last_name + first_initial):
        return (first_initial + last_name)
    if current_id == (first_initial + last_name):
        return (last_name + "1")
    #Extract the number from the username. It should always be at the end
    number = "error"
    for i in reversed(range(len(current_id))):
        if not current_id[i].isnumeric():
            number = current_id[i + 1:len(current_id)]
            break
    number = int(number)
    number = number + 1
    number = str(number)
    if len(last_name) + len(number) > 8:
        last_name = last_name[0:(8 - len(number))]
    return (last_name + number)
    
#gen_id_list("data/uid_list.txt", 10000)
