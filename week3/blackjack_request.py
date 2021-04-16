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
    (3, 12), # test0 
    (5, 5, 10), #test1
    (11, 10, 1),
    (1, 5),
    (1, 1, 5),
    (1, 1, 1, 7),
    (7, 8, 10)

]

# Boolean constants utilized in stand function
STAND_ON_SOFT = True
HIT_ON_SOFT = False

#payload for stand function
stand_payload = [
    # below stand on value, never stand
    (16, STAND_ON_SOFT, [5, 8]), # test0
    (16, HIT_ON_SOFT, [5, 8]), #test1
    # at stand on value, and the hand is hard, should stand either way
    (16, STAND_ON_SOFT, [5, 7, 2, 2]) #test3
    (16, HIT_ON_SOFT, [5, 7, 2, 2]),
    # at stand on value, and the hand is hard (but contains an ace), should stand either way
    (16, STAND_ON_SOFT, [5, 5, 5, 1]),
    (16, HIT_ON_SOFT, [5, 5, 5, 1]),
    # at stand on value, and the hand is soft
    (16, STAND_ON_SOFT, [5, 1]),
    (16, HIT_ON_SOFT, [5, 1]),
    # above stand on value, has ace, always stand
    (16, STAND_ON_SOFT, [3, 3, 1]),
    (16, HIT_ON_SOFT, [3, 3, 1]),
    # above stand on value, no ace, always stand
    (16, STAND_ON_SOFT, [5, 5, 3, 4]),
    (16, HIT_ON_SOFT, [5, 5, 3, 4])
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


# score_payload_results
# *********************
# test_0: total = 13, soft_aces = 0
# test_1: total = 20, soft_aces = 0
# test_2: total = 21, soft_aces = 0
# test_3: total = 16, soft_aces = 1
# test_4: total = 17, soft_aces = 1
# test_5: total = 20, soft_aces = 1
# test_6: total = 25, soft_aces = 0

# stand_payload_results
# *********************
# test_0: False
# test_1: False
# test_2: True
# test_3: True
# test_4: True
# test_5: True
# test_6: True
# test_7: False
# test_8: True
# test_9: True
# test_10: True
# test_11: True

