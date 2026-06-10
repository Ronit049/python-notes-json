import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
import json

# code modularity, file divide krke manange krna hoga
# 1. role.json
# 2. responseformat.json


def generate_response(prompt):
    genai.configure(api_key=os.getenv("gemini_api_key"))
    response = genai.GenerativeModel("gemini-2.5-flash")
    output = response.generate_content(
        prompt
    )
    return output.text

try:
    with open("input/role.json", "r") as file:
        content = json.load(file)
        response = generate_response(str(content))
        print(response)
    with open("input/response.json", "r") as res_file:
        response_type = generate_response(str(json.load(res_file)))
    with open("input/prompt.txt" , "r", encoding="utf-8") as prompt_data:
        summerized_answer = generate_response(prompt_data.read())
        print(summerized_answer)

        
        
except FileNotFoundError as e:
    print("file not found")
