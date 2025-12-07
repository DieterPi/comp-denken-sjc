import os
import importlib.util
import random
import ruamel.yaml

yaml = ruamel.yaml.YAML()

# set fixed seed for generating test cases
random.seed(12345678)

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join('..', 'solution')
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

def write_yaml( data:list ):
    """ A function to write YAML file"""
    with open(os.path.join('..', 'evaluation', 'tests.yaml'), 'w', encoding='utf-8') as f:
        yaml.dump(data, f)


module_name = 'solution'
file_path = os.path.join(solutiondir, 'solution.nl.py')
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# generate test data
ntests = 21
cases = []
i = 1
while len(cases) < ntests:
    case = (i, )
    cases.append(case)
    i   += 1

# generate unit tests for functions
yamldata = []

# Generate first tab
tabtitle = "Feedback volgende_getal"

yamldata.append( {'tab': tabtitle, 'contexts': []})

for i in range(len(cases)):
    n = cases[i][0]
    if n != 1:
        yamldata[0]['contexts'].append( {'testcases' : []})
        
        # setup for return expressions
        getal = module.speciale_rij(n - 1)
        expression_name = f"volgende_getal({getal})"
        result = module.volgende_getal(getal)

        # setup for return expressions
        testcase = { "expression": expression_name, "return": result }
        yamldata[0]['contexts'][i-1]["testcases"].append( testcase)




# Generate second tab
tabtitle = "Feedback speciale_rij"

yamldata.append( {'tab': tabtitle, 'contexts': []})

for i in range(len(cases)):
    n = cases[i][0]
    yamldata[1]['contexts'].append( {'testcases' : []})
    
    # setup for return expressions    
    expression_name = f"speciale_rij({n})"
    result = module.speciale_rij(n)

    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[1]['contexts'][i]["testcases"].append( testcase)
    
write_yaml(yamldata)