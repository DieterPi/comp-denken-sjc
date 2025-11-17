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
cases = []
cases.append( ['def f( x ) : return x - 2', 0, 5, -4])
cases.append( ['def f( x ) : return x**3 - 2', 1, 4, -5] )
cases.append( ['def f( x ) : return (x-2)**(1/3)-1', 2, 7, -7] )
cases.append( ['def f( x ) : return 5 * (x - 2) * (x - 3) * (x - 4)', 0, 5, -7] )
cases.append( ['def f( x ) : return -5 / (x**2 + 1) + 2', -1, 3, -3] )
cases.append( ['def f( x ) : return -5 / (x**2 + 1) + 2', -1, 3, -2] )
cases.append( ['def f( x ) : return -5 / (x**2 + 1) + 2', -1, 3, -1] )

def makeF():
    script = test[0]
    exec(script, globals())
    return f

# generate unit tests for functions
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for test in cases:
    # generate test expression
    print('>>> {} #doctest: +NEWCONTEXT'.format( test[0]))
    print('>>> bisectiemethode( f, {}, {}, 10**{})'.format( test[1], test[2], test[3] ) )
            
    # generate return value
    try:        
        f = makeF()
        print( module.bisectiemethode( f, test[1], test[2], 10**int(test[3]) ) )
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))