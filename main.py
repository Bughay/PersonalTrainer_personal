from trainer_functions.trainer import extract_food,extract_training
from trainer_functions.sqlite import *
from trainer_functions.sqlalchemy_methods import add_food, add_training

def main():
    check = input('training or diet test? ')

    if check == 'training':

        training_prompt = 'Today i have performed 2 sets of bench press 100 kg for 10 reps ,after that i lowered the weight and did bench press again for 3 sets at 90kg for 15 reps. then did 3 sets pullups body weight for 15,10,8 reps. and finally finished off with dumbell curls 10 kg for 15 reps'
        training_extracted = extract_training(training_prompt)

        for exercise in training_extracted['training']:
            print(f'SUCCESFULLY SAVED INTO Training database: {exercise}')
            add_training(exercise)

    if check == 'diet':
        diet_prompt = "For breakfast, I had 100g of oats with 30g almond butter and 100g blueberries, plus a 50g boiled egg; for lunch, I ate 200g grilled chicken, 150g roasted sweet potatoes, 100g steamed broccoli, and 30g avocado; for dinner, I enjoyed 180g baked salmon, 200g mashed cauliflower, 120g sautéed spinach, and 20g olive oil; and for snacks, I had 100g Greek yogurt, 30g mixed nuts, and a 180g apple."

        diet_extracted = extract_food(diet_prompt)
        for food in diet_extracted['foods']:
            print(f'SUCCESFULLY ADDED FOOD TO DATABASE: {food}')
            add_food(food)
if __name__ == "__main__":
    main()






