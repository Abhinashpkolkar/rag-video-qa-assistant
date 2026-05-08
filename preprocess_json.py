import requests
import os
import json
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def create_embedding(text_list):
    # https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })

    embedding = r.json()["embeddings"] 
    return embedding


jsons = os.listdir("jsons")  # List all the jsons 
my_dicts = [] #Initiate an dictionary.
chunk_id = 0

for json_file in jsons:
    with open(f"jsons/{json_file}") as f:  # Open each json file one by one and load the content of the json file in a variable called content.
        content = json.load(f)
    print(f"Creating Embeddings for {json_file}")
    embeddings = create_embedding([c['text'] for c in content['chunks']])  # We made a list of all text in bulk and sent it to the create_embedding function which will return a list of embeddings for each text in the same order as the text list.

    # If we used individual texts then it might take lot of time. So we are using bulk texts to create embeddings which is much faster. 
       
    for i, chunk in enumerate(content['chunks']):
        chunk['chunk_id'] = chunk_id # we are adding a new key called chunk_id to each chunk which will be used later to identify the chunk in the dataframe.
        chunk['embedding'] = embeddings[i] # we are adding a new key called embedding to each chunk which will store the embedding of the text in that chunk. We are using the index i to get the corresponding embedding for each chunk.
        chunk_id += 1
        my_dicts.append(chunk) 

df = pd.DataFrame.from_records(my_dicts)
# Save this dataframe
joblib.dump(df, 'embeddings.joblib')

