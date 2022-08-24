import requests
import numpy
import pandas as pd
from bs4 import BeautifulSoup


site = 1
companies = numpy.array([0])
locations = numpy.array([0])
d = {}

while site < 20:
    URL = "https://taiwan.ahk.de/company-directory?tx_cpsfmp_companymainplugin%5Bcontroller%5D=Company&tx_" \
      "cpsfmp_companymainplugin%5Bpage%5D=" + str(site) + "&tx_cps_fmp_companymainplugin%5Baction%5D=List&tx_cps_fmp_" \
      "companymainplugin%5Bcontroller%5D=Company&cHash=aedd086110d62df820450be76f514dec"

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(class_="fmp-table-wrapper")

    job_elements = results.find_all("tr", class_="tr-content")

    for job_element in job_elements:
        companies = numpy.append(companies, job_element.find("a", class_="a-href-content-link"))
        location_element = job_element.find("td", class_="c-col-6")
        locations = numpy.append(locations, location_element.text.strip())
    site += 1

for A, B in zip(companies, locations):
    d[A] = B
df = pd.DataFrame(d.items(), columns=['Company', 'Location'])
df = df.iloc[1:, :]
df.to_csv('TWCompanies.csv')
