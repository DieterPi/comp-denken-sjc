from evaluation_utils import EvaluationResult, Message

def hoger_lager():
    pass

def evaluate_value(expected, actual, args):
    inputs = args.split('\n')
    
    return EvaluationResult(True, expected, actual, [Message(actual)])
