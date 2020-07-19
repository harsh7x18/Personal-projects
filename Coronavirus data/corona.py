from covid import Covid
covid = Covid()     # change the source to worldometer if you want by - covid = Covid(source = "worldometer"), by default its John Hopkins University
data = covid.get_data()
# print(data) ... if you want to get all the information

countries = covid.list_countries()    # This comes in handy when you need to know the available names of countries 
# print(countries)

# Get Status By Country Name
India_cases = covid.get_status_by_country_name("India")
print(India_cases)

# Get Status By Country Id
India_cases = covid.get_status_by_country_id(27)
print(India_cases)

# Get Total Active Cases
active = covid.get_total_active_cases()
print(active)

# Get Total Confirmed Cases
confirmed = covid.get_total_confirmed_cases()
print(confirmed)

# Get Total Recovered Cases
recovered = covid.get_total_recovered()
print(recovered)

# Get Total Deaths
deaths = covid.get_total_deaths()
print(deaths)

