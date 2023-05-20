<!-- ABOUT THE PROJECT -->
## About The Project

This project is meant to make a schedulable Python script that will send you an email alert through gmail of the newest movies from your local AMC theater with an IMDB rating of 7.0 or higher.

### Built With

* Python

<!-- GETTING STARTED -->
## Getting Started

1. Create a gmail API key that bypasses 2 factor authentication. Watch the video below on how to do that:
    https://www.youtube.com/watch?v=g_j6ILT-X0k

    Use the password in the next step in the .env file for configuration.

2. Configure the .env file according to your parameters:

    ```ACC_USERNAME='your_email@gmail.com'```

    ```PASSWORD=your_password```

    ```RECIPIENT_EMAIL="your_recipient_email""```

    ```AMC_LINK="your_local_amc_link"```

Files:
* movies.py - this is the main Python file.
* .env - this is used by dotenv library to pass environment variables of your gmail username and password, recipient eamil address, and your local AMC theater link into the movies.py file.
* requirements.txt - this contains a list of libraries and their versions which you'll need installed in order to run movies.py.

### Prerequisites

* Python 3.11.1
* Gmail account
* Gmail API key
* Chrome web browser
* Libraries installed from requirements.txt

### Installation

1. Download the movies.py, .env, and requirements.txt files in a new project folder
2. Download the required libraries to run this script by running this command ```pip install -r requirements.txt``` in your IDE
3. If you are on Windows, use Task Scheduler to schedule this script to run on a desired recurrence