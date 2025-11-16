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
ntests = 35
cases = [(4, [[2,3], [1, 4], [1, 2], [1, 2], [2, 2], [2, 2], [2, 1]])]
while len(cases) < ntests:
    w = random.randint(4,50)
    l = random.randint(4,50)
    opp = w * l
    
    A = 0
    stukken = []
    while A < opp:
        stuk = [random.randint(1, min(w,l,4)) for _ in range(2)]
        if A + stuk[0] * stuk[1] > opp:
            if random.randint(0,1) == 0:
                stuk = [1, opp - A]
            else:
                stuk = [opp - A, 1]
            A += stuk[0] * stuk[1]
        else:
            A += stuk[0] * stuk[1]
        
        stukken.append(stuk)
    
    case = (w, stukken)
    if case not in cases:
        cases.append(case)

cases = sorted(cases, key =  lambda x: len(x[1]))

# generate unit tests for functions
yamldata = []

# Generate first tab
tabtitle = "Feedback"

yamldata.append( {'tab': tabtitle, 'contexts': []})

for i in range(len(cases)):
    breedte = cases[i][0]
    stukken = cases[i][1]
    yamldata[0]['contexts'].append( {'testcases' : []})
    
    # setup for return expressions    
    expression_name = f"lengte_cake({breedte}, {stukken})"
    result = module.lengte_cake(breedte, stukken)

    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)
    
write_yaml(yamldata)