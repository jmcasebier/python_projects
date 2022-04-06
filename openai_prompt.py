# imports
import os
import openai
# api key
openai.api_key = os.getenv("OPENAI_API_KEY")
# get prompt input
promptInput = input("Enter a prompt: ")
# get completion
response = openai.Completion.create(
    engine="davinci", prompt=promptInput, max_tokens=10)
# print completion
print(response)
