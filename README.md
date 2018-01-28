# WebScraping

Setup instructions:

PyCharm IDE Setup

Download and install Pycharm from: https://www.jetbrains.com/pycharm/ 

If you are a student you can get a free license from JetBrain at: https://www.jetbrains.com/student/


User Defined Python Packages

1. Include the ____init____.py scirpts in each folder so that pyhton recoginizes the folder and scripts within your package.
  
   File can be found at: https://github.com/sealneaward/uoit-machine-learning/tree/master/tutorials/scraping

2. Create a setup.py script that includes the package information.
  
   File can be found at: https://github.com/sealneaward/uoit-machine-learning/tree/master/tutorials/scraping

3. Install your user defined packages.

   python setup.py build
   
   python setup.py install


Scraping:

1. Visit: http://stats.nba.com/team/1610612741/

2. Open developer tools in Chrome and change the settings to Network and XHR. Now refresh the page. 

3. Locate a file named "teamdetails?teamID=1610612..." and double-click on this. It will take you to a JSON formated text page at: http://stats.nba.com/stats/teamdetails?teamID=1610612741

4. Visit: https://github.com/sealneaward/uoit-machine-learning/tree/master/tutorials/scraping and locate the "api.ipynb" file. 

5. Change format of file to "api.py" and open.

6. Locate the URL command and insert the JSON url: http://stats.nba.com/stats/teamdetails?teamID=1610612741.

7. Run the program. The output should be a "team.csv" file. This file contains information on the Chicago Bulls NBA team, 
   such as: "TEAM_ID", "NICKNME", "YEAR FOUNDED", "CITY", "ARENA", "OWNER" and "HEAD COACH".
   
   
   *** Code, methodology and tutorial orignate from: https://github.com/sealneaward/uoit-machine-learning 
       and https://github.com/sealneaward/template-py ***
