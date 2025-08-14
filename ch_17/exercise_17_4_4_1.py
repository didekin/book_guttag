import matplotlib.pyplot as plt

from modules import guttag_module as gu


def dice_success(trialsIn, successesIn):
    prob_succ = 1 / 6
    return gu.combinations(trialsIn, successesIn) * prob_succ ** successesIn * (1 - prob_succ) ** (
            trialsIn - successesIn)


prob_succes_list = []
trials = list(range(2, 101))
successes = 2
for trial in trials:
    prob_succes_list.append(dice_success(trial, successes))
plt.plot(trials, prob_succes_list)
plt.savefig('./exercise_17_4_4_1.pdf')
plt.show()
