import pandas as pd
#import numpy as np

# STP = standard temperature and pressure
# SLP = Sea Level Pressure
# rh = relative Humidity
# prcp = Precipitation



class country:
    def __init__(self, name, population, total_cases, total_deaths):
        self.name = name
        self.population = population
        self.total_cases = total_cases
        self.total_deaths = total_deaths

    def __str__(self):
        return '{} has {} cases of COVID-19. Currently, this virus has taken the lives of {} people.'.format(self.name,self.total_cases,self.total_deaths)

class state:
    def __init__(self, name, population, total_cases, case_timeline,total_deaths):
        self.name = name
        self.population = population
        self.total_cases = total_cases
        self.case_timeline = case_timeline
        self.total_deaths = total_deaths

class county:
    def __init__(self, name, state, population, total_cases, case_timeline,total_deaths):
        self.name = name
        self.population = population
        self.state = state
        self.total_cases = total_cases
        self.case_timeline = case_timeline
        self.total_deaths = total_deaths



def clean_data():
    # Create dataframe and select United States Only
    # Drop unneeded Columns
    us_temp_data = pd.read_csv('training_data_with_weather_info_week_1.csv')
    us_temp_data.drop(['Id', 'day_from_jan_first', 'min', 'max', 'stp', 'slp', 'dewp', 'ah', 'wdsp', 'fog'], axis=1, inplace = True)   
    us_Temp = us_temp_data[us_temp_data['Country'] == 'US']

    # us_states_covid19_daily
    # us_counties
    
    
    # Create Dataframe and drop unneeded columns
    # Note: Active means infected but still alive
    global_dly_data = pd.read_csv('covid_19_clean_complete.csv')
    global_dly_data.drop(['Province/State', 'Lat', 'Long'], axis = 1, inplace = True)
    print(global_dly_data.head())
    
    # Information as of 6/9/2020
    # Global Totals
    g_total_data = pd.read_csv('worldometer_data.csv')
    g_total_data.drop(['NewCases', 'NewDeaths', 'NewRecovered'], axis = 1, inplace = True)
    print(g_total_data.head())




if __name__ == "__main__":

    clean_data()