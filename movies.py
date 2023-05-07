import os
import smtplib
from email.message import EmailMessage

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def amc_movies_alert(amc_theater_link: str, imdb_link: str) -> None:
    """Main function to send email of movies, ratings, and descriptions

    Web scrape AMC and IMDB links and email
    yourself a list of movies with an IMDB rating of >= 7.0

    Parameters
    ------------
        amc_theater_link: str
            The link to your local AMC theater
        imdb_link: str
            The link to IMDB's homepage
    """
    # get the driver for chrome browser
    driver = get_chrome_webdriver

    # open AMC link first and scrape a list of all movies from the dropdown
    movies = get_amc_movies(driver, amc_theater_link)

    # get the ratings and descriptions of each movie in a dict
    movie_dict = get_imdb_data(movies, driver, imdb_link)

    send_email_alert(movie_dict)


def get_chrome_webdriver() -> webdriver:
    """Create chrome webdriver using selenium to web scrape AMC and IMDB links

    Return a webdriver
    """
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver


def get_amc_movies(driver: webdriver, amc_theater_link: str) -> list:
    """Scrape a list of movies from the 'all movies" dropdown on AMC's website

    Return a list
    """
    driver.get(f"{amc_theater_link}")
    movie_dropdown = driver.find_element(By.ID, "showtimes-movie-title-filter")
    to_remove = ["All Movies", ""]
    # only grab the movies that don't have the above filter
    movies = [
        movie.text.strip()
        for movie in movie_dropdown.find_elements(By.TAG_NAME, "option")
        if movie.text not in to_remove
    ]
    # filter the list of movies further by removing duplicate movie names
    filtered_movies = []
    for i in range(len(movies)):
        # for example, we want 'guardians of the galaxy vol 3'
        # not 'guardians of the galaxy vol 3: private theater rental'
        if i == 0 or not movies[i].startswith(
            movies[i - 1]
        ):  # This checks whether the current movie's name does not start
            # with the name of the previous movie in the list
            filtered_movies.append(movies[i])
    return filtered_movies


def get_imdb_data(movies: list, driver: webdriver, imdb_link: str) -> dict:
    """Scrape the IMDB rating and description for each movie.

    Return a dictionary
    """
    # open a new tab for IMDB link
    driver.execute_script("window.open('{}');".format(imdb_link))
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)

    # create empty dictionary to store
    # movie as key and rating/description as list of values
    movie_dict = {}
    # loop through each movie and scrape the rating and description
    for movie in movies:
        try:
            # click the search bar and enter the name of the movie
            search_bar = driver.find_element(By.ID, "suggestion-search")
            search_bar.click()
            search_bar.send_keys(f"{movie}")

            # click the search button
            search_button = driver.find_element(By.ID, "suggestion-search-button")
            search_button.click()

            # loop through each search result element
            # and check if the title of the movie matches
            for result in driver.find_elements(
                By.CLASS_NAME, "ipc-metadata-list-summary-item__t"
            ):
                if result.text.lower() == movie.lower():
                    # click on the link to the movie's page
                    driver.execute_script("arguments[0].click();", result)
                    break
        except NoSuchElementException:
            pass

        # get the page_source and parse the HTML using BeautifulSoup
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")

        # scrape the rating and description and insert to movie_dict
        try:
            rating = soup.find("span", {"class": "sc-bde20123-1 iZlgcd"}).text.strip()
            description = soup.find(
                "span", {"class": "sc-5f699a2-0 kcphyk"}
            ).text.strip()
            movie_dict[movie] = [rating, description]
        except AttributeError:
            pass
    driver.quit()
    return movie_dict


def send_email_alert(movie_dict: dict) -> None:
    """Send email using movie_dict to construct message"""
    # Load the environment variables from the .env file
    load_dotenv()
    username = os.getenv("ACC_USERNAME")
    password = os.getenv("PASSWORD")

    # Format the values as a string with line breaks and paragraphs
    movies_text = ""
    MOVIE_RATING_THRESHOLD = 7.0
    for movie, values in movie_dict.items():
        rating, description = values
        # only grab movies that have an IMDB rating of 7 or higher
        if float(rating) >= MOVIE_RATING_THRESHOLD:
            movie_text = f"<p><b>{movie}:</b></p><p>IMDB Rating: {rating}</p><p>Description: {description}</p>"
            movies_text += movie_text

    # construct email
    msg = EmailMessage()
    msg.add_alternative(movies_text, subtype="html")
    msg["subject"] = "Movie Ratings and Descriptions"
    msg["to"] = "youremail@gmail.com"
    msg["from"] = username

    # send email
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # setting gmail requires
    server.login(username, password)
    server.send_message(msg)
    server.quit


if __name__ == "__main__":
    amc_theater_link = (
        r"https://www.amctheatres.com/showtimes/all/2023-05-05/amc-broadstreet-7/all"
    )
    imdb_link = r"https://www.imdb.com/"
    amc_movies_alert(amc_theater_link, imdb_link)
