import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nA:"
restart_sequence = "\n\nQ: "

def ai_resp(question):
  response = openai.Completion.create(
    engine="davinci",
    prompt=f"I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ:{question} A:",
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\n"]
  )
  return response

x=1

while x==1:
  qs = input("Q: ")
  ai_resp(qs)
  print(ai_resp.response)