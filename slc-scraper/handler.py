import mechanicalsoup
import os


def scraper():
    USERID = os.getenv('USERID')
    PASSWORD = os.getenv('PASSWORD')
    SECRETANSWER = os.getenv('SECRETANSWER')

    browser = mechanicalsoup.StatefulBrowser()
    browser.open(
        "https://www.manage-student-loan-balance.service.gov.uk/")
    browser.select_form()
    browser["userId"] = USERID
    browser["password"] = PASSWORD
    browser.submit_selected()
    browser.select_form()
    browser["secretAnswer"] = SECRETANSWER
    browser.submit_selected()
    value = browser.page.find(
        id="balanceId_1").get_text().splitlines()[1].strip()
    return value


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    return scraper()
