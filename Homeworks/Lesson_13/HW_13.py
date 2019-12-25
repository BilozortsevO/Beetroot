def accrued_salary (salary, bonus):
    def taxes (personal_income_tax, war_tax):
        return ((salary + bonus)*(100 - (personal_income_tax + war_tax)))/100
    return taxes

monthly_salary = accrued_salary(6300, 3700)

print ('Your monthly salary is: ' + str(monthly_salary (18, 1.5)) + ' UAH.')

