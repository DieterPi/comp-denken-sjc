from evaluation_utils import EvaluationResult, Message

def hoger_lager( value, result, aantal ):
    messages = []
    if value > result:
        messages.append( Message( "Gok een getal: {}".format(value) ) )
        messages.append( Message( "Hoger" ) )
    elif value < result:
        messages.append( Message( "Gok een getal: {}".format(value) ) )
        messages.append( Message( "Hoger" ) )
    else: # value == result
        messages.append( Message( "Gok een getal: {}".format(value) ) )
        messages.append( Message( "Aantal pogingen: {}".format(aantal) ) )
    return messages        

def evaluate_value(expected, actual, args):
    inputs = args[0].split('\n')
    messages =  []
    for input in inputs:
        result = hoger_lager( input, inputs[-1], len( inputs ) )
        messages.extend( result )
    
    messages.append( Message( expected))
    messages.append( Message( actual))
    
    flag = len( inputs ) == expected[-1]

    return EvaluationResult( flag, expected, actual, messages )
