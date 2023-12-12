# create .env file

from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()  # Load environment variables from a .env file into the os.environ dictionary

api_key = os.environ['OPENAI_API_KEY']
client = OpenAI(api_key=api_key)

def open_file(filepath):
  with open(filepath, 'r') as f:
    return f.read()

def save_file(filepath, content):
  with open(filepath, 'w') as f:
      f.write(content) 

def complete(prompt):
    response = client.completions.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        temperature=1,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text = response.choices[0].text.strip()

    token_dict = {
        'prompt_tokens':response['usage']['prompt_tokens'],
        'completion_tokens':response['usage']['completion_tokens'],
        'total_tokens':response['usage']['total_tokens'],
        }

    return text, token_dict

complete(prompt)
print(token_dict)


# combined
messages =  [  
{'role':'system',
 'content':"""You are an assistant who \
responds in the style of Dr Seuss. \
All your responses must be one sentence long."""},    
{'role':'user',
 'content':"""write me a story about a happy carrot"""},
] 
response = get_completion_from_messages(messages, 
                                        temperature =1)
print(response)