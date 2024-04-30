import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)


def callGPT(prompt, model="gpt-3.5-turbo"):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant'},
            {'roel': 'user', 'content': prompt}
        ]
    )
    return completion


if __name__ == '__main__':
    result = callGPT('What are some famous astronomical observatories?')
    print(result)
