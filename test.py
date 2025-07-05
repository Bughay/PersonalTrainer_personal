from modules.chat_template import DeepseekChat

from dotenv import load_dotenv
import os
load_dotenv()  

api_key = os.getenv("DEEPSEEK_API_KEY")

prompt_1 = DeepseekChat.one_shot()