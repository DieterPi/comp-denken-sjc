import os
import contextlib, io
import importlib
import random
import ruamel.yaml

yaml = ruamel.yaml.YAML()

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

def write_yaml( data:list ):
    """ A function to write YAML file"""
    with open(os.path.join('..', 'evaluation', 'tests.yaml'), 'w', encoding='utf-8') as f:
        yaml.dump(data, f)

def construct_graph( connected = False, weight = 0, n_vertices = 0, n_edges = 0 ) -> dict:
    """ A function to construct a (possibly disconnected) random graph
    The implementation is not that good xD
    
    :param connected: boolean indicating if there can be vertices without connections.
    :param weight: int indicating if the graph should be weighted, if weighted then this
                   number is used as a max for the weight.
    """
    alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if n_vertices == 0:
        n_vertices = random.randint(3, 10) # can be set to 26 for huge graphs
    V = []
    for i in range(n_vertices):
        V.append(alf[i])
        
    E = []
    E_simple = []
    if n_edges == 0:
        n_edges = random.randint(n_vertices, (n_vertices - 1)*n_vertices/2 )
    
    # construction of all possible edges, and then picking some at random
    all_E = []
    for v1 in V:
        for v2 in V:
            if v1 != v2:
                all_E.append( (v1, v2) )

    discount = 0
    if connected: # if all vertices must be present and connected in the graph
        V_copy = V.copy()
        v1 = random.choice( V_copy )
        V_copy.remove(v1)
        v2 = random.choice( V_copy )
        V_copy.remove(v2)
        E_simple.append( (v1, v2) )
        if weight != 0:
            E.append( (v1, v2, random.randint(2, weight)) )
        else:
            E.append( (v1, v2) )
        
        for i in range( n_vertices - 2):
            v1 = random.choice( E_simple )[random.randint(0,1)]
            v2 = random.choice( V_copy )
            V_copy.remove(v2)
            E_simple.append( (v1, v2) )
            if weight != 0:
                E.append( (v1, v2, random.randint(2, weight)) )
            else:
                E.append( (v1, v2) )

        discount = n_vertices - 1
    
    i = discount
    
    i = discount
    while i < n_edges:
        edge_c = random.choice( all_E )
        edge_c_inv = (edge_c[1], edge_c[0])
        if edge_c not in E_simple and edge_c_inv not in E_simple:
            E_simple.append( edge_c)
            i += 1
            if weight != 0:
                E.append( (edge_c[0], edge_c[1], random.randint(2, weight)) )
            else:
                E.append( (edge_c[0], edge_c[1]) )
        else: # remove this edge from all
            try:
                all_E.remove(edge_c)
                all_E.remove(edge_c_inv)
            except ValueError:
                pass
            
    return {'V': V, 'E': E}

# generate test data
ntests = 20
cases = [ ('C', [('A', 'B', 3), ('B', 'C', 2), ('C', 'A', 5), ('C', 'D', 2), ('D', 'B', 8), ('B', 'E', 3)] ) ]

while len( cases ) < ntests:
    graph = construct_graph(connected = True, weight = random.randint(0,1)*random.randint(3,40) )
    cases.append( (random.choice(graph["V"]), graph["E"]) )
    
# generate unit tests for functions
yamldata = []
yamldata.append( {'tab': 'Feedback', 'testcases': []})
# input, expression, statement or stdin?
input = 'expression'
# output, stdout or return?
output = 'stdout'
for test in cases:
    # generate test expression
    expression_name = 'verbonden_bogen( {}, {} )'.format( test[0], test[1] )
    result = str(module.verbonden_bogen( test[0], test[1] ))
    
    # setup for return expressions
    testcase = { input: expression_name, output: result }
    yamldata[0]['testcases'].append( testcase)

write_yaml(yamldata)