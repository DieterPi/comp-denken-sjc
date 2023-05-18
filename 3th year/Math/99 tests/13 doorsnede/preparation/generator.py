import os
import sys
import importlib
import random

# set fixed seed for generating test cases
random.seed(123456789)

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join('..', 'solution')
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

# load functionality defined in sample solution
module_name = 'solution'
file_path = os.path.join(solutiondir, 'solution.nl.py')
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

for name in dir(module):
    if not (name.startswith('__') and name.endswith('__')):
        globals()[name] = eval(f'module.{name}')

# generate test data
ntests= 40
cases = [ (( 3, 5 ), ( -1, 4 ) ), ( ( -8, 0 ), ( 5, 10 ) ), (( -2, 6 ), ( 6, 7 )) ]
while len(cases) < ntests:
    a = random.randint(-15,15)
    b = random.randint(-15,15)
    
    c = random.randint(-15,15)
    d = random.randint(-15,15)
    if a < b and c < d:
        cases.append( ((a,b), (c,d)) ) 

# generate unit tests for functions
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for test in cases:
    # generate test expression
    print(f'>>> doorsnede({test[0]}, {test[1]}) # doctest: +STDOUT')

    # generate return value
    try:
        module.doorsnede(test[0], test[1])
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))
