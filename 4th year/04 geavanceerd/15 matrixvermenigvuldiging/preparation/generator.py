import os
import sys
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

def write_yaml(data):
    """ A function to write YAML file"""
    with open(os.path.join('..', 'evaluation', 'tests.yaml'), 'w', encoding='utf-8') as f:
        yaml.dump(data, f)

# generate test data
ntests= 20
cases = [ [[[1,3],[4,5]], [[0,1],[-1,3]]],
          [[[1,5,7]], [[3],[2],[-1]]]]


while len(cases) < ntests:
    m = random.randint(1,5)
    k = random.randint(1,5)
    n = random.randint(1,5)

    A = []
    for r in range(m):
        row = []
        for c in range(k):
            row.append( random.randint( -10,10 ) )
        A.append( row )
    B = []
    for r in range(k):
        row = []
        for c in range(n):
            row.append( random.randint( -10,10 ) )
        B.append( row )
    
    cases.append( [A, B] )

# generate unit tests for functions
yamldata = []
yamldata.append( {'tab': 'Feedback', 'testcases': []})
for test in cases:
    # generate test expression
    expression_name = 'matrixvermenigvuldiging( {} , {} )'.format( test[0], test[1] )
    result = ruamel.yaml.comments.CommentedSeq( module.matrixvermenigvuldiging( test[0], test[1] ) )
    result.fa.set_flow_style()
    
    # setup for return expressions
    testcase = { 'expression': expression_name, 'return': result }
    yamldata[0]['testcases'].append( testcase)

write_yaml(yamldata)