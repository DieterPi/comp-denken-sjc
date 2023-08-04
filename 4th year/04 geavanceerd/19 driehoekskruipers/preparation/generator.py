import os
import contextlib, io
import importlib
import random
import json

# set fixed seed for generating test cases
#random.seed(123456789)

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


def write_json( data:dict ):
    """ A function to write JSON file"""
    with open(os.path.join('..', 'evaluation', 'tests.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent = 2)


# generate unit tests for functions
exportdata = {'tabs': [] }
exportdata['tabs'].append( {'name': 'Feedback',
                            'contexts': [] } )

for i in range( 10 ):
    # generate test expression
    seedint = int( random.randint( 1, 10000 ) )
    expression = 'import random; random.seed( {} )'.format( seedint )
    
    exportdata['tabs'][0]['contexts'].append( {'before': {'python': {'data': expression }} })
    exportdata['tabs'][0]['contexts'][i]['testcases'] = []
    
    testcase = {'description': 'Uitvoeren van de code met seed {} leidt tot:'.format( seedint ),
                'input': {'main_call': 'True'},
                'output': {} }
    
    f = io.StringIO()
    with contextlib.redirect_stdout( f ):
        random.seed( seedint )
        spec.loader.exec_module(module)
    
    result = f.getvalue().replace('\n', '') 
    
    # setup for return expressions
    testcase['output']['stdout'] = {'type': 'text', 'data': result }
    exportdata['tabs'][0]['contexts'][i]['testcases'].append( testcase )

write_json( exportdata )