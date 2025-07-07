from sqlalchemy.orm import sessionmaker
from trainer_functions.sqlalchemy_schema import Foods,Trainings,engine
from trainer_functions.data_models import FoodSchema, TrainingSchema
from pydantic import BaseModel


def add_food(food):
    Session = sessionmaker(bind=engine)
    session = Session()
    food_schema = FoodSchema(**food).model_dump()
    food_item = Foods(**food_schema)
    # add_food = Foods(
    #     food_name=food['food_name'],
    #     calories=food['calories'],
    #     protein=food['protein'],
    #     carbs=food['carbs'],
    #     fats=food['fats'],
    #     serving_g=food['serving_g']
    #     )
    session.add(food_item)
    session.commit()

def add_training(training):
    Session = sessionmaker(bind=engine)
    session = Session()

    training_schema = TrainingSchema(**training).model_dump()
    training_item = Trainings(**training_schema)

    # add_training = Trainings(
    #     exercise_name=training['exercise_name'],
    #     weight=training['weight'],
    #     reps=training['reps'],
    #     )

    session.add(training_item)
    session.commit()



