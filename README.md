# GPT API - Example

# Setup environment
Copy .env.template to .env and pass your api key from openai website.

```shell
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

# Output

```json
{
  "id": "chatcmpl-7wX7oy3hu2DWbpQXitfmsGwUcfFu7",
  "object": "chat.completion",
  "created": 1694184712,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Cześć, jak się masz?"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 32,
    "completion_tokens": 9,
    "total_tokens": 41
  }
}
```
