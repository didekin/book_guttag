import matplotlib.pyplot as plt


def plot_infections(infections_in, tot_infections_in, fixed_in):
    infection_plot = plt.plot(infections_in, 'r', label='Infected')[0]
    plt.xticks(fontsize='large')
    plt.yticks(fontsize='large')
    plt.xlabel('Days Since First Infection', fontsize='xx-large')
    plt.ylabel('Number Currently Infected', fontsize='xx-large')
    plt.title('Number of Infections Assuming No Vaccine\n' +
              f'Pop = {fixed_in["pop"]:,},\n' +
              f'Contacts/Day = {fixed_in["init_contacts"]},\n' +
              f'Infectivity = {(100 * fixed_in["contagiousness"]):.1f}%, ' +
              f'Days Contagious = {fixed_in["days_spreading"]}')
    plt.legend(fontsize='xx-large')
    txt_box = plt.text(plt.xlim()[1] / 2, plt.ylim()[1] / 1.25,
                       f'Total Infections = {tot_infections_in:,}',
                       fontdict={'size': 'xx-large', 'weight': 'bold',
                                 'color': 'red'})
    return infection_plot, txt_box


def simulation(fixed_in, variable_in):
    infected = [fixed_in['initial_infections']]
    new_infections = [fixed_in['initial_infections']]
    tot_infections = fixed_in['initial_infections']

    for t in range(fixed_in['duration']):
        cur_infections = new_infections[-fixed_in['days_spreading']:]
        # remove people who are no longer contagious
        if len(new_infections) > fixed_in['days_spreading']:
            cur_infections = new_infections[-fixed_in['days_spreading']:]
        # if social distancing, change number of daily contacts
        if variable_in['red_start'] <= t < variable_in['red_end']:
            daily_contacts = variable_in['red_daily_contacts']
        else:
            daily_contacts = fixed_in['init_contacts']

        # compute number of new cases
        total_contacts = cur_infections * daily_contacts
        susceptible = fixed_in['pop'] - tot_infections
        risky_contacts = total_contacts * (susceptible / fixed_in['pop'])
        newly_infected = round(risky_contacts * fixed_in['contagiousness'])

        # update variables
        new_infections.append(newly_infected)
        tot_infections += newly_infected
        infected.append(cur_infections + newly_infected)

    return infected, tot_infections


# Example usage
fixed = {
    'pop': 5000000,  # population at risk
    'duration': 50,  # number of days for simulation
    'initial_infections': 4,  # initial number of cases
    'init_contacts': 8.0,  # contacts without social distancing
    'contagiousness': 0.05,  # prob. of getting disease if exposed
    'days_spreading': 10  # days contagious after infection
}

variable = {
    'red_start': 20,  # start of social distancing
    'red_end': 30,  # end of social distancing
    'red_daily_contacts': 4,  # social distancing
}

infections, total_infections = simulation(fixed, variable)
plot_infections(infections, total_infections, fixed)
plt.show()
