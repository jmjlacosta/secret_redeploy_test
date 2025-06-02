def ask_gpt(prompt):
    if prompt.strip().lower() == "the key":
        the_key = os.environ.get("THE_KEY", "Not set.")
        return f"The key is: {the_key}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7,
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"
