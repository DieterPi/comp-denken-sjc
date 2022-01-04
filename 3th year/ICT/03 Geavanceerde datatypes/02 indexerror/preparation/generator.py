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
klassen = [ '3GRLA', '3LA1', '3LA2', '3LA3', '3ECWE', '3NAWE1', '3NAWE2', '3NAWE3', '3HUWE', '3MT', '3SPWE' ]
ntests= 20
cases = [klassen.copy(), [ '3GRLA', '3LA1', '3LA2', '3LA3' ]]
while len(cases) < ntests:
    randomlength = random.randint(2, len(klassen)-1)
    random.shuffle(klassen)
    cases.append( klassen[:randomlength] ) 

# generate unit tests
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for test in cases:
    # generate test expression
    print(f'>>> laatste_element({test})')

    # generate return value
    try:
        print('\'{}\'\n'.format(module.laatste_element(test)))
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))
