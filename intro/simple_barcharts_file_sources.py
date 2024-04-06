import csv
import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
from collections import Counter

# Applies a style
plt.style.use("fivethirtyeight")

# First uses the csv module from the standard library to load the dataset in CSV: data.csv
with open('intro/resources/data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # Instantiate a Counter (dict wrapper) for languages field in the CSV file
    language_counter = Counter()
    # Loop over every row in the csv file contents and use the Counter to keep track of languages counted
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

# Print counter to inspect and confirm we have coherent data
# print(language_counter)

# Counter built-in method provides functionality to retrieve from it the most common value
print(f"Most common language: ${language_counter.most_common(15)}") # 15 most common responses

# To plot the above info, we need to SPLIT languages and counts into their own separate lists
languages = []
popularity = []

#A lengthier, though more readable code wise, is the following:
for language_tuple in language_counter.most_common(15):
    languages.append(language_tuple[0])
    popularity.append(language_tuple[1])

# To plot as to read max-min values from top-bottom, we can reverse the lists
languages.reverse()
popularity.reverse()

# BELOW: Using pandas library to process the information
data = pd.read_csv('intro/resources/data.csv')
responder_id = data['Responder_id']
languages_pd = data['LanguagesWorkedWith']
counter_pd = Counter()

# Below could also be filtered with pandas and aggregate functions (like group_by and counter)
for panda_row in languages_pd:
    counter_pd.update(panda_row.split(';'))

# A Horizontal Bar Chart can make the dataset be more readable, due to its nature
# plt.barh(languages, popularity)

languages_pd = []
popularity_pd = []

# Plot the pandas' base counter, should look the same as above commented code
for language_tuple in counter_pd.most_common(15):
    languages_pd.append(language_tuple[0])
    popularity_pd.append(language_tuple[1])

languages_pd.reverse()
popularity_pd.reverse()

plt.barh(languages_pd, popularity_pd)

# # Uses a legend
plt.legend()

# Adds titles and legends
plt.title('Languages and Popularity')
plt.xlabel('Usage Count (Number of People)')

plt.tight_layout()

# # Finally, displays plot
plt.show()
