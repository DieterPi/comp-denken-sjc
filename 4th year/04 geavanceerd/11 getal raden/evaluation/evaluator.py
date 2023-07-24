from evaluation_utils import EvaluationResult, Message

def hoger_lager():
    return "a"

def evaluate_value(expected, actual, args):
    #inputs = args.split('\n')
    
    return EvaluationResult(True, expected, actual, [Message( "ab" + args )])
