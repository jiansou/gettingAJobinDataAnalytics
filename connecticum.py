import requests
import numpy
import pandas as pd
from bs4 import BeautifulSoup


companies = numpy.array([0])
URL = "https://www.connecticum.de/karrieremesse/firmen"

# Parse Data from URL and save them

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="mb30")
results.prettify()
job_elements = results.find_all("div", class_="name")

# Iterate all elements to find the company names
for job_element in job_elements:
    company_element = job_element.find("a", class_="dIB lineclamp")

    # Exception Handling: Some parsed attributes seem to be empty
    try:
        companies = numpy.append(companies, company_element.text.strip())
    except AttributeError:
        print("value was none-type")

# Create a DataFrame with numpyArray and save it to csv

df = pd.DataFrame(companies, columns=['Companies'])
df = df.iloc[1:, :]
df.to_csv('Jobmesse.csv')
