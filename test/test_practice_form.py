from selene import browser, be, have

def test_practice_form():
    browser.open('/automation-practice-form')
    browser.element('[class=text-center]').should(have.text('Practice Form'))
    browser.element('#firstName').type('Петров')
    browser.element('#lastName').type('Андрей')
    browser.element('#userEmail').type('petrov@mail.ru')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('8925321852')
    browser.element('.react-datepicker-wrapper').click()
    browser.element('.react-datepicker__day-names').should(have.text('We'))
    browser.element('.react-datepicker__month-select').click().element("[value='2']").click()
    browser.element('.react-datepicker__current-month').should(have.text('March'))
    browser.element('.react-datepicker__year-select').click().element("[value='2008']").click()
    browser.element('.react-datepicker__current-month').should(have.text('2008'))
    browser.element('.react-datepicker__day--010').click()
