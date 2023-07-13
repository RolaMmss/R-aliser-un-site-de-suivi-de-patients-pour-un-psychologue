
import requests

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-emotion-multilabel-latest"
headers = {"Authorization": f"Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "I like you. I love you",
})
print(output[0][0]['label'])

# import requests

# API_URL = "https://api-inference.huggingface.co/models/michellejieli/emotion_text_classifier"
# headers = {"Authorization": "Bearer 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"}

# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()
	
# output = query({
# 	"inputs": "I like you. I love you",
# })

# print(output)