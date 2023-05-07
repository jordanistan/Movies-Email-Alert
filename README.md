<!-- ABOUT THE PROJECT -->
## About The Project

This project is meant to make a schedulable Python script that will send you an email alert through gmail of the newest movies from your local AMC theater with an IMDB rating of 7.0 or higher.


### Built With

* Python


<!-- GETTING STARTED -->
## Getting Started

In the source code, replace the AMC link with the link of your local AMC theater on the page after you click "find your tickets" and where the option at the top has a drop down "all movies".

Retrieve your gmail's API username and password and modify the .env file with your credentials.

Files:
* movies.py - this is the main Python file.
* .env - this is used by dotenv library to pass environment variables of your gmail username and password into the movies.py file.
* requirements.txt - this contains a list of libraries and their versions which you'll need installed in order to run movies.py.

### Prerequisites

* Python 3.11.1
* Visual Studio Code
* Gmail account
* Gmail API key
* Libraries installed from requirements.txt

### Installation

Download the movies.py and .env files in a new project folder. In order to download the required libraries to run this script, you can run this command ```pip install -r requirements.txt``` in your terminal in Visual Studio Code.