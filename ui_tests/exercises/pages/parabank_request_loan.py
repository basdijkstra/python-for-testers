from selenium.webdriver.common.by import By
from ui_tests.answers.helpers import SeleniumHelpers


class RequestLoanPage:

    # Add locators for the following elements:
    # - textfield containing the loan amount
    # - textfield containing the down payment amount
    # - dropdown for selecting the from account ID
    # - button to submit the loan application
    # - textfield containing the loan application result

    def __init__(self, browser):
        self.browser = browser
        self.selenium = SeleniumHelpers(browser)

    # Create a method request_loan() that performs the loan request
    # It takes (besides self) three arguments: the loan amount, the down payment and the from account ID
    # In this method, perform the type and click actions necessary to submit the loan request

    # Create a method get_application_result() that returns the loan application result as text
    # Use the locator for the application result textfield here and a
    # suitable helper method that returns its visible text
