class Mortgage(object):
    """Abstract class for building different kinds of mortgages"""

    def __init__(self, loan, ann_rate, months):
        """Assumes: loan and ann_rate are floats, months an int
        Creates a new mortgage of size loan, duration months, and
        annual rate ann_rate"""
        self.loan = loan
        self.ann_rate = ann_rate
        self.months = months
        self._month_rate = ann_rate / 12
        self._paid = [0.0]
        self._outstanding = [loan]
        self._payment = find_payment(loan, self._month_rate, months)
        self.legend = None  # Description of mortgage

    def make_payment(self):
        """Make a payment"""
        self._paid.append(self._payment)
        # Reduction take into account only the part of the payment after accrued interest.
        reduction = self._payment - self._outstanding[-1] * self._month_rate
        self._outstanding.append(self._outstanding[-1] - reduction)

    def get_total_paid(self):
        """Return the total amount paid so far"""
        return sum(self._paid)

    def get_params(self):
        return (f' amount:{str(self.loan)}, annual_rate:{str(self.ann_rate)}, '
                f'months:{str(self.months)}, monthrate:{self._month_rate}')

    def get_outstanding(self):
        return self._outstanding

    def get_paid(self):
        return self._paid

    def get_payment(self):
        return self._payment

    def __str__(self):
        return self.legend


def find_payment(loan, month_rate, months):
    """Assumes: loan and month_rate are floats, months an int
    Returns the monthly payment for a mortgage of size
    loan, duration months, and monthly rate r"""
    return loan * (month_rate * (1 + month_rate) ** months) / ((1 + month_rate) ** months - 1)


class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, {0:.1f}%'.format(r * 100)


class FixedWithPoints(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self._paid = [loan * (pts / 100)]
        self.legend = 'Fixed, {0:.1f}%, {1} points'.format(r * 100, pts)


class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaser_rate, teaser_months):
        Mortgage.__init__(self, loan, teaser_rate, months)
        self.teaser_months = teaser_months
        self.teaser_rate = teaser_rate
        self.nextRate = r / 12
        self.legend = ('{0:.1f}% for '.format(teaser_rate * 100) +
                       '{0} months, then {1:.1f}%'.format(teaser_months, (100 * r)))

    def make_payment(self):
        if len(self._paid) == self.teaser_months + 1:
            self._month_rate = self.nextRate
        self._payment = find_payment(self._outstanding[-1],
                                     self._month_rate,
                                     self.months - self.teaser_months)

        Mortgage.make_payment(self)


def compare_mortgages(amt, years, fixed_rate, pts, pts_rate,
                      var_rate1, var_rate2, var_months):
    tot_months = years * 12
    fixed1 = Fixed(amt, fixed_rate, tot_months)
    fixed2 = FixedWithPoints(amt, pts_rate, tot_months, pts)
    two_rate = TwoRate(amt, var_rate2, tot_months, var_rate1, var_months)
    morts = [fixed1, fixed2, two_rate]
    for m in range(tot_months):
        for mort in morts:
            mort.make_payment()
    for m in morts:
        print(m)
        print('  Total payments = ${0:,.0f}'.format(m.get_total_paid()))
