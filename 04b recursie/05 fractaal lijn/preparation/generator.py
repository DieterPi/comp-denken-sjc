import os
import importlib.util
import random
import ruamel.yaml
import subprocess
import sys
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
ntests= 10
i = 4
cases = [(1,),(2,),(3,)]
while len(cases) < ntests:
    cases.append((i, ))
    i += 1


# generate unit tests for functions
yamldata = []

# input, expression, statement or stdin?
input = 'stdin'
# output, stdout or return?
output = 'stdout'
tabtitle = "Feedback"

yamldata.append( {'tab': tabtitle, 'contexts': []})

for i in range(len(cases)):
    test = cases[i]
    param = test[0]
    print("testcase:", test)
    yamldata[0]['contexts'].append( {'testcases' : []})
        
    # generate test expression
    expression_name = f"lijn({param})"
        
    # Script dat we in de subprocess uitvoeren om het .nl.py bestand te laden
    python_code = f"""
import importlib.util
import os
spec = importlib.util.spec_from_file_location('solution', '{file_path}')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
module.lijn({param})
"""

    result = subprocess.run(
        [sys.executable, "-c", python_code],
        capture_output=True,
        text=True
    )
    
    # result.stdout bevat nu alles wat de recursieve functie geprint heeft
    captured_stdout = result.stdout
    
    # Gebruik result.stdout om alleen de geprinte tekst op te vangen
    captured_output = result.stdout.strip()
    
   
    print(captured_output)
    # setup for return expressions
    testcase = { "expression": expression_name, "stdout": captured_output }
    yamldata[0]['contexts'][i]["testcases"].append( testcase)


write_yaml(yamldata)