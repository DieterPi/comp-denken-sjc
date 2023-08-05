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

# generate test data
cases = [ ((0,0), (-2,4), (3,4), 3.00, 2.14, 3.26) ]
cases.append( ((-106,2), (134,54), (134,-20), 136.565002837, 157.079597657, 119.641130052) )
cases.append( ((-80, -45), (148, 131), (117, -75), 83.0963296422, 205.0, 156.773722288) )
cases.append( ((-142, -90), (112, 114), (122, -83), 176.819116614, 152.161098839, 141.400141443) )
cases.append( ((-124, 142), (91, 149), (100, -48), 158.050624801, 175.641680703, 142.239235094) )
cases.append( ((-132, -147), (147, 90), (127, -65), 219.127816582, 151.489273548, 83.6301381082) )
cases.append( ((-148, -111), (139, 126), (92, -130), 203.403539792, 169.177421661, 162.012345209) )
cases.append( ((-112, -10), (130, 39), (87, -149), 69.3541635376, 195.256241898, 174.917123233) )

# generate unit tests for functions
yamldata = []
yamldata.append( {'tab': 'Feedback', 'testcases': []})
# input, expression, statement or stdin?
input = 'expression'
# output, stdout or return?
output = 'stdout'
for test in cases:
    # generate test expression
    expression_name = 'trilateratie( {}, {}, {}, {}, {}, {} )'.format( test[0], test[1], test[2], test[3], test[4], test[5] )
    
    f = io.StringIO()
    with contextlib.redirect_stdout( f ):
        module.trilateratie( test[0], test[1], test[2], test[3], test[4], test[5] )
    
    result = f.getvalue().strip() 
    
    # setup for return expressions
    testcase = { input: expression_name, output: ''+ result }
    yamldata[0]['testcases'].append( testcase )

write_yaml(yamldata)