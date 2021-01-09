from selenium import webdriver
from time import sleep
import pandas


class CovidTracker():
    def __init__(self):
        self.driver = webdriver.Chrome('/Users/Anrheas/PycharmProjects/chromedriver')
        categories = ['country', 'total cases', 'new cases', 'total deaths',
                      'active cases', 'critical cases','cases/million']
        self.df = pandas.DataFrame(columns=categories)

    def info_scrape(self):
        website = self.driver.get('https://www.worldometers.info/coronavirus/')
        table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]')
        country = table.find_element_by_xpath("//td[contains(., 'USA')]")
        row = country.find_element_by_xpath('./..')
        cell = row.text.split(" ")

        sleep(1)
        Country = cell[1]
        total_cases = cell[2]
        new_cases = cell[3]
        total_deaths = cell[4]
        active_cases = cell[7]
        critical_cases = cell[8]
        cases_milli = cell[9]



        self.df = self.df.append({
            'country': Country,
            'total cases': total_cases,
            'new cases': new_cases,
            'total deaths': total_deaths,
            'active cases': active_cases,
            'critical cases': critical_cases,
            'cases/million': cases_milli,

            }, ignore_index=True)

    def transfer_to_csv(self):
        self.df.to_csv('covid19-stats.csv', mode='a', header=False)

        self.driver.close()


CovidBot = CovidTracker()
CovidBot.info_scrape()
CovidBot.transfer_to_csv()
