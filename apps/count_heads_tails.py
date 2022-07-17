# 10000 loops
# 100 coin flips (H vs. T)
# count steaks of 6 (H or T)

import random
experiment_list = []
for experiment in range(0,10000):
    tosses_list = []
    for tosses in range(0,100):
        call_int = random.randint(0,1)
        if call_int == 0:
            call = 'Heads'
        if call_int == 1:
            call = 'Tails'
        tosses_list.append(call) 
    experiment_list.append(tosses_list)

def count_6_streaks(tosses_list):
    percentage = 0
    for index in range(0,len(tosses_list)-5): # cut end by 5
        sliding_six_group = tosses_list[(index):(index+6)]
        if 'Heads' in sliding_six_group and 'Tails' not in sliding_six_group:
            percentage += 1
        # print sliding_six_group
        if 'Tails' in sliding_six_group and 'Heads' not in sliding_six_group:
            percentage += 1
        # print sliding_six_group
    # print percentage
    return percentage

percentages_list = []
for experiment in experiment_list:
    percentage = count_6_streaks(experiment)    
    percentages_list.append(percentage)

print(len(percentages_list))
sum_of_streaks = 0
for percentage in percentages_list:
    sum_of_streaks += percentage

Total_Percentage = float(sum_of_streaks)/(10000*100)*(100)# 10000 experiments, 100 tosses/exp
print str(Total_Percentage)+' % of coin tosses contain a streak of 6 Heads or Tails.'
