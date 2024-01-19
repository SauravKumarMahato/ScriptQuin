import openai
openai.api_key = "YOUR_API_KEY"


def generate_code_with_gpt(task_description ):
    try:
        # prompt = f"Generate code: {task_description}"
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613", 
            messages = [{"role": "system", "content" : "generate test script for below html in selenium using python"},
            {"role": "user", "content" : f"{task_description}"}]
        )

        return completion.choices[0].message.content
    except Exception as e:
        return str(e)

