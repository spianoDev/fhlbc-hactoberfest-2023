from API.travel_functions import api_login, retrieve_travel_info, get_airport_list

# DISCLAIMER
# Need to create a creds.py file within the API folder with the following keys and your own unique values


if __name__ == "__main__":
    headers = api_login()
    api_response = retrieve_travel_info("SYD", "BKK", "2024-03-29", "2024-03-29", headers=headers)
    print(api_response)

    # Function still needs more logic added.
    # list_trip_options(api_response)

   # Added as test to call the airport details for the source/destination dropdown.
    get_airport_list("vns")

    print ("program end")