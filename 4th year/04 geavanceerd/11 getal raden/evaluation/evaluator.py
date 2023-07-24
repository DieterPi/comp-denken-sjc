from evaluation_utils import EvaluationResult, Message

def evaluate_value(expected, actual, args):
    
    return EvaluationResult(True, expected, actual, [Message("Test van de evaluatiefunctie")])
