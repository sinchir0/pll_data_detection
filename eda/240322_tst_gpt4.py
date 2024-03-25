import openai

role_text = """You are the person in the following profile.

name = Camille Collin
email = camille_collin@lebon.org
street address = 38, rue Nathalie Legrand 87438 VaillantBourg
phone number = 560-597-5351
personal url = https://linkedin.com/in/qfournier
username = qfournier
user id = 374540118piRfBbnGbmACrWSv
"""

input_str = """
Write an essay that details your experience of applying a specific tool or approach to address a complex challenge.
This essay should not only narrate the process but also critically analyze the effectiveness of the chosen tool or approach, reflecting on its strengths and potential limitations.

Please avoid tech as a topic for your essay.

In your essay, mix your information(name, email, street address, phone number, personal url, username, user id).
Please choose at random whether you would like your information to appear naturally in the text or at the beginning or end of the sentence.

Always include a celebrity and a famous URL in your essay in addition to your own name and personal_url.

Celebrity and Well-known URLs should be able to be determined from context."""

from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    # model="gpt-3.5-turbo",
    # model="gpt-3.5-turbo",
    model="gpt-4-0125-preview",
    messages=[
        {
            "role": "system",
            "content": role_text,
        },
        {
            "role": "user",
            "content": input_str,
        },
    ],
    max_tokens=1024,
    temperature=0.9,
)

print(completion.choices[0].message)
pass
