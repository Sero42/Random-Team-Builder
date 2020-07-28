import random
import sys

def single_name(list_of_names, sampling):
    for c in range(len(list_of_names)):
      print(sampling[c])
      print('One more name? (1) Or exit? (2)')
      decision = input()
      if decision == 1:
          single_name(list_of_names, sampling)
      if decision == '2':
          print('Do you want to save the current situation (1), the whole randomized list of names (2) or just exit (3)?')
          exit_decision = input()
          if exit_decision == '1':
              f = open(str(group) + "single.txt", "w")
              f.write(str(sampling[(c + 1):(len(list_of_names))]))
              f.close()
              sys.exit()
          if exit_decision == '2':
              f = open(str(group) + "single.txt", "w")
              f.write(str(sampling))
              f.close()
              sys.exit()
          if exit_decision == '3':
              sys.exit()

def single_names_old():
    with open(str(group) + 'single.txt', 'r') as f:
        old_sample = f.read()
        old_sample = old_sample.replace("[", "")
        old_sample = old_sample.replace("]", "")
        old_sample = old_sample.replace("'", "")
        old_sample = old_sample.split(",")
    for c in range(len(old_sample)):
      print(old_sample[c])
      print('One more name (1), or exit (2)?')
      decision = input()
      if decision == 1:
          single_names_old()
      if decision == '2':
          print('Would you like to save the current state (1), the previous one (2) or just exit (3)?')
          exit_decision = input()
          if exit_decision == '1':
              f = open(str(group) + "single.txt", "w")
              f.write(str(old_sample[(c + 1):(len(old_sample))]))
              f.close()
              sys.exit()
          if exit_decision == '2':
              f = open(str(group) + "single.txt", "w")
              f.write(str(old_sample))
              f.close()
              sys.exit()
          if exit_decision == '3':
              sys.exit()

def old_groups():
    with open(str(group) + 'groups.txt', 'r') as file:
        for line in file:
            print(line)
    input()
    sys.exit()

def groups_exit(dicts):
    print('Would you like to save groups (1) or just exit (2)?')
    decision = input()
    if decision == '1':
        f = open(str(group) + "groups.txt", "w")
        f.write(str('\n'.join("{}: {}".format(k, v) for k, v in dicts.items())))
        f.close()
        sys.exit()
    else:
        sys.exit()




print('What group is it about?')
group = input().lower()

list_of_names = open(str(group) + '.txt', encoding='utf-8').read().splitlines()

sampling = random.sample(list_of_names, k=len(list_of_names))


print('Would you like to display single names (1) or groups (2)?')
decision = input()

if decision == '1':
    print('Start from scratch (1) or continue with a saved list (2) ?')
    start_decision = input()
    if start_decision == '1':
        single_name(list_of_names, sampling)
    else:
        single_names_old()

else:
    print('New groups (1), or saved ones (2)?')
    start_decision = input()
    if start_decision == '1':
        print('How many groups should it be?')
        number_of_groups = input()
    else:
        old_groups()

dicts = {}

remainder = len(list_of_names) % int(number_of_groups)
'''remainder is the number of group members which remains by dividing the number of all group members by the number of groups'''

for i in range((remainder)): # groups which get an additional member
    c = (i+1) + (i + 1) * (len(list_of_names) // int(number_of_groups))
    ''' c is the upper limit for the number of groups
    with an additional member. For group 0 (i=0) it is: 1 + 1 * (number_of_all_group_members/number_of_groups) 
    e.g.: 1 + 1*30/4 = 3 '''
    d = i + i * (len(list_of_names) // int(number_of_groups))
    '''d is the lower limit of the number of groups with an additional member
    e.g. (i=0) 0 + 0 * 30/4 = 0 '''
    dicts[i] = sampling[d:c]
    ''' values to key i. In the previous example for i=0 the group members 0 to 7, for i=1 members from 8 to 16 etc. '''

for i in range((remainder), int(number_of_groups)): # groups without additional member
    c = remainder + (i + 1) * (len(list_of_names) // int(number_of_groups))
    ''' c is the upper limit of groups
    for group 2 (i=2) it is: 2 + (2+1) * (number_of_all_group_members/number_of_groups)
    e.g. c = 2 + 3*(30/4) = 23 '''
    d = remainder + i * (len(list_of_names) // int(number_of_groups))
    ''' d is the lower limit
    example: (i=2) d= 2 + 2*7 = 16'''
    dicts[i] = sampling[d:c]
    ''' for 30/4 and i = 2 these are the members 16 to 23'''

print('\n'.join("{}: {}".format(k, v) for k, v in dicts.items()))

groups_exit(dicts)






