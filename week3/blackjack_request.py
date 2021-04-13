'''
This example script will utilize the request libray to post a json payload
to a serverless function in the Azure environment. The response is a text output
for the return values for each test case in each payload.
'''

# library to interact with urls
import requests

# payload fed into score function
score_payload = [
    # Will need to get test cases from assignment
    # Example tuples in payload:
    #( 99, 99 ),
    #( 99, 99, 9 )

]

# Boolean constants utilized in stand function
STAND_ON_SOFT = True
HIT_ON_SOFT = False

#payload for stand function
stand_payload = [
    # below stand on value, never stand
    (16, STAND_ON_SOFT, [5, 8]),
    (16, HIT_ON_SOFT, [5, 8]) #,
    # at stand on value, and the hand is hard, should stand either way
    
    
    # at stand on value, and the hand is hard (but contains an ace), should stand either way
    
    
    # at stand on value, and the hand is soft
    
    
    # above stand on value, has ace, always stand
    
    
    # above stand on value, no ace, always stand
    
    
]

payload = {
    'score_payload' : score_payload,
    'stand_payload' : stand_payload
    }

response = requests.post(url='https://cs3006.azurewebsites.net/api/HttpExample', json = payload)

# response code. 200 is bueno
print(response)

#text output from serverless function
return_payload = response.text
print(return_payload)

