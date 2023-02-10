import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

def generateText(prompt, temperature, tokens):
    res = openai.Completion.create(
        model="text-davinci-003", 
        prompt=prompt, 
        temperature=temperature, 
        max_tokens=tokens
    )
    return res.choices[0].text[2:]

def approve(generatedText):
    print("Generated Text:")
    print(generatedText)
    print("Is this text acceptable?\n")
    return input()


niche = None


hasBeenApproved = False
maxIters = 3
i = 0
while hasBeenApproved is False or i >= maxIters:
    niche = generateText(
    "randomly pick either Health and Welness, E-Commerce, or Relationships, then return back ONLY the one you have picked", 
    0.6, #temperature
    20) #max tokens
    if approve(niche).lower() != 'no':
        hasBeenApproved = True
    i += 1