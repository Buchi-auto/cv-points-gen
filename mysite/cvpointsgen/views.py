from django.shortcuts import render
import openai
import os
import time
from parrot import Parrot

# Create your views here.
# openai.api_key = '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'
openai.api_key = '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'
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(model=model, messages=messages, temperature=0)
    return response.choices[0].message["content"]


def index(request):
    paraphrases = ["Result will be displayed here"]
    if request.method == "POST":
        project_name = request.POST['name']
        project_techstack = request.POST['tech']
        project_result = request.POST['result']
        project_num_points = request.POST['points']
        prompt = "Create {} crisp resume points for the project {} using the techstacks {} to achieve {} results. Give them in a paragraph separated by full stops.".format(str(project_num_points), str(project_name), str(project_techstack), str(project_result))
        values = get_completion(prompt)
        paraphrases = values.split("\n")
    return render(request, 'cvpointsgen/index.html', context={"context": paraphrases})