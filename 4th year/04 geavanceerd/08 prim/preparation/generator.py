import os
import sys
import importlib
import random
import string

# set fixed seed for generating test cases
random.seed(123456789)

def triangle_num(n):
    som = 0
    for i in range(1,n):
        som += i
    return som

def edge_exists( E, vertex1, vertex2 ):
    flag = False
    for edge in E:
        flag += (edge[0] == vertex1 and edge[1] == vertex2) or (edge[1] == vertex1 and edge[0] == vertex2)

    return flag

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
alphabet = list( string.ascii_uppercase )
ntests= 5
cases = [ ( ['A','B','C','D','E'], 
            [('A','B',3), ('B','C',4),('C','D',2),('B','D',7),('B','E',8)] ), ]
while len(cases) < ntests:
    aantal_v = random.randint(4,7)
    V = alphabet[:aantal_v]
    E = []

    vertex_unconnected = V.copy()
    while len(vertex_unconnected) > 0:
        vertex1 = V[random.randint(0,aantal_v-1)]
        vertex2 = V[random.randint(0,aantal_v-1)]
        weight = random.randint(1, 15)

        if vertex1 != vertex2 and not(edge_exists( E, vertex1, vertex2)):
            E.append( (vertex1, vertex2, weight))
            if(vertex1 in vertex_unconnected):
               vertex_unconnected.remove(vertex1)
            if(vertex2 in vertex_unconnected):
                vertex_unconnected.remove(vertex2)

    cases.append( (V, E) ) 

# generate unit tests for functions
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for test in cases:
    # generate test expression
    print(f'>>> MST_prim( {test[0]}, {test[1]} )')

    # generate return value
    try:
        print('{}'.format(module.MST_prim( test[0], test[1])))
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))