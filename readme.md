###General info:
version of python tested: 3.4
additional library installations needed: none

##external function descriptions

###low_effort_pass_gen(randfrac):
Contained in src/low_effort_pass_gen.py
Selects a random password from a large internal password list.
randfrac: is a random fraction between 0 and 1
The following code uses the function as intended:
```
random.seed()
print(low_effort_pass_gen(random.random()))
```

###low_effort_username_gen(randfrac):
Contained in src/low_effort_username_gen.py
Selects a random username from an internal name list.
randfrac: is a random fraction between 0 and 1
The following code uses the function as intended:
```
random.seed()
print(low_effort_username_gen(random.random()))
```

###med_effort_pass_gen(randfrac):
Contained in src/med_effort_pass_gen.py
Selects a random password from a large internal weighted password list.
randfrac: is a random fraction between 0 and 1
The following code uses the function as intended:
```
random.seed()
print(med_effort_pass_gen(random.random()))
```

###gen_purdue_id_list(id_list_filename, new_entry_count):
Conatined in src/purdue_id_gen.py
Generates a list of plausible purdue ids.
Known distributions of surnames are used in conjunction with the known ethnic distribution of a given population.
id_list_filename: Filename of output list of purdue ids
new_entry_count: number of ids to generate (either in an empty file, or adding onto a preexisting file
The following code uses the function as intended:
```
#Add 10000 purdue ids to the file output_list.txt
gen_id_list("output_list.txt", 10000)
#Add 500 more ids to the same list
gen_id_list("output_list.txt", 500)
```