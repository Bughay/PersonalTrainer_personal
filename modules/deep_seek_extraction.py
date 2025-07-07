from openai import OpenAI
from dotenv import load_dotenv
import os
import json

class DeepseekExtractor:
    def __init__(self,user_message,extraction_prompt,extraction_schema,example_schema,api_key):
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
        self.user_message = user_message
        self.extraction_prompt = extraction_prompt
        self.extraction_schema = extraction_schema
        self.example_schema = example_schema
        self.api_key = api_key

    def extract(self):
        response = self.client.chat.completions.create(
        model="deepseek-chat",
        messages=[
                {
                    "role": "system",
                    "content": f"""
                    <extraction_prompt>
                    {self.extraction_prompt}
                    </extraction_prompt>
                    <extraction_schema>
                    {self.extraction_schema}
                    </extraction_schema>

                    Stay true to the return format and do not deviate from it
                    <return_format>
                    {self.example_schema}
                    </return_format>
                                    """

                },
                {
                    "role": "user",
                    "content": self.user_message,
                },
            ],
            response_format={"type": "json_object"},
            temperature=0,
        )
        extracted_data = json.loads(response.choices[0].message.content)

        return extracted_data
    



    

