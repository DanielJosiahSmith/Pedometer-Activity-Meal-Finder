from django.conf import settings
import requests



def get_dinner_options(steps,num_of_meals):
    #API VARIABLES
    api_key = settings.SPOONACULAR_API_KEY
    base_url = settings.SPOONACULAR_BASE_URL

    #Calculate min and max calorie range for meal options
    min_calories, max_calories = calc_calories(steps,num_of_meals)

    filter = f'?&minCalories={min_calories}&maxCalories={max_calories}&number=2&random=true'

    #Build url
    url = f'{base_url}{filter}&apiKey={api_key}'

    #GET request from Spoonacular API
    resp = requests.get(url,timeout=10)


    if resp.status_code >= 400:
        data = {
            'error':'Try reducing your steps'
        }

    else:
        data = {
            'number of meals requested': num_of_meals,
            'range':f'per meal {min_calories}-{max_calories}',
            'options': resp.json()
            }

    return data


def calc_calories(steps,num_of_meals):
    """Calculates and returns min and max calorie allotement"""
    min_calories_base = 500
    max_calories_base = 1000

    #avg calorie burned per step
    burn_rate = .04
    additional_calories = int(steps * burn_rate)



    return (min_calories_base + additional_calories)/num_of_meals, (max_calories_base + additional_calories)/num_of_meals

    """
    Test # 1example if steps 5000, and num_of meals 1 = expected result
         results = calc_calories(5000,1)
         test_result = assert(expected_results,results)

         if test_result:
            pass test
        else:
            fail test

    Test # 2 example if steps 5000, and num_of meals 1 = unexpected result

         results = calc_calories(5000,1)
         test_result = assertfail(expected_results,results)

         if test_result:
            pass test
        else:
            fail test
    """



