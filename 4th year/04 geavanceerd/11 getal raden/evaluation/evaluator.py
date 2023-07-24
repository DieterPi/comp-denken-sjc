from evaluation_utils import EvaluationResult, Message

def hoger_lager( value, result, aantal ):
    if value > result:
        str = "Gok een getal: {}\nLager".format( value )
    elif value < result:
        str = "Gok een getal: {}\nHoger".format( value )
    else: # value == result
        str = "Gok een getal: {}\nAantal pogingen: {}".format( value, aantal )
    return str        

def evaluate_value(expected, actual, args):
    inputs = args[0].split('\n')
    msg = ""
    for input in inputs:
        msg += hoger_lager( input, inputs[-1], len( inputs ) )

    return EvaluationResult(True, expected, actual, [Message( msg )])
