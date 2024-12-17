#!/usr/bin/env python3
import csv

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LotteryAutomator:
    """Automates the process of selecting lottery numbers on the Caixa lottery website."""

    URL_TERMS_OF_USE = (
        "https://www.loteriasonline.caixa.gov.br/silce-web/#/termos-de-uso"  # noqa
    )
    URL_MEGA_SENA = (
        # "https://www.loteriasonline.caixa.gov.br/silce-web/#/mega-sena"  # noqa
        "https://www.loteriasonline.caixa.gov.br/silce-web/#/mega-sena/especial"  # noqa
    )
    URL_QUINA = "https://www.loteriasonline.caixa.gov.br/silce-web/#/quina"  # noqa

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
            print(f"Acessando a URL: {url}...")
            self.driver.get(url)
            print(f"Aguardando carregar os números...")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, "ul.escolhe-numero li a.ng-binding")
                )
            )
            for number in numbers:
                print(f"Clicando no número {number}")
                number_element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, f"//a[text()='{number:02d}']")
                    )
                )
                number_element.click()
            add_to_cart_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "colocarnocarrinho"))
            )
            print("Adicionando jogos no carrinho...")
            add_to_cart_button.click()

    def load_games_from_file(self, filepath):
        """Loads game numbers from a CSV file."""
        games = []
        with open(filepath, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                game = [int(number) for number in row]
                games.append(game)
        return games

    def run(self, mega_path, quina_path):
        """Runs the entire automation process for both Mega Sena and Quina lotteries."""
        print("Aceitando os termos de uso...")
        self.navigate_and_accept_terms()
        print("Carregando os jogos da Mega Sena...")
        mega_games = self.load_games_from_file(mega_path)
        print(mega_games)
        print("Carregando os jogos da Quina...")
        quina_games = self.load_games_from_file(quina_path)
        print(mega_games)
        print("Criando os jogos da Quina...")
        self.create_lottery_tickets(self.URL_QUINA, quina_games)
        print("Criando os jogos da Mega Sena...")
        self.create_lottery_tickets(self.URL_MEGA_SENA, mega_games)

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
