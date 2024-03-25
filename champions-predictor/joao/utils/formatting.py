from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import Dict

def getFormatedResult(row: WebElement) -> Dict[str, Dict[str, str]]:
    """
    Formats the result of a match.

    Args:
        row (WebElement): The row element of the match.

    Returns:
        Dict[str, Dict[str, str]]: A dictionary with the formatted information for the match result.
    """
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
