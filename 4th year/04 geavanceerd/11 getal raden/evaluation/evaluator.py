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
    
    flag = len( inputs ) == actual[-1]
    messages.append( Message(actual))
    messages.append( Message(isinstance(actual,str)  ))
    messages.append( Message("last -1: {}".format( actual[-1:] ) ) ) ## get last char
    messages.append( Message("last -2: {}".format( actual[-2:] ) ) ) ## get last char
    messages.append( Message("last -3: {}".format( actual[-3:] ) ) ) ## get last char
    messages.append( Message("last -4: {}".format( actual[-4:] ) ) ) ## get last char

    return EvaluationResult( flag, expected, actual, messages )
