<!-- ABOUT THE PROJECT -->
## About The Project

This project is meant to make a schedulable Python script that will send you an email alert through gmail of the newest movies from your local AMC theater with an IMDB rating of 7.0 or higher.


### Built With

* Python


<!-- GETTING STARTED -->
## Getting Started

1. In the source code, replace the AMC link with the link of your local AMC theater on the page after you click "find your tickets" and where the option at the top has a drop down "all movies"
2. Change the value on line 128 with your email address:
    ```msg["to"] = "youremail@gmail.com"```
3. Retrieve your gmail's API username and password and modify the .env file with your credentials
    ```ACC_USERNAME='youremail@gmail.com'
       PASSWORD=yourpassword```
4. Replace the path in the service variable to the path of your chromedriver.exe
    ```service = pathlib.Path(
        r"C:\Users\kevin\OneDrive\Documents\Python\Web Scraping\chromedriver_win32\chromedriver.exe"
    )```
    
Files:
* movies.py - this is the main Python file.
* .env - this is used by dotenv library to pass environment variables of your gmail username and password into the movies.py file.
* requirements.txt - this contains a list of libraries and their versions which you'll need installed in order to run movies.py.

### Prerequisites

* Python 3.11.1
* Gmail account
* Gmail API key
* Chrome driver 
* Libraries installed from requirements.txt

### Installation

1. Download the movies.py, .env, and requirements.txt files in a new project folder
2. Download the required libraries to run this script by running this command ```pip install -r requirements.txt``` in your IDE
3. Download the chrome driver version that matches your google chrome version by going to https://chromedriver.chromium.org/downloads
4. If you are on Windows, use Task Scheduler to schedule this script to run on a desired recurrence