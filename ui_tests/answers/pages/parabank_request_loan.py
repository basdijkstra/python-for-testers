from selenium.webdriver.common.by import By
from ui_tests.answers.helpers import SeleniumHelpers


class RequestLoanPage:

    # Add locators for the following elements:
    # - textfield containing the loan amount
    # - textfield containing the down payment amount
    # - dropdown for selecting the from account ID
    # - button to submit the loan application
    # - textfield containing the loan application result
    textfield_amount = (By.ID, "amount")
    textfield_down_payment = (By.ID, "downPayment")
    dropdown_from_account = (By.ID, "fromAccountId")
    button_do_request = (By.XPATH, "//input[@value='Apply Now']")
    textfield_application_result = (By.ID, "loanStatus")

    def __init__(self, browser):
        self.browser = browser
        self.selenium = SeleniumHelpers(browser)

    def request_loan(self, amount, down_payment, from_account):
        self.selenium.send_keys(self.textfield_amount, amount)
        self.selenium.send_keys(self.textfield_down_payment, down_payment)
        self.selenium.select(self.dropdown_from_account, from_account)
        self.selenium.click(self.button_do_request)

    def get_application_result(self):
        return self.selenium.get_element_text(self.textfield_application_result)
