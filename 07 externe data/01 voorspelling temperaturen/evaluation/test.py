from evaluation_utils import EvaluationResult, ConvertedOracleContext, Message
import urllib.request

def check_function(context: ConvertedOracleContext, doel) -> EvaluationResult:
    
    # Get live data and calculate the needed result
    req = urllib.request.Request("https://api.open-meteo.com/v1/forecast?latitude=50.9384&longitude=4.0334&hourly=temperature_2m", 
                             headers={'User-Agent': 'Mozilla/5.0'})
    resp =  urllib.request.urlopen(req)
    data = eval(resp.read().decode().replace('false', 'False').replace('true', 'True'))

    temperaturen = data["hourly"]["temperature_2m"]
    
    aantal = -1
    for i in range(len(temperaturen)):
        temp = temperaturen[i]
        if temp >= doel[0] and aantal == -1:
            aantal = i

    if aantal == -1:
        readable_expected = f"De komende periode wordt het nooit {doel[0]} °C."
    else:
        readable_expected = f"Na {aantal} uur wordt het {doel[0]} °C."
    ## END OF THE PROGRAM
    
    
    value = context.actual == readable_expected

    obj = EvaluationResult(
        result = value,
        readable_actual = context.actual,
        readable_expected = readable_expected
    )

    return obj
