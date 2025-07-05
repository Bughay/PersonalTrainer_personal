from sqlalchemy.orm import sessionmaker
from trainer_functions.sqlalchemy_schema import Foods,Trainings,engine



def add_food(food):
    Session = sessionmaker(bind=engine)
    session = Session()

    add_food = Foods(
        food_name=food['food_name'],
        calories=food['calories'],
        protein=food['protein'],
        carbs=food['carbs'],
        fats=food['fats'],
        serving_g=food['serving_g']
        )

    session.add(add_food)
    session.commit()

def add_training(training):
    Session = sessionmaker(bind=engine)
    session = Session()

    add_training = Trainings(
        exercise_name=training['exercise_name'],
        weight=training['weight'],
        reps=training['reps'],
        )

    session.add(add_training)
    session.commit()