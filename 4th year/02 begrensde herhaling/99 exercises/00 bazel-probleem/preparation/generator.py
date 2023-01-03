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
#ntests= 10
cases = [(10,),(100,),(10000,),(50,), (100000,), (5000,), (1000000,), (10000000,)]
#while len(cases) < ntests:
#    exp = random.randint(3,6)
#    cases.append( (pow(10,exp), )) 

# generate unit tests for functions
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for test in cases:
    # generate test expression
    print(f'>>> bazel_benadering({test[0]}) # doctest: +STDOUT')

    # generate return value
    try:
        print('{}'.format(module.bazel_benadering(test[0])))
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))
