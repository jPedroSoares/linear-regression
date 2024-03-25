from scraper.match_scraper import getMatchInfos, scrapeMatches
from scraper.web_driver import configWebDriver

def main():
    # Configurar o WebDriver
    driver = configWebDriver()

    # Obter informações das partidas e IDs das equipes
    matches = getMatchInfos()

    # Fazer scraping dos resultados das partidas
    results = scrapeMatches(driver, matches)

    # Imprimir os resultados formatados
    for result in results:
        print('{} {}-{} {}'.format(result["home_team"]["name"], 
                                    result["home_team"]["goals"],
                                    result["away_team"]["goals"],
                                    result["away_team"]["name"]))

    # Fechar o WebDriver
    driver.quit()

if __name__ == "__main__":
    main()
