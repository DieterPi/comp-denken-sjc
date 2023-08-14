import os
import contextlib, io
import importlib
import random
import json

# set fixed seed for generating test cases
random.seed(123456789)

# locate evaldir
evaldir = os.path.join("..", "evaluation")
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join("..", "solution")
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

# load functionality defined in sample solution
module_name = "solution"
file_path = os.path.join(solutiondir, "solution.nl.py")
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def write_json( data:dict ):
    """ A function to write JSON file"""
    with open(os.path.join("..", "evaluation", "tests.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent = 2)

def construct_graph( connected = False, weight = 0, n_vertices = 0, n_edges = 0 ) -> dict:
    """ A function to construct a (possibly disconnected) random graph
    The implementation is not that good xD
    
    :param connected: boolean indicating if there can be vertices without connections.
    :param weight: int indicating if the graph should be weighted, if weighted then this
                   number is used as a max for the weight.
    """
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n_vertices == 0:
        n_vertices = random.randint(3, 10) # can be set to 26 for huge graphs
    V = []
    for i in range(n_vertices):
        V.append(alf[i])
        
    E = []
    E_simple = []
    if n_edges == 0:
        n_edges = random.randint(n_vertices, (n_vertices - 1)*n_vertices/2 )
    
    # construction of all possible edges, and then picking some at random
    all_E = []
    for v1 in V:
        for v2 in V:
            if v1 != v2:
                all_E.append( (v1, v2) )

    discount = 0
    if connected: # if all vertices must be present and connected in the graph
        V_copy = V.copy()
        v1 = random.choice( V_copy )
        V_copy.remove(v1)
        v2 = random.choice( V_copy )
        V_copy.remove(v2)
        E_simple.append( (v1, v2) )
        if weight != 0:
            E.append( (v1, v2, random.randint(2, weight)) )
        else:
            E.append( (v1, v2) )
        
        for i in range( n_vertices - 2):
            v1 = random.choice( E_simple )[random.randint(0,1)]
            v2 = random.choice( V_copy )
            V_copy.remove(v2)
            E_simple.append( (v1, v2) )
            if weight != 0:
                E.append( (v1, v2, random.randint(2, weight)) )
            else:
                E.append( (v1, v2) )

        discount = n_vertices - 1
    
    i = discount
    
    i = discount
    while i < n_edges:
        edge_c = random.choice( all_E )
        edge_c_inv = (edge_c[1], edge_c[0])
        if edge_c not in E_simple and edge_c_inv not in E_simple:
            E_simple.append( edge_c)
            i += 1
            if weight != 0:
                E.append( (edge_c[0], edge_c[1], random.randint(2, weight)) )
            else:
                E.append( (edge_c[0], edge_c[1]) )
        else: # remove this edge from all
            try:
                all_E.remove(edge_c)
                all_E.remove(edge_c_inv)
            except ValueError:
                pass
            
    return {"V": V, "E": E}


# generate test data
ntests = 20
cases = [ ( ['A','B','C','D','E'], 
            [('A','B',3), ('B','C',4),('C','D',2),('B','D',7),('B','E',8)] ),
          ( ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            [('A','D',5), ('A', 'B', 7), ('B','D',9), ('B','C',8), ('C','E',5), ('B','E',7), 
             ('D','E',15), ('D','F',6), ('F', 'E', 8), ('E', 'G',9), ('F','G',11)] ) ]

while len( cases ) < ntests:
    G = construct_graph(connected = True, weight = 20)
    cases.append( (G['V'], G['E']) )
    
# generate unit tests for functions
exportdata = {"tabs": [] }
exportdata["tabs"].append( {"name": "Feedback",
                            "contexts": [] } )
exportdata["tabs"][0]["contexts"].append({})
exportdata["tabs"][0]["contexts"][0]["testcases"] = []

for test in cases:
    # generate test expression        
    testcase = {"input": {"type": "function",
                          "name": "MST_prim",
                          "arguments": [
                              {"type": "list",
                               "data": [] },
                              {"type": "list",
                               "data": [] }]},
                "output": {} }
    
    for input in test[0]:
        testcase["input"]["arguments"][0]["data"].append({"type": "char",
                                                          "data": input })
    
    for input in test[1]:
        tuple_data = []
        for i in range( len(input) ):
            if i != 2:
                tuple_data.append( {"type": "char",
                                    "data": input[i] })
            else:
                tuple_data.append( {"type": "integer",
                                    "data": input[i] })
        testcase["input"]["arguments"][1]["data"].append({"type": "tuple",
                                                          "data": tuple_data })
    
    result = module.MST_prim( test[0], test[1] )

    # setup for return expressions
    testcase["output"]["result"] = {"value": {"type": "list", "data": [] }}
    
    for output in result:
        tuple_data = []
        for i in range( len(output) ):
            if i != 2:
                tuple_data.append( {"type": "char",
                                    "data": output[i] })
            else:
                tuple_data.append( {"type": "integer",
                                    "data": output[i] })
                
        testcase["output"]["result"]["value"]["data"].append({"type": "tuple",
                                                              "data": tuple_data})
    
    exportdata["tabs"][0]["contexts"][0]["testcases"].append( testcase )

write_json( exportdata )