import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Function to load more movies
def load_more_movies(driver, target_count):
    while True:
        movies_count = len(driver.find_elements(By.CSS_SELECTOR, "div.js-tile-link"))
        if movies_count >= target_count:
            break

        try:
            load_more_button = driver.find_element(
                By.CSS_SELECTOR, "div.discovery__actions button"
            )
            load_more_button.click()
            time.sleep(2)  # Wait for the content to load
        except Exception as e:
            logging.info("No more movies to load or error occurred: {}".format(e))
            break


# Main function to scrape data
def scrape_rottentomatoes_movies(target_count):
    url = "https://www.rottentomatoes.com/browse/movies_at_home/sort:popular"
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless browser
    chrome_options.add_argument("--disable-gpu")
    service = Service(
        r"C:\Users\marks\Downloads\chromedriver-win64\chromedriver.exe"
    )  # Provide the path to your chromedriver

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)

    load_more_movies(driver, target_count)

    soup = BeautifulSoup(driver.page_source, "lxml")
    driver.quit()

    movies = []
    critics_scores = []
    audience_scores = []

    movie_divs = soup.find_all("div", {"class": "js-tile-link"})

    for ix, movie_div in enumerate(movie_divs):
        if ix >= target_count:
            break

        # Extract movie name
        movie_name_tag = movie_div.find("span", {"class": "p--small"})
        movie_name = movie_name_tag.text.strip() if movie_name_tag else "N/A"

        # Extract critics score
        critics_score_tag = movie_div.find("rt-text", {"slot": "criticsScore"})
        critics_score = critics_score_tag.text.strip() if critics_score_tag else "N/A"

        # Extract audience score
        audience_score_tag = movie_div.find("rt-text", {"slot": "audienceScore"})
        audience_score = (
            audience_score_tag.text.strip() if audience_score_tag else "N/A"
        )

        # Append the data to lists
        movies.append(movie_name)
        critics_scores.append(critics_score)
        audience_scores.append(audience_score)

    # Create a DataFrame to store the results
    df = pd.DataFrame(
        {
            "Movie Name": movies,
            "Critics Score": critics_scores,
            "Audience Score": audience_scores,
        }
    )

    # Save the DataFrame to a CSV file
    df.to_csv("rottentomatoes_movies.csv", index=False)

    logging.info(
        "Scraping completed successfully. Data saved to 'rottentomatoes_movies.csv'"
    )


if __name__ == "__main__":
    target_count = int(input("Enter the number of movie rows to scrape: "))
    scrape_rottentomatoes_movies(target_count)

