"""
Application Goal
user inputs Weight:
user inputs K(g) or (L)bs:
app outputs converted weight
weight conversion:
1kg = 2.20462 lbs
"""

conversion = 2.20462
weight = raw_input('Weight: ')
# fail if not convertible to float
try:
     weight = float(weight)
except ValueError:
    print('Input must be integer or floating-point number')
metric = raw_input('K(g) or L(bs): ')
if metric.lower() == 'k':
    print('Weight is ' + str(round(weight*conversion,2)) + 'Lbs.')
elif metric.lower() == 'l':
    print('Weight is ' + str(round(weight/conversion,2)) + 'Kg')
else:
    raise Exception('Metric unit not allowed in allowes values: K, k, L, l')
