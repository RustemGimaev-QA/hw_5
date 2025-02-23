from selene import browser, be, have
import os

def test_practice_form():
    browser.open('/automation-practice-form')
    browser.element('[class=text-center]').should(have.text('Practice Form'))
    browser.element('#firstName').type('Petrov')
    browser.element('#lastName').type('Andrey')
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
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('#uploadPicture').type(os.path.abspath('images/Screenshot_4.png'))
    browser.element('#currentAddress').type('City Kirov Lenin street house 25 apartment 3')
    browser.element('#state').click().element('#react-select-3-option-1').click()
    browser.element('#city').click().element('#react-select-4-option-2').click()
    browser.element('#submit').click()
    browser.element('.modal-content').should(have.text('Thanks for submitting the form'))

    #Проверка введенных данных в результирующей таблице
    browser.element(".table-dark").should(have.text('Petrov Andrey'))
    browser.element(".table-dark").should(have.text('petrov@mail.ru'))
    browser.element(".table-dark").should(have.text('Male'))
    browser.element(".table-dark").should(have.text('8925321852'))
    browser.element(".table-dark").should(have.text('10 March,2008'))
    browser.element(".table-dark").should(have.text('Maths'))
    browser.element(".table-dark").should(have.text('Sports'))
    browser.element(".table-dark").should(have.text('Screenshot_4.png'))
    browser.element(".table-dark").should(have.text('City Kirov Lenin street house 25 apartment 3'))
    browser.element(".table-dark").should(have.text('Uttar Pradesh Merrut'))

    #Закрытие результирующей таблицы
    browser.element('.modal-content').element('#closeLargeModal').click()

    #Проверка элемента на странице
    browser.element('[class=text-center]').should(have.text('Practice Form'))







