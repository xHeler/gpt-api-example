import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

api_endpoint = 'https://api.openai.com/v1/chat/completions'

prompt = 'Translate the following English text to Polish: "Hello, how are you?"'

max_tokens = 50

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}

data = {
    'model': 'gpt-3.5-turbo',
    'messages': [{
        'role': 'system',
        'content': 'You are a helpful assistant.'
    }, {
        'role': 'user',
        'content': prompt
    }],
    'max_tokens': max_tokens,
}

response = requests.post(api_endpoint, headers=headers, json=data)

if response.status_code == 200:
    content = response.json()['choices'][0]['message']['content']
    print(content)
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
