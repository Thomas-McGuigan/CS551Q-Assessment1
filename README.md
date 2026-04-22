Project description:
This project is a Django/Python application designed to help analyze the performance of movies, specifically, their ratings (both from IMDB and MetaCritic), alongside their budget listed in USD.

The source of the data is a public domain data-set from kaggle.com (https://www.kaggle.com/datasets/shahjhanalam/movie-data-analytics-dataset/data), which was modified to better fit the purposes of the project, converting from SQLite to .csv, removing the genres table, alongside only importing the appropiate columns from each table.  This was done in order to both reduce the complexity of the project, as well as to reduce the amount of unnecessary information that is presented to the end user.



How to run:
1. Unzip the downloaded file and extract the folder within to a location of your choosing.
2. Open a Powershell window in the same directory as the extracted project where manage.py is located (Tip, you can type in "powershell" in the Windows Explorer address bar to quickly open Powershell in that directory)
3. Enter the following commands: "python3 -m venv .venv", ".\.venv\Scripts\Activate" and "python .\manage.py runserver".  This will initialize a Python virtual environment, enter the environment, and then start the server.
4. In a web browser of your choice, then navigate to the web address http://127.0.0.1:8000/ .


Basic usage instructions:
Upon navigating to the specified web address, you will immediately see the names of movies alongside relevant information pertaining to each entry, displayed in a list.  

From here, you can scroll to the bottom of the page and use the page navigation buttons to go forwards or backwards in the list.  You can also use the search bar at the top of the page to filter and search for specific entries in the list.

You can also log-in with a demo account.  No features are locked behind the log-in, and there is no registration feature available.  If you wish to log-in, you can use the demo credentials "johnmovielover/ilovemovies" or "janemovielover/ilovemovies".

Task completion checklist:

Data models and database design:
Partially implemented (no linked tables)

Data presentation and pages:
Fully implemented

Open data use:
Fully implemented

User accounts and interaction:
Partially implemented (no features for logged-in users)

Search/filtering and usability:
Partially implemented (Only a basic search feature is in place)

Code quality and project structure:
Fully implemented (code was made readable by incorporating sensible names for functions and variables)

Testing:
Not implemented

Documentation:
Fully implemented

Deployment Bonus:
Fully implemented (available at tmcguigan.pythoneverywhere.com)