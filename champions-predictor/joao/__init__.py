from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.common.by import By
from typing import Dict, List, Tuple

def getMatchInfos () -> Tuple[Dict[str, int], List[List[str]]]:
    team_ids: Dict[str, int] = {
        "bayern": 108,
        "arsenal": 75,
        "manchester_city": 86,
        "real_madrid": 50,
        "psg": 127,
        "barcelona": 40,
        "atletico_madrid": 39,
        "borussia": 107
    }
    
    matches: List[List[str]] = [
        ["bayern", "arsenal"],
        ["manchester_city", "real_madrid"],
        ["psg", "barcelona"],
        ["atletico_madrid", "borussia"]
    ]
    
    return team_ids, matches

def configWebDriver() -> WebDriver:
    firefox_options = FirefoxOptions()
    firefox_options.add_argument('--headless')  # Execução em modo headless (sem interface gráfica)

    driver = Firefox(options=firefox_options)
    return driver

def getMatchRows(home_team: int, away_team: int, driver: WebDriver) -> List[WebElement]:
    driver.get('https://www.ogol.com.br/xray.php?equipa_id={}&equipa_vs_equipa_id={}'
               .format(home_team, away_team))

    table = driver.find_element(By.XPATH, "//*[@id='DataTables_Table_2']/tbody")
    rows = table.find_elements(By.CLASS_NAME, 'parent')
    return rows

def getFormatedResult(row: WebElement) -> Dict[str, Dict[str, str]]:
    home_team_element = row.find_element(By.CLASS_NAME, 'text.home')
    away_team_element = row.find_element(By.CLASS_NAME, 'text.away')
    goals_element = row.find_element(By.CLASS_NAME, 'result>a')
    goals = goals_element.text.split('-')
    home_goals = goals[0]
    away_goals = goals[1]
    result = {
        "home_team": {
            "name": home_team_element.text,
            "goals": home_goals
        },
        "away_team": {
            "name": away_team_element.text,
            "goals": away_goals
        },
    }
    return result

def main ():
    team_ids, matches = getMatchInfos()
    driver = configWebDriver()
    rows = getMatchRows(team_ids[matches[0][0]], team_ids[matches[0][1]], driver)
    
    print("Título da página:", driver.title)
    
    results = []

    for row in rows:
        result = getFormatedResult(row)
        
        results.append(result)
        print('{} {}-{} {}'.format(result["home_team"]["name"], 
                                result["home_team"]["goals"],
                                result["away_team"]["goals"],
                                result["away_team"]["name"]))

    driver.quit()
    
main()