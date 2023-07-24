import traceback

from evaluation_utils import EvaluationResult, Message

def evaluate_value(expected, actual, args):
    if isinstance(actual, ZeroDivisionError):
        # If a zero division error, show the stacktrace.
        formatted = "".join(traceback.format_exception(type(actual), actual, actual.__traceback__))
        return EvaluationResult(True, formatted, formatted)
    elif isinstance(actual, Exception):
        # If another error, show the stacktrace as well.
        formatted = "".join(traceback.format_exception(type(actual), actual, actual.__traceback__))
        return EvaluationResult(False, "ZeroDivisionError", formatted, [Message(f"Verwachtte een ZeroDivisionError, maar kreeg een {type(value).__name__}.")])
    else:
        # Else show the str of the value.
        actual = str(actual) if actual else ""
        return EvaluationResult(False, "ZeroDivisionError", actual, [Message("Verwachtte een ZeroDivisionError.")])
