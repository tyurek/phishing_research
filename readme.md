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

###gen_purdue_id_list(id_list_filename, new_entry_count, prop_white=0, prop_api=0, prop_hisp=0, prop_black=0, prop_china=0, prop_colomb=0, prop_india=0, prop_indo=0, prop_iran=0, prop_malay=0, prop_skorea=0, prop_taiwan=0):
Conatined in src/purdue_id_gen.py

Generates a list of plausible purdue ids.

Known distributions of surnames are used in conjunction with the known ethnic distribution of a given population.

id_list_filename: Filename of output list of purdue ids

new_entry_count: number of ids to generate (either in an empty file, or adding onto a preexisting file)

prop_white: Optional, specifies the proportion of surnames that will be from a weighted distribution of white american surnames

prop_api: Optional, specifies the proportion of surnames that will be from a weighted distribution of asian/pacific islander american surnames

prop_hisp: Optional, specifies the proportion of surnames that will be from a weighted distribution of hispanic american surnames

prop_black: Optional, specifies the proportion of surnames that will be from a weighted distribution of african american surnames

prop_china: Optional, specifies the proportion of surnames that will be from a weighted distribution of surnames from China

prop_colomb: Optional, specifies the proportion of surnames that will be from a weighted distribution of surnames from Colombia

prop_india: Optional, specifies the proportion of surnames that will be from a weighted distribution of surnames from India

prop_indo: Optional, specifies the proportion of surnames that will be from a weighted distribution of surnames from Indonesia

prop_iran: Optional, specifies the proportion of surnames that will be from a weighted distribution of surnames from Iran

prop_malay: Optional, specifies the proportion of surnames that will be from a weighted distribution of surnames from Malaysia

prop_skorea: Optional, specifies the proportion of surnames that will be from a weighted distribution of surnames from South Korea

prop_taiwan: Optional, specifies the proportion of surnames that will be from a weighted distribution of surnames from Taiwan

The following code uses the function as intended:
```
#Add 10000 purdue ids to the file output_list.txt
#This list will have approximately 40% names of Colombian origin, 50% from South Korea, and 10% from Taiwan
gen_id_list("output_list.txt", 10000, prop_colomb=.4, prop_skorea=.5, prop_taiwan=.1)
#Add 500 more ids to the same list
gen_id_list("output_list.txt", 500, prop_colomb=.4, prop_skorea=.5, prop_taiwan=.1)
```