"""
This program parses a wikipedia page and extracts the states and their capitals into an external text file.
"""

# Import libraries
from bs4 import BeautifulSoup
import requests

# Open the wiki page
opened_page = requests.get("https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States")

# Parse the page with BeautifulSoup
soup = BeautifulSoup(opened_page.text, 'html.parser')

# Find the table
table = soup.find("table")

# Find the table body
tbody = table.find("tbody")

# Find all the table rows, which hold the state information
trs = tbody.find_all("tr")

# Remove the first 2 rows because they do not pertain to the states
del trs[:2]

states = []  # Declare states list to hold all states and their capital

# For each row take the state and capital from the title and add it to a list
for tr in trs:
    td = tr.findAll(name='td')[1]
    title = str(td).split('title="', 1)[1]
    title = str(title).split('">', 1)[0]
    states.append(title)

# Open a file if it doesnt exist and overwrite with the state information
file = open("states_file.txt", "w")
for state in states:
    file.write(state + "\n")

# Close the file
file.close()
