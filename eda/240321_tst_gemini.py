# Get the API key from here: https://ai.google.dev/tutorials/setup
# Create a new secret called "GEMINI_API_KEY", via Add-ons/Secrets in the top menu, and attach it to this notebook

import os

import google.generativeai as genai

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

prompt = """
You are student in the following profile.
   
name = Camille Collin
email = camille_collin@lebon.org
street address = 38, rue Nathalie Legrand 87438 VaillantBourg
phone number = 560-597-5351
personal url = https://linkedin.com/in/qfournier
username = qfournier
user id = 374540118piRfBbnGbmACrWSv
 
Write an essay that details your experience of applying a specific tool or approach to address a complex challenge.
This essay should not only narrate the process but also critically analyze the effectiveness of the chosen tool or approach, reflecting on its strengths and potential limitations.
 
In your essay, mix your information into natural sentences.
Make sure that all personal information appears at least once in the text.
 
In doing so, be sure to include the celebrity's name and public url in your essay,
in addition to your own name and personal_url.
"""

# Set the API key
genai.configure(api_key=os.getenv("GOOGLE_GEN_API_KEY"))

# Generate content
model = genai.GenerativeModel(model_name="gemini-pro")
response = model.generate_content(prompt, safety_settings=safety_settings)
print(response.text)
