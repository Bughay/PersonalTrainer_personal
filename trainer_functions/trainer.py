from modules.chat_template import DeepseekChat
from modules.deep_seek_extraction import DeepseekExtractor
from trainer_functions.config import example_schema, extraction_prompt, extraction_schema, separate_food_prompt,separate_training_prompt,extraction_schema_training,example_schema_training
from openai import OpenAI
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()  

api_key = os.getenv("DEEPSEEK_API_KEY")



def extract_food(user_message):
    chat = DeepseekChat(api_key,separate_food_prompt)

    text = chat.one_shot(user_message)

    print(text)

    test = DeepseekExtractor(text,extraction_prompt,extraction_schema,example_schema,api_key)

    extracted = test.extract()
    print('We have successfully extracted this data')
    print('--------------------------------------------------')
    print(extracted)
    print('---------------------------------------------')

    return extracted

def extract_training(user_message):
    chat = DeepseekChat(api_key,separate_training_prompt)
    text = chat.one_shot(user_message)
    print(text)

    test = DeepseekExtractor(text,extraction_prompt,extraction_schema_training,example_schema_training,api_key)
    extracted = test.extract()
    print('We have successfully extracted this data')
    print('--------------------------------------------------')
    print(extracted)
    print('---------------------------------------------')

    return extracted

def insert_food_items(json_extracted):
    """
    Inserts food items into trainer.db
    - Uses user_id = 1 for all entries
    - Follows the exact food table schema
    - Includes current timestamp
    """
    conn = sqlite3.connect('trainer.db')
    cursor = conn.cursor()
    
    for item in json_extracted:
        cursor.execute('''
            INSERT INTO food (
                user_id,
                type_food,
                serving_g,
                calories,
                protein,
                carbs,
                fats,
                date_added
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''), (
            1,  # Fixed user_id
            item['type_food'],
            item['serving_g'],
            item['calories'],
            item['protein'],
            item['carbs'],
            item['fats'],
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
    
    conn.commit()
    conn.close()
    print(f"Inserted {len(json_extracted)} items")