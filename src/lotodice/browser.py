import csv
import signal
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LotteryAutomator:
    """Automates the process of selecting lottery numbers on the Caixa lottery website."""

    URL_TERMS_OF_USE = (
        "https://www.loteriasonline.caixa.gov.br/silce-web/#/termos-de-uso"
    )
    URL_MEGA_SENA = (
        "https://www.loteriasonline.caixa.gov.br/silce-web/#/mega-sena/especial"
    )
    URL_QUINA = "https://www.loteriasonline.caixa.gov.br/silce-web/#/quina"

    def __init__(self, driver):
        self.driver = driver

    def accept_terms(self):
        """Accepts the terms of use."""
        self.driver.get(self.URL_TERMS_OF_USE)
        accept_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "botaosim"))
        )
        accept_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://www.loteriasonline.caixa.gov.br/silce-web/#/home")
        )

    def select_numbers_and_add_to_cart(self, numbers):
        """Selects lottery numbers and adds them to the cart."""
        for number in numbers:
            try:
                print(f"Selecionando o número: {number}")
                xpath = f"//a[@id='n{number:02d}']"

                # Espera até o elemento estar presente e clicável
                number_element = WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )

                number_element.click()
            except Exception as e:
                print(f"Erro ao selecionar o número {number}: {e}")
                continue

        try:
            print("Adicionando os números ao carrinho...")
            add_to_cart_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.ID, "colocarnocarrinho"))
            )
            add_to_cart_button.click()
        except Exception as e:
            print(f"Erro ao adicionar ao carrinho: {e}")

    def load_games_from_file(self, filepath):
        """Loads game numbers from a CSV file."""
        games = []
        with open(filepath, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                games.append([int(num) for num in row])
        return games

    def create_lottery_tickets(self, url, games):
        """Navigates to a URL and creates lottery tickets."""
        for game in games:
            print(f"Acessando a URL: {url}...")
            self.driver.get(url)

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "escolhe-numero"))
            )
            self.select_numbers_and_add_to_cart(game)


def handle_exit(signum, frame):
    print("\nEncerrando o script e fechando o navegador...")
    sys.exit(0)


def browser(mega_path, quina_path):
    """Main method to execute the lottery automation."""

    if not mega_path and not quina_path:
        return
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    try:
        automator = LotteryAutomator(driver)

        # Accept terms
        print("Aceitando os termos de uso...")
        automator.accept_terms()

        if mega_path:
            # Process Mega Sena games
            print("Carregando jogos da Mega Sena...")
            mega_games = automator.load_games_from_file(mega_path)
            print("Criando jogos da Mega Sena...")
            automator.create_lottery_tickets(automator.URL_MEGA_SENA, mega_games)

        if quina_path:
            # process quina games
            print("carregando jogos da quina...")
            quina_games = automator.load_games_from_file(quina_path)
            print("criando jogos da quina...")
            automator.create_lottery_tickets(automator.URL_QUINA, quina_games)

        # Aguardar encerramento do script pelo usuário
        print(
            "\nAutomação concluída. Pressione Ctrl+C para encerrar o script e fechar o navegador."
        )
        signal.signal(signal.SIGINT, handle_exit)
        signal.signal(signal.SIGTERM, handle_exit)

        # Mantém o script em execução até o encerramento manual
        signal.pause()

    except Exception as e:
        print(f"Erro durante a execução: {e}")
    finally:
        driver.quit()
