from evaluation_utils import EvaluationResult, Message

def hoger_lager( value, result, aantal ):
    if value > result:
        str = "Gok een getal: {}\n Hoger".format( value )
    elif value < result:
        str = "Gok een getal: {}\n Lager".format( value )
    else: # value == result
        str = "Gok een getal: {}\n Aantal pogingen: {}".format( value, aantal )
    return str        

def evaluate_value(expected, actual, args):
    inputs = args[0].split('\n')
    messages =  []
    for input in inputs:
        result = hoger_lager( input, inputs[-1], len( inputs ) )
        messages.append( Message( result ) )

    return EvaluationResult( True, expected, actual, messages )
