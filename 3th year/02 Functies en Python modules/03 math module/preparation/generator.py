import os
import random
import subprocess
from typing import Text

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

# configuration settings
tab_name = 'Feedback'
settings = f'''
tab name: {tab_name}
python input without prompt: true
block count: multi
input block size: 3
output block size: ends with
comparison: exact match
'''

# generate test data
jongens = ['Ronar', 'Tiago', 'Uriel', 'Lars', 'Jules', 'Alec', 'Niels', 'Stan', 'Klaas', 'Iben', 'Timoer', 'Matteo', 'Mahmed', 'Louis', 'Thor', 'Boy', 'Ruben', 'Sem', 'Robin', 'Louis', 'Rik', 'Jarre', 'Lode', 'Nils', 'Simon', 'Jules', 'Noah', 'Wout', 'Igor', 'Lukas', 'Senne', 'Jef', 'Ward', 'Ryan', 'Stephan', 'Ali', 'Falco', 'Jean', 'Seppe', 'Louis', 'Louis', 'Elias', 'Jayson', 'Noah', 'Tom', 'Jaro', 'Silas', 'Maxime', 'Dylan', 'Leandro', 'Maxime', 'Reinoud', 'Roeland', 'Artuur', 'Andreas', 'Michiel', 'Robbe', 'Louis', 'Mauro', 'Kenzo', 'Tristan', 'Matteo', 'Rein', 'Tiemo', 'Bram', 'Mano', 'Tibo', 'Louis', 'Matteo', 'Tijl', 'Arne', 'Merlijn', 'Jarne', 'Michiel', 'Mats', 'Finn', 'Lennert', 'Adam', 'Wout', 'Henry', 'Viktor', 'Adil', 'Yannick', 'Arno', 'Arne', 'Henri', 'Tibo', 'Cédric', 'Jules', 'Lennert', 'Stan', 'Robin', 'Brent', 'Jelle', 'Roan', 'Lucas', 'Gedéon', 'Austin', 'León', 'Elias', 'Gaspard', 'Isaak', 'Eliot']
ntests= 20
cases = [('Louis','Jarre','Bram')]
while len(cases) < ntests:
    cases.append( (jongens[random.randint(0, len(jongens)-1)], jongens[random.randint(0, len(jongens)-1)], jongens[random.randint(0, len(jongens)-1)]) ) 

# configure test files
infile = open(os.path.join(evaldir, '0.in'), 'w')
outfile = open(os.path.join(evaldir, '0.out'), 'w')

# generate unit tests
for stdin in cases:

    # add input to input file
    stdin = '\n'.join(f'{line}' for line in stdin)
    print(stdin, file=infile)

    # generate output to output file
    script = os.path.join(solutiondir, 'solution.nl.py')
    process= subprocess.run(
        ['python3', script],
        input=stdin,
        encoding='utf-8',
        capture_output=True
    )
    
    result_lines = process.stdout.split("\n")
    for line in result_lines:
        if not(line.startswith( 'Geef' )):
            print(line)
            print(line, file=outfile, end='\n')

    # add stdout to output file
    # print(stdout, file=outfile, end='')

# add settings to output file
print('-' * 41 + settings, file=outfile, end='')
