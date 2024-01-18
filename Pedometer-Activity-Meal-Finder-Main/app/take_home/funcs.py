from django.conf import settings
import requests



def get_dinner_options(steps):
    #API VARIABLES
    api_key = settings.SPOONACULAR_API_KEY
    base_url = settings.SPOONACULAR_BASE_URL

    #Calculate min and max calorie range for meal options
    min_calories, max_calories = calc_calories(steps)

    filter = f'?&minCalories={min_calories}&maxCaloreis=1000&number=2&random=true'

    #Build url
    url = f'{base_url}{filter}&apiKey={api_key}'

    #GET request from Spoonacular API
    resp = requests.get(url,timeout=10)

    data = {
        'range':f'{min_calories}-{max_calories}',
        'options': resp.json()
        }

    return data


def calc_calories(steps):
    """Calculates and returns min and max calorie allotement"""
    min_calories_base = 500
    max_calories_base = 1000

    #avg calorie burned per step
    burn_rate = .04
    additional_calories = int(steps * burn_rate)

    return min_calories_base + additional_calories, max_calories_base + additional_calories

