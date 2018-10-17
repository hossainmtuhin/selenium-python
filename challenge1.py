# Problem Description
# Find out if there are any duplicate urls used in the josn placeholder photo data

import requests

url = 'http://jsonplaceholder.typicode.com/photos'

# get the data about the photos
response = requests.get(url)

# read that data into another variable
json_data = response.json()

# create a list for storing the url of each photo
url_list = []

for photo in json_data:
    url_list.append(photo['url'])

# how many items are in the url list
print(len(url_list))

# how many items are there if we turn that list into a set?
print(len(set(url_list)))

# $ python challenge1.py
# 5000
# 4996