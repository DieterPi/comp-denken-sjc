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


films = [
    ("The Shawshank Redemption", "SHAWSHNK"),
    ("The Godfather", "GODFATHR"),
    ("The Dark Knight", "DARKKNG"),
    ("Pulp Fiction", "PULPFICT"),
    ("Forrest Gump", "FORRSTGP"),
    ("Inception", "INCEPTN"),
    ("Fight Club", "FGHTCLUB"),
    ("The Matrix", "MATRIX"),
    ("The Lord of the Rings: The Fellowship of the Ring", "LOTRFEL"),
    ("The Lord of the Rings: The Return of the King", "LOTRRET"),
    ("Interstellar", "INTRSTLR"),
    ("Gladiator", "GLADIATR"),
    ("Jurassic Park", "JURSPARK"),
    ("The Lion King", "LIONKING"),
    ("Back to the Future", "BACKFUT"),
    ("The Silence of the Lambs", "SILNLMB"),
    ("Saving Private Ryan", "SAVPRYAN"),
    ("The Green Mile", "GRNMILE"),
    ("Avatar", "AVATAR"),
    ("Titanic", "TITANIC")
]

# generate test data
ntests= 20
cases = [("Dune: Part Two","DUNE", 3, "B17")]
seats = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
i = 0
while len(cases) < ntests:
    film = films[i][0]
    afk = films[i][1]
    zaal = random.randint(1,12)
    zetelplaats = seats[random.randint(0,len(seats)-1)] + str(random.randint(1,50))
    i += 1
    
    case = (film, afk, zaal, zetelplaats)
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

