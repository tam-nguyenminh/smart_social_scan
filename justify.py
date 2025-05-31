import pandas as pd
from openai import OpenAI
import json
from sklearn.preprocessing import MinMaxScaler
# create a def to read json file
def read_json(file_path):
    with open(file_path, 'r',encoding='utf-8') as f:
        data = json.load(f)
        # print(data)
        # Convert the JSON data to a DataFrame
        df = pd.DataFrame(data)
    return df

def read_key_value(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        secrete_key_value = data['secrete_key']
        # print(secrete_key_value)
        return secrete_key_value
    
def call_prompt(prompt_data, secret_key=None):
    df_post = prompt_data
    # calculate impact score of views*0.05 + likes*0.1 + comments*0.2 + shares*0.3
    scaler = MinMaxScaler()
    # Scale the numerical columns

    impact_score= (df_post['views'] * 0.05 + df_post['reactions'] * 0.1 + df_post['comments'] * 0.2 + 
                            df_post['shares'] * 0.3)
    df_post['impact_score'] = scaler.fit_transform(impact_score.values.reshape(-1, 1))
    client = OpenAI(api_key=secret_key)
    instruction = "Justify the risk of the post content with what it relates to and the risk. No preamble. " \
    "No more than 3 sentences. No break lines needed. Here is the content: "
    results = []
    for idx, row in prompt_data.iterrows():
        # print(row['content'])
        content = row['content']
        prompt = f'{instruction} {content}'
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": prompt}
        ]
        )
        # print(completion.choices[0].message)
        results.append(completion.choices[0].message.content)
    df_post['justify_risk'] = results
    
        
    return df_post


if __name__ == "__main__":
    path = 'smart_social_scan'
    # Read the key-value pairs from the file
    key_value = read_key_value(path + '/secrete.json')
    # read post dada from json file
    post_data = read_json(path + '/post.json')
    # Call the prompt with the post data and secret key
    response = call_prompt(post_data, secret_key=key_value)
    # Save the response to a new JSON file
    response.to_json(path + '/post_justified.json', orient='records', force_ascii=False, indent=4)
    print("done justifying")
    