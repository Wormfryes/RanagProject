import requests 

def gen(tofind):
    API_URL = "https://api-ranagproject.onrender.com/process"
    prompt = f"""
    <s>[INST] 
    You are a Code Bug Finder. Your task is to analyze the provided code, identify any syntax or logical errors, and suggest the correct version. 

    For each mistake, output it in the following format:
    £wrong_snippet£—¥correct_snippet¥

    Rules:
    1. Each error should be enclosed in `£` and `¥` as shown.
    2. Do NOT include nested corrections inside another correction.
    3. If multiple errors exist, list them separately in new lines.
    4. Preserve the original indentation and structure as much as possible.

    Example:

    Input code:

    print(hello world)
    variable = 10;

    def hello:
    print(“hello!”)

    Expected output:

    £print(hello world)£—¥print(“hello world”)¥
    £def hello:£—¥def hello():¥

    Now, analyze the following code and return the corrected snippets:

    {tofind}
    [/INST]"""
    
    data = {"prompt": prompt}

    response = requests.post(API_URL, json=data)
    if response.status_code == 200:
        resp = response.json()
        resp = resp['generated']
        return str(resp)
    else:
        return f"Error: {response.status_code}"

