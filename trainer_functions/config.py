extraction_prompt = """
                    You will be performing extraction of data from the text as a JSON file using the following schema
                    keep note that the key is the variable and the value is the description
"""
extraction_schema= {
    'food_name': 'The name of the food item',
    'calories': 'Calories per 100g (float)',
    'protein': 'Protein content per 100g (float)',
    'carbs': 'Carbohydrates per 100g (float)',
    'fats': 'Fat content per 100g (float)',
    'serving_g': 'Total grams consumed (int)'
}

extraction_schema_training = {
    'exercise_name': 'the name of the exercise performed e.g(benchpress, squats, pull ups)',
    'weight': 'what is the weight that was lifted in kilograms, IF THERE IS NO WEIGHT MENTIONED OR BODYWEIGHT IS MENTIONED THE ANSWER IS 0 .',
    'reps': 'how many repetitions where performed? e.g(benchpress 100kg for 10 reps) = 10 repetitions where performed',

}
example_schema = {
  "foods": [
    {
      "food_name": "chicken breast",
      "calories": 165.0,
      "protein": 31.0,
      "carbs": 0.0,
      "fats": 3.6,
      "serving_g": 270
    },
    {
      "food_name": "rice",
      "calories": 130.0,
      "protein": 2.7,
      "carbs": 28.0,
      "fats": 0.3,
      "serving_g": 125
    }
  ]
}

example_schema_training = {
    "training" : [
        {
            "exercise_name": 'bench_press',
            'weight' : 100,
            'reps' : 10
        },
        {
            "exercise_name": 'Squat',
            'weight' : 180,
            'reps' : 5           
        },
        {
            "exercise_name": 'pull_ups',
            'weight' : 0,
            'reps' : 10            
        }
    ]
}


separate_food_prompt = """I am trying to save every single food that I have eaten in order to count calories in the most accurate way. 
                          Your input will be the entire meal(s) that I have eaten and you should seperate it into a single ingrient and how many grams
                          Each line will be a single food group with how many grams of it was eaten.
                          If the food_name contains a space due to multiple words. make sure to add _
                          THE ONLY DATA IN YOUR ANSWER SHOULD BE THE FOOD NAME AND THE AMOUNT OF GRAMS EATEN
                          DO NOT SHARE ANY OTHER DATA
                          
                          <example>
                          <input>
                          I ate 150g of chicken breast with 215 grams white rice and 125 g banana. after that I went on to eat 140 g of tuna with 315 g potatoes.
                          <input/>
                          <output>
                          chicken_breast 150 grams
                          white_rice 215 grams
                          banana 125 grams
                          tuna 140 grams
                          potatoes 315 grams
                          <output/>
                          <example/>




                          """

separate_training_prompt = """I am trying to save every single exercise that I have performed in order to track my training accurately.  
                             Your input will be the entire workout session I completed and you should separate it into a single exercise name, the weight used, and the number of reps.  
                             Each line will contain one exercise with the weight lifted and reps completed.  
                             If the exercise_name contains spaces, replace them with underscores (_).  
                             THE ONLY DATA IN YOUR ANSWER SHOULD BE THE EXERCISE NAME, WEIGHT, AND REPS.  
                             DO NOT SHARE ANY OTHER DATA.  

                             <example>  
                             <input>
                             Today i have done 2 sets of bench press with 100 kg at 8 reps,
                             Afterwards, I have done 2 sets of pull ups for 15 reps with my body weight followed by on set of dumbell curls 15kg for 12 reps  
                             <input/>  
                             <output>  
                             bench_press 100 kg 8 reps
                             bench_press 100 kg 8 reps  
                             pullups 0 kg 5 reps  
                             pullups 0 kg 5 reps  
                             dumbbell_curls 15 kg 12 reps  
                             <output/>  
                             <example/>  
                             """

diet_test = "For breakfast, I had 150g of oats with 30g almond butter and 100g blueberries, plus a 50g boiled egg; for lunch, I ate 200g grilled chicken, 150g roasted sweet potatoes, 100g steamed broccoli, and 30g avocado; for dinner, I enjoyed 180g baked salmon, 200g mashed cauliflower, 120g sautéed spinach, and 20g olive oil; and for snacks, I had 100g Greek yogurt, 30g mixed nuts, and a 180g apple."
