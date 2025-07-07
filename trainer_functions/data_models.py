from pydantic import BaseModel, field_validator,ValidationError



class FoodSchema(BaseModel):
    food_name : str
    calories : float
    protein : float
    carbs : float
    fats : float
    serving_g : int

    @field_validator("calories",'protein','carbs','fats','serving_g')
    def greater_than_zero(cls,v,info:ValidationError):
        if v < 0:
            raise ValueError(f'{info.field_name} attribute needs to be greater or equal to 0')

class TrainingSchema(BaseModel):
    exercise_name: str
    weight: int
    reps: int

    @field_validator("weight","reps")
    def greater_than_zero(cls,v,info:ValidationError):
        if v < 0:
            raise ValueError(f'{info.field_name}attribute needs to be greater or equal to 0')

 