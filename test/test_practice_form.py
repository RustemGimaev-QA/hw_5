from selene import browser, be, have

def test_practice_form():
    browser.open('/automation-practice-form')
    browser.element('[class=text-center]').should(have.text('Practice Form'))
    browser.element('#firstName').type('Петров')
    browser.element('#lastName').type('Андрей')
    browser.element('#userEmail').type('petrov@mail.ru')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('89253218526')

