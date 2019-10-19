from pytest_bdd import scenario, given, when, then

from loans.factories import LoanFactory


LOANS_SIZE = 3


@scenario('features/loans.feature', 'Loans list')
def test_loans_list(browser):
    pass


@scenario('features/loans.feature', 'Add loan')
def test_loans_add(browser):
    pass


@given('I visit loans list')
def visit_homepage(live_server, db, browser):
    LoanFactory.create_batch(size=LOANS_SIZE)
    browser.visit(live_server.url)


@given('I visit loans create')
def visit_loan_create(live_server, db, browser):
    url = live_server.url + '/create'
    browser.visit(url)


@given('I have filled out a loan form')
def fill_loan_form(browser):
    browser.fill('amount', 5000)


@when('I press submit button')
def press_submit_button(browser):
    browser.find_by_css('body > form > input[type=submit]:nth-child(3)')[0].click()


@then('I should see loans')
def should_see_loans(browser):
    assert len(browser.find_by_css('li')) == LOANS_SIZE


@then('I should see a new loan')
def should_see_new_loan(browser):
    assert len(browser.find_by_css('li')) == 1
    browser.find_by_css('body > ul > li').html == '1 - 5000'
