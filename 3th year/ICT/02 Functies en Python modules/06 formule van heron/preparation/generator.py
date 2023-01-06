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
ntests= 20
cases = [(4,13,15),]
while len(cases) < ntests:
    a = random.randint(1,20)
    b = random.randint(1,20)
    c = random.randint(1,20)
    if  b+c > a and a+c > b and a+b > c:
        cases.append( (a, b, c) ) 

# generate unit tests for function oppervlakte
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for test in cases:
    # generate test expression
    print(f'>>> oppervlakte({test[0]},{test[1]},{test[2]}) # doctest: +STDOUT')

    # generate return value
    try:
        print('{}\n'.format(module.oppervlakte(test[0], test[1], test[2])))
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))
