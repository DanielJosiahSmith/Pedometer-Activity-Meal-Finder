from django.http import JsonResponse
from .funcs import get_dinner_options


def dinner_options(request):
    """Provide one or two dinner options, more steps equal higher calorie meal options"""
    try:

        steps = request.GET.get('steps','0')
        meals = request.GET.get('num_of_meals','1')
        
        #validate steps 
        if steps.isdigit() and meals.isdigit():

            dinner_data = get_dinner_options(int(steps),int(meals))
            return JsonResponse(dinner_data)
        
        else:
            return JsonResponse({"error":"please provide steps and meals in number form ex.123"})
    except:
            return JsonResponse({"400":"bad request"})


