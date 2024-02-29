import json
import requests
from API.config import base_url, token_headers, token_url, location_url
from API.creds import api_key, api_secret


def api_login():
    """This function logs into the API and returns a token."""

    auth_info = {
        'grant_type': 'client_credentials',
        'client_id': api_key,
        'client_secret': api_secret
    }

    response = requests.post(token_url, auth_info, headers=token_headers)
    response.raise_for_status()

    if response.status_code == 200:
        print("sucessfully fetched the token")
        responseData=json.loads(response.text)
        token = responseData['access_token']
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+ token
        }
    
        return headers
    print('An error occured when trying to log into the API.')


def retrieve_travel_info(source, destination, start_date, end_date, headers):
    """This functions calls the API and returns flight information based on the arguments."""

    parameters = {
        "originLocationCode": source,
        "destinationLocationCode": destination,
        "departureDate": start_date,
        "adults": 1,
        "returnDate": end_date
    }

    response = requests.get(base_url, params=parameters,headers=headers)

    if response.status_code == 200:
        print("sucessfully fetched the data with parameters provided")
        api_response =  json.loads(response.text)
        records = list_trip_options(api_response)        
        print(records)
        return records
    
    print(f"Error in retriving the flight information : {response.status_code} error with request.")


# Function still needs work.
def list_trip_options(api_response):
    """Function which parses API response and returns top 5 list of airfare choices based on price."""
    items = api_response["data"]

    # As of now we are returning top 5 records
    # This can be changed in future.
    """TODO : Need to add the sorting based on the price."""
    records = items[:5]
    return records

#Funtion to get the Airport details for source/destination dropdown.
def get_airport_list(keyword):
    parameters = {
        "subType": "AIRPORT,CITY",
        "keyword": keyword
    }
    
    response = requests.get(location_url, params=parameters,headers=api_login())

    if response.status_code == 200:
        print("sucessfully fetched the location/airport data with parameters provided")
        api_response =  json.loads(response.text)
        records = list_trip_options(api_response)        
        print(records)
        return records