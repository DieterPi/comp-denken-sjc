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

# generate test data
ntests= 20
namen = [
    "Lars", "Amira", "Yanis", "Mila", "Arne",
    "Sofie", "Tarek", "Noor", "Jonas", "Eline",
    "Kwame", "Alicia", "Santiago", "Nour", "Bram",
    "Ji-Yun", "Hamza", "Zara", "Rune", "Emil",
    "Khadija", "Luka", "Anaya", "Matteo", "Selim"
]
klassen = ["1LAa", "1LAb", "1LAc", "1LAd", "1LAe", "1MTWa", "1MTWb", "1MTWc", "1MTWd", "2GRLA", "2LAa",
           "2LAb", "2LAc", "2LAd", "2MTWa", "2MTWb", "2MTWc", "2MTWd", "2SPa", "2SPb", "3LAB1", "3LAB2", "3GRLAB", "3GRLAA", "3NAWE1",
           "3NAWE2", "3ECWEB", "3ECWEA", "3MT","3LAA","3HUWE", "3SPWE", "4LAB", "4GRLAB", "4GRLAA", "4NAWE1",
           "4NAWE2", "4ECWEB", "4ECWEA", "4MT","4LAA", "4HUWE", "3SPWE", "5GRIWA", "5GRWIB", "5GRLA", "5LAWIA", "5LAWIB",
           "5WEWIA", "5WEWIB1", "5WEWIB2", "5ECWI", "5ECMT", "5MT", "5HUWE", "5LAWE", "5LAMT", "6GRIWA", "6GRWIB", "6GRLA", "6LAWIA", "6LAWIB",
           "6WEWIA", "6WEWIB1", "6WEWIB2", "6ECWI", "6ECMT", "6MT", "6HUWE", "6LAWE", "6LAMT"]
cases = [("Louis", 4, "NAWE1", 15), ("Maram", 4, "LAB", 24) ]
while len(cases) < ntests:
    voornaam = random.choice(namen)
    klas = random.choice(klassen)
    jaar = int(klas[0])
    code = klas[1:]
    nr = random.randint(1,25)
    case = (voornaam, jaar, code, nr)
    if case not in cases:
        cases.append(case)


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
