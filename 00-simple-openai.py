import openai
import os

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

customer_style = """American English \
in a calm and respectful tone
"""

customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse, \
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

prompt = f"""Translate the text \
that is delimited by triple backticks 
into a style that is {customer_style}.
text: ```{customer_email}```
"""

def get_completion(prompt, model="gpt-4o"):
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

print(get_completion(prompt))