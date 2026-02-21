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
ntests= 25
cases = [(-3,-1,2,3,1,1.2),
         (0,0,5,0,0,2),
         (-8,2,5,-8,2,5),
         (4,3,2,-1,3,3),
         (4,3,5,5,2,0.2)]
while len(cases) < ntests:
    case = []
    case.append(random.randint(-10, 10))
    case.append(random.randint(-10, 10))
    case.append(round(random.uniform(0.5,10), 1))
    case.append(random.randint(-10, 10))
    case.append(random.randint(-10, 10))
    case.append(round(random.uniform(0.5,10), 1))
    if case not in cases:
        cases.append(case) 

# generate unit tests for functions
yamldata = []

# Generate first tab
tabtitle = "Feedback"

yamldata.append( {'tab': tabtitle, 'contexts': []})

for i in range(len(cases)):
    case = cases[i]
    yamldata[0]['contexts'].append( {'testcases' : []})
    
    # setup for return expressions    
    expression_name = f"onderlinge_ligging({case[0]}, {case[1]}, {case[2]}, {case[3]}, {case[4]}, {case[5]})"
    result = module.onderlinge_ligging(case[0], case[1], case[2], case[3], case[4], case[5])

    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)
            
write_yaml(yamldata)
