import pandas as pd
import numpy as np

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
    def __init__(self, name, population, total_cases, case_timeline,total_deaths):
        self.name = name
        self.population = population
        self.total_cases = total_cases
        self.case_timeline = case_timeline
        self.total_deaths = total_deaths

def clean_data():
    temp_data = 





if __name__ == "__main__":
    # Example
    america = country("United States", 1000000, 23000, 200)
    print(america)