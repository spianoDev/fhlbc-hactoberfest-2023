import requests
import json

'''
To do list:
Add logic to retrieve_travel_info function - Anup
Add logic to list_trip_options function - ***Currently Unassigned*** 
'''

# Anup to build out this initially.
#Open file to get the client_id and client_secret.
#please create credential.txt file in your system and change the path accordingly.
# the credential file will contains id and secret
#example of credentail file:
#<<client_id value>>
#<<client_secret value>>

credential = open("c:\\code\credential.txt", "r") 

credentialData = credential.readlines()
#base url for flight data retrival
base_url="https://test.api.amadeus.com/v2/shopping/flight-offers"

#Code To generate the token.
tokenUrl = 'https://test.api.amadeus.com/v1/security/oauth2/token'
tokenHeaders = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

auth_info = {
    'grant_type': 'client_credentials',
    'client_id': credentialData[0].strip(),
    'client_secret': credentialData[1]
}
def retrieve_travel_info(source, destination, start_date, end_date):
    response = requests.post(tokenUrl,auth_info, headers=tokenHeaders)
    response.raise_for_status()

    if response.status_code == 200:
        print("sucessfully fetched the token")
        responseData=json.loads(response.text)
        token = responseData['access_token']
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+ token
        }
        
        parameters = {
            "originLocationCode": f"{source}",
            "destinationLocationCode": f"{destination}",
            "departureDate": f"{start_date}" ,
            "adults": 1,
            "returnDate": f"{end_date}"
        }

        response = requests.get(f"{base_url}", params=parameters,headers=headers)

        if response.status_code == 200:
            print("sucessfully fetched the data with parameters provided")
            return  json.loads(response.text)
        else:
            print(f"Error in retriving the flight information : {response.status_code} error with request.")
    else:
        print(f"Error with token generation:  {response.status_code} error with request.")
    pass
    return None

# Need a volunteer to add their name here, claim this function and make a push!
def list_trip_options(api_response):
    """Function which parses API response and returns top 5 list of airfare choices based on price."""
    pass
    return None

print (retrieve_travel_info("SYD","BKK","2023-12-02","2023-12-03"))
print ("prgram end")