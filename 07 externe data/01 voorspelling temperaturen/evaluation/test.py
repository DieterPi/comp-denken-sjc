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
        if temp >= doel and aantal == -1:
            aantal = i

    if aantal == -1:
        print(f"De temperatuur {doel} °C wordt in de nabije toekomst niet bereikt.")
    elif aantal == 0:
        print(f"Om middernacht was het al {doel} °C.")
    elif aantal == 1:
        print(f"De temperatuur {doel} °C wordt bereikt na 1 uur.")
    else:
        print(f"De temperatuur {doel} °C wordt bereikt na {aantal} uren.")
    ## END OF THE PROGRAM
    
    
    value = context.actual.strip() == readable_expected.strip()

    obj = EvaluationResult(
        result = value,
        readable_actual = context.actual,
        readable_expected = readable_expected
    )

    return obj
