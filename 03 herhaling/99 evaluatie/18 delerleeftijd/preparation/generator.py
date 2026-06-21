import os
import sys
import importlib.util
import random
import ruamel.yaml
import subprocess

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

def count_divs(a:int, b:int, c:int, d:int) -> int:
    count = 0
    for div in range(2, min(a,b,c,d) + 1):
        if (a % div == 0 and b % div == 0 and c % div == 0 and d % div == 0):
            count += 1
    
    return count

def get_primes_up_to(n):
    if n < 2:
        return []
    
    # Create a boolean array and assume all are prime initially
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # Sieve: mark multiples of each prime as not prime
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    # Return list of all numbers marked as prime
    return [num for num in range(2, n + 1) if is_prime[num]]

# Get all primes <= 9999
primes = get_primes_up_to(5000)


# generate test data
ntests= 20
cases = [(30,), (23,), (18,)]
while len(cases) < ntests:
    a = random.randint(17, 45)
    case = (a,)

    if case not in cases:
        cases.append(case)

cases.sort()

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
    yamldata[0]['contexts'].append( {'testcases' : []})
    # generate test expression
    # add input to input file
    stdin = '\n'.join(f'{line}' for line in test)

    # generate output to output file
    script = os.path.join(solutiondir, 'solution.nl.py')
    process= subprocess.run(
        ['python3', script],
        input=stdin,
        encoding='utf-8',
        capture_output=True
    )
    
    result_lines = process.stdout.split("\n")
    result_lines = [x for x in result_lines[:-1]] ## drop last element
    
    outputtxt = ""
    for line in result_lines:
        if not(line.startswith( 'Geef' ) or line.startswith( 'Voer' )):
            print(line)
            outputtxt += line + "\n"
            
    testcase = { input: stdin, output: outputtxt }            
    yamldata[0]['contexts'][i]["testcases"].append( testcase)


write_yaml(yamldata)