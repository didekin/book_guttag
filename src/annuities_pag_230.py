class Amortization(object):
    def __init__(self, yearnominal, months, amount=0):
        self.__yearly_nominal_rate = yearnominal
        self.__months_amortization = months
        self.__principal = amount

    def yearly_payment(self):
        rate = self.__yearly_nominal_rate
        years = self.__months_amortization / 12
        principal = self.__principal
        return rate * ((1 + rate) ** years) * principal / ((1 + rate) ** years - 1)

    def monthly_payment(self):
        rate = self.__yearly_nominal_rate / 12
        months = self.__months_amortization
        principal = self.__principal
        return rate * ((1 + rate) ** months) * principal / ((1 + rate) ** months - 1)

    def principal_from_payment(self, payment):
        rate = self.__yearly_nominal_rate / 12
        months = self.__months_amortization
        return (1 - (1 / (1 + rate) ** months)) * payment / rate


# Luenberger, 'Investment science', pag. 47.
ynr_1 = 0.12
months_1 = 60
amount_1 = 1000
amortization_1 = Amortization(ynr_1, months_1, amount_1)
print(amortization_1.monthly_payment())

# Luenberger, 'Investment science', pag. 48.
apr_2 = 0.07883
ynr_2 = 0.07625
months_2 = 360
amount_2_1 = 203150
amortization_2 = Amortization(apr_2, months_2, amount_2_1)
payment_2_1 = amortization_2.monthly_payment()
amount_2_2 = amortization_2.principal_from_payment(payment_2_1)
print(payment_2_1)
print(amount_2_2)

# Luenberger, 'Investment science', pag. 49.
ynr_3 = 0.16
months_3 = 120
amount_3 = 100000
amortization_3 = Amortization(ynr_3, months_3, amount_3)
print(amortization_3.yearly_payment())
