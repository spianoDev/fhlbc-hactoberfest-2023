# Hacktoberfest 2023

### Description of Concept

We want to build a flight application that allows users to enter starting location, target location, and date range. 
The program will then return the best times to buy flights.

#### MVP
The following list is what we consider to be a minimal viable product:

- Forecasting best date range (by month) for purchasing tickets (before/after)
- Checkbox that will tell you the best month in general (by year) but can be more specific
- Add a price range
- Limit to the number of results (top 10)
- Dropdown for the airports to travel to/from
- Best times to buy flights
- Cache results from the query

#### Future Features
The following are some initial features we would build out to enhance the MVP: 

- More granular date options
- Estimated costs for buying on dates
- Which airlines offer the best prices for the date range or in general
- Allow user to navigate to actual booking step
- Establish login for users
- Record users selection/past results

### Setting up Django

For the first iteration of this project's database, each user will have to establish a local postgres database to 
run Django. This means that saved data will vary from user to user, but the application should run for each of us. 
We will create a better collaborative solution later, but to get started, refer to the 
[database setup](https://www.spiano.dev/djangoTutorial/#database_setup) 
section of this 
[Django Tutorial](https://www.spiano.dev/djangoTutorial/). 
