# importing libraries
import pandas as pd
import requests

# headers are often used to gain access to an otherwise locked API
HEADERS = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'Referer': 'http://stats.nba.com/player/',
    'Connection': 'keep-alive',
    'x-nba-stats-origin': 'stats'
}

# define function to be used
def get_data(url):
    response = requests.get(url, headers=HEADERS)
    while response.status_code != 200:
        response = requests.get(url)
    # explore the response in developers tools to find the proper arrangement of your json response
    headers = response.json()['resultSets'][0]['headers']
    data = response.json()['resultSets'][0]['rowSet']
    data = pd.DataFrame(data, columns=headers)
    return data

# define the url
url = 'http://stats.nba.com/stats/teamdetails?teamID=1610612741'

# get the pandas data frame
data = get_data(url)

# print rows of information with column names
# to only take the first five rows of a frame, use print(data.head(5))
print(data.head())


# once you have the data, you can save it simply to a csv
# to remove the index from the frame, indicate so as an argument
data.to_csv('team.csv', index=False)
