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
ntests = 30
cases = [(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), (14, [3, 9, 7, 5]), (13, [3, 9, 7, 5]), (6, [3, 9, 7, 5]),
         (96, [1, 3, 7, 15, 31, 65, 140, 250]),
         (4, [31, 15, 140, 7, 250, 3, 65, 1])]
while len(cases) < ntests:
    n = random.randint(2,1000)
    nums = list(random.sample(range(2, 4000), n))
    i, j = (random.randint(0,n-1), random.randint(0,n-1))
    if i != j:
        case = (max(2,nums[i] + nums[j] + (random.randint(0,10) != 0)*random.randint(-1000,10000)), nums)
        cases.append(case)

cases = sorted(cases, key = lambda x : len(x[1]))


# generate unit tests for functions
yamldata = []

# Generate first tab
tabtitle = "Feedback"

yamldata.append( {'tab': tabtitle, 'contexts': []})

for i in range(len(cases)):
    case = cases[i]

    yamldata[0]['contexts'].append( {'testcases' : []})
    
    # setup for return expressions
    expression_name = f"in_balans({case[0]}, {case[1]})"
    result = module.in_balans(case[0], case[1])

    # setup for return expressions
    testcase = { "expression": expression_name, "return": result }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)


write_yaml(yamldata)