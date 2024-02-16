#!/usr/bin/env python3
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException


class LotteryAutomator:
    """Automates the process of selecting lottery numbers on the Caixa lottery website."""

    URL_TERMS_OF_USE = "https://www.loteriasonline.caixa.gov.br/silce-web/#/termos-de-uso"
    URL_MEGA_SENA = "https://www.loteriasonline.caixa.gov.br/silce-web/#/mega-sena"
    URL_QUINA = "https://www.loteriasonline.caixa.gov.br/silce-web/#/quina"

    def __init__(self, driver):
        self.driver = driver

    def navigate_and_accept_terms(self):
        """Navigates to the terms of use and accepts them."""
        self.driver.get(self.URL_TERMS_OF_USE)
        accept_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "botaosim"))
        )
        accept_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://www.loteriasonline.caixa.gov.br/silce-web/#/home")
        )

    def create_lottery_tickets(self, url, ticket_numbers):
        """Creates lottery tickets for either Mega Sena or Quina based on the provided URL and numbers."""
        for numbers in ticket_numbers:
            self.driver.get(url)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "ul.escolhe-numero li a.ng-binding"))
            )
            for number in numbers:
                number_element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f"//a[text()='{number:02d}']"))
                )
                number_element.click()
            add_to_cart_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "colocarnocarrinho"))
            )
            add_to_cart_button.click()

    def load_games_from_file(self, filepath):
        """Loads game numbers from a CSV file."""
        games = []
        with open(filepath, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                game = [int(number) for number in row]
                games.append(game)
        return games

    def run(self, mega_path, quina_path):
        """Runs the entire automation process for both Mega Sena and Quina lotteries."""
        self.navigate_and_accept_terms()
        mega_games = self.load_games_from_file(mega_path)
        quina_games = self.load_games_from_file(quina_path)
        self.create_lottery_tickets(self.URL_MEGA_SENA, mega_games)
        self.create_lottery_tickets(self.URL_QUINA, quina_games)

        while self.driver.window_handles:
            pass

def browser(mega_path, quina_path):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    with webdriver.Chrome(options=options) as driver:
        automator = LotteryAutomator(driver)
        try:
            automator.run(mega_path, quina_path)
        except WebDriverException as e:
            print(f"An error occurred: {e}")
        finally:
            driver.quit()
