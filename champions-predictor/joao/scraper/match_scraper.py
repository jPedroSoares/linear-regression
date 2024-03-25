from typing import Dict, List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from data.team_ids import team_ids
from utils.formatting import getFormatedResult

def getMatchInfos() -> List[List[str]]:
    """
    Retrieves a list of team pairs for each match.

    Returns:
        List[List[str]]: A list containing sublists representing each match's teams.
    """ 
    matches: List[List[str]] = [
        ["bayern", "arsenal"],
        ["manchester_city", "real_madrid"],
        ["psg", "barcelona"],
        ["atletico_madrid", "borussia"]
    ]
    
    return matches

def getMatchRows(home_team: str, away_team: str, driver: WebDriver) -> List[WebElement]:
    """
    Retrieves match rows from a table containing all games between two teams.

    Args:
        home_team (str): The name of the home team.
        away_team (str): The name of the away team.
        driver (WebDriver): The Selenium driver used for web navigation.

    Returns:
        List[WebElement]: A list of row elements representing matches between the provided teams.
    """
    home_team_id = team_ids.get(home_team)
    away_team_id = team_ids.get(away_team)
    if home_team_id is not None and away_team_id is not None:
        driver.get('https://www.ogol.com.br/xray.php?equipa_id={}&equipa_vs_equipa_id={}'
                   .format(home_team_id, away_team_id))

        table = driver.find_element(By.XPATH, "//*[@id='DataTables_Table_2']/tbody")
        rows = table.find_elements(By.CLASS_NAME, 'parent')
        return rows
    else:
        return []

def scrapeMatches(driver: WebDriver, matches: List[List[str]]) -> List[Dict[str, Dict[str, str]]]:
    """
    Scrapes the results of all matches listed in the provided list of matches.

    Args:
        driver (WebDriver): The Selenium driver used for web navigation.
        matches (List[List[str]]): A list of pairs of team names.

    Returns:
        List[Dict[str, Dict[str, str]]]: A list of dictionaries with the formatted information for each match result.
    """
    results = []

    for match in matches:
        rows = getMatchRows(match[0], match[1], driver)
        
        for row in rows:
            result = getFormatedResult(row)
            results.append(result)

    return results
