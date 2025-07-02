import matplotlib.pyplot as plt
import numpy as np

import ch_10.example_10_4 as mg


def plot_payments(mortgage, style):
    plt.plot(mortgage.get_paid()[1:], style, label=mortgage.legend)


def plot_balance(mortage, style):
    plt.plot(mortage.get_outstanding(), style, label=mortage.legend)


def plot_tot_pd(mortgage, style):
    tot_pd = [mortgage.get_paid()[0]]
    for i in range(1, len(mortgage.get_paid())):
        tot_pd.append(tot_pd[-1] + mortgage.get_paid()[i])
    plt.plot(tot_pd, style, label=mortgage.legend)


def plot_net(mortgage, style):
    tot_pd = [mortgage.get_paid()[0]]
    for i in range(1, len(mortgage.get_paid())):
        tot_pd.append(tot_pd[-1] + mortgage.get_paid()[i])
    equity_acquired = np.array([mortgage.loan] * len(mortgage.get_outstanding()))
    equity_acquired = equity_acquired - np.array(mortgage.get_outstanding())
    net = np.array(tot_pd) - equity_acquired
    plt.plot(net, style, label=mortgage.legend)


def compare_mortgages(amt, years, fixed_rate, pts, pts_rate, var_rate1, var_rate2, var_months):
    tot_months = years * 12
    fixed1 = mg.Fixed(amt, fixed_rate, tot_months)
    fixed2 = mg.FixedWithPoints(amt, pts_rate, tot_months, pts)
    two_rate = mg.TwoRate(amt, var_rate2, tot_months, var_rate1, var_months)
    mortg_types = [fixed1, fixed2, two_rate]
    for m in range(tot_months):
        for mort in mortg_types:
            mort.make_payment()
    plot_mortgages(mortg_types, amt)


def plot_mortgages(mortg_types, amt):
    def label_plot(figure, title, x_label, y_label):
        plt.figure(figure)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend(loc='best')

    styles = ['k-', 'k-', 'k:']
    # Give names to figure numbers
    payments, cost, balance, net_cost = 0, 1, 2, 3

    for i in range(len(mortg_types)):
        plt.figure(payments)
        plot_payments(mortg_types[i], styles[i])
        plt.figure(cost)
        plot_tot_pd(mortg_types[i], styles[i])
        plt.figure(balance)
        plot_balance(mortg_types[i], styles[i])
        plt.figure(net_cost)
        plot_net(mortg_types[i], styles[i])

    label_plot(payments, f'Monthly Payments of ${amt:,.0f} Mortages',
               'Months', 'Monthly Payments')
    label_plot(cost, f'Cash Outlay of ${amt:,.0f} Mortgages',
               'Months', 'Total Payments')
    label_plot(balance, f'Balance Remaining of ${amt:,.0f} Mortgages',
               'Months', 'Remaining Loan Balance of $')
    label_plot(net_cost, f'Net Cost of ${amt:,.0f} Mortgages',
               'Months', 'Payments - Equity $')


compare_mortgages(amt=200000, years=30, fixed_rate=0.07,
                  pts=3.25, pts_rate=0.05, var_rate1=0.045,
                  var_rate2=0.095, var_months=48)
plt.show()
