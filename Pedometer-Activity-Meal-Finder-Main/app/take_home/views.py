from django.http import JsonResponse
from .funcs import get_dinner_options


def dinner_options(request):
    """Provide one or two dinner options, more steps equal higher calorie meal options"""

    steps = request.GET.get('steps','0')
    
    #validate steps 
    if steps.isdigit():

        dinner_data = get_dinner_options(int(steps))
        return JsonResponse(dinner_data)
    
    else:
        return JsonResponse({"error":"please provide steps in number form ex.123"})


