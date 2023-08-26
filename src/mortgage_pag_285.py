import matplotlib.pyplot as plt
import numpy as np


class Mortgage(object):

    def __init__(self, loan, annrate, months):
        self._loan = loan
        self._rate = annrate / 12.0
        self._months = months
        self._paid = [0.0]
        self._oustanding = [loan]
        self._month_payment = (self._loan *
                               (self._rate * (1 + self._rate) ** self._months) /
                               ((1 + self._rate) ** self._months) - 1)

    def make_payment(self):
        self._paid.append(self._month_payment)
        reduction = self._month_payment - self._oustanding[-1] * self._rate
        self._oustanding.append(self._oustanding[-1] - reduction)

    def total_paid(self):
        return sum(self._paid)

    def plot_payments(self, style, legend):
        plt.plot(self._paid[1:], style, label=legend)

    def plot_balance(self, style, legend):
        plt.plot(self._oustanding, style, label=legend)

    def accum_moth_paid(self):
        tot_paid = [self._paid[0]]
        for i in range(1, len(self._paid)):
            tot_paid.append(tot_paid[-1] + self._paid[i])
        return tot_paid

    def plot_tot_paid(self, style, legend):
        tot_paid = self.accum_moth_paid()
        plt.plot(tot_paid, style, label=legend)

    def plot_net_equity(self, style, legend):
        tot_paid = self.accum_moth_paid()
        entity_acquired = np.array([self._loan] * len(self._oustanding))
        entity_acquired = entity_acquired - np.array(self._oustanding)
        paid_over_equity = np.array(tot_paid) - entity_acquired
        plt.plot(paid_over_equity, style, label=legend)


class Fixed(Mortgage):
    def __init__(self, loan, annrate, months):
        Mortgage.__init__(self, loan, annrate, months)
        self.legend = f'Fixed {annrate * 100: .2f}%'


class FixedWithPoins(Mortgage):
    def __init__(self, loan, annrate, months, points):
        Mortgage.__init__(self, loan, annrate, months)
        self._points = points
        self._paid = [loan * points]
        self.legend = f'FixedWithPoints {annrate * 100: .2f}%, {points} points'


class TwoRate(Mortgage):
    def __init__(self, loan, annrate, months, teaser_rate, teaser_months):
        # Initialize rate with the teaser rate and uses it and the total months of the loan to calculate
        # payments during the teaser period.
        Mortgage.__init__(self, loan, teaser_rate, months)
        self._teaser_months = teaser_months
        self._second_rate = annrate / 12
        self.legend = (f'TwoRate loan with teaser_rate {teaser_rate * 100: .2f}% for ' +
                       f'{teaser_months} months, then {annrate * 100: .2f}%')

    def make_payment(self):
        if len(self._paid == self._teaser_months) + 1:
            self._rate = self._second_rate
            self._months -= self._teaser_months
            self._month_payment = (self._oustanding[-1] *
                                   (self._rate * (1 + self._rate) ** self._months) /
                                   ((1 + self._rate) ** self._months) - 1)
        Mortgage.make_payment(self)


mort1 = Mortgage(1000, 0.01, 12)
mort2 = Fixed(1000, 0.01, 12)
print(mort2.legend)
