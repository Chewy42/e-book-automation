import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

class Bot():
    #Important Variables
    maxIters = 3
    niche = None

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
        print("Is this text acceptable? (yes/no))")
        return input()

    def generateSupervised(prompt, temperature, max_tokens):
        hasBeenApproved = False
        i = 0
        while hasBeenApproved is False or i >= maxIters:
            niche = generateText(
            prompt, 
            temperature, #temperature
            max_tokens, #max tokens
            )
            if approve(niche).lower() != 'no':
                hasBeenApproved = True
            i += 1
        return niche


if __name__ == "__main__":