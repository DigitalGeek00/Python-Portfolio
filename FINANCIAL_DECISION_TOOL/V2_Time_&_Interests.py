def financial_data():

    initial_capital = float(input('Enter initial capital, without using dots: (E.g. 10000, 20000, etc): '))
    while initial_capital < 0:
        print('Please, enter a value equal to or higher than 0.')
        initial_capital = float(input('New value: '))
    print('Perfect, continue.')
    input('Press ENTER to continue')

    time = float(input('Enter years invested, use int or float: (E.g. 2, 4, 5.6, etc): '))
    while time < 1:
        print('Please, enter a value equal to or higher than 1.')
        time = float(input('New value: '))
    print('Perfect, continue.')
    input('Press ENTER to continue')

    annual_rate = float(input('Enter annual rate, use int or float: (E.g. 2, 4, 2.3, etc): ')) / 100
    while annual_rate <= 0:
        print('Please, enter a value higher than 0.')
        annual_rate = float(input('New value: '))
    print('Perfect, continue.')
    input('Press ENTER to end calculation.')

    return initial_capital, time, annual_rate

def simple_interest(initial_capital, time, annual_rate):

    simple_interests = initial_capital * time * annual_rate

    simple_final_capital = initial_capital + simple_interests

    return simple_interests, simple_final_capital

def compound_interest(initial_capital, time, annual_rate):
   
    compound_final_capital = initial_capital * (1 + annual_rate) ** time
   
    compound_interests = compound_final_capital - initial_capital

    return compound_interests, compound_final_capital

def calculate_dca(initial_capital, monthly_contribution, time, annual_rate):

    time_months = time * 12

    monthly_rate = annual_rate / 12

    total_contribution = initial_capital + (monthly_contribution * time_months)

    initial_capital_growth = (
        initial_capital * (1 + monthly_rate) ** time_months
    ) - initial_capital

    contribution_growth = monthly_contribution * (
        ((1 + monthly_rate) ** time_months - 1)
        / monthly_rate
    ) - (monthly_contribution * time_months)

    final_capital = (
        initial_capital
        + initial_capital_growth
        + (monthly_contribution * time_months)
        + contribution_growth
)
    investment_return = final_capital - total_contribution

    return (
        total_contribution, 
        initial_capital_growth, 
        contribution_growth, 
        final_capital, 
        investment_return
    )

while True:
    print('==============================')
    print('WELCOME TO FINANCE CALCULATOR TOOL: ')
    print('==============================')
    print('1. Simple interest')
    print('2. Compound interest')
    print('3. DCA Strategy')
    print('4. Exit')

    option = input('Select an option: ')

    if option == '1':
        print('User selected simple interest')
        initial_capital, time, annual_rate = financial_data()

        simple_interests, simple_final_capital = simple_interest(initial_capital, time, annual_rate)

        print(f'Simple interests generated over {time} years are: {simple_interests:.2f} €')
        input('Press ENTER to know your final capital:')
        print(f'This result shows the final capital you have: {simple_final_capital:.2f} €')
        input('Press ENTER to return to menu.')

    elif option == '2':
        print('User selected compound interest')
        initial_capital, time, annual_rate = financial_data()
        compound_interests, compound_final_capital = compound_interest(initial_capital, time, annual_rate)
        print(f'Compound interests generated over {time} years are: {compound_interests:.2f} €')
        input('Press ENTER to see final capital:')
        print(f'This result shows the final capital you have: {compound_final_capital:.2f} €')
        input('Press ENTER to return to menu.')

    elif option == '3':
        print('User selected DCA Strategy')
        initial_capital, time, annual_rate = financial_data()
        monthly_contribution = float(input('Enter monthly contributions without using dots (E.g. 100, 200,...): '))
        while monthly_contribution <= 0:
            print('Please, enter a higher value than 0.')
            monthly_contribution = float(input('New value: '))
        total_contribution, initial_capital_growth, contribution_growth, final_capital, investment_return = calculate_dca(initial_capital, monthly_contribution, time, annual_rate)
        print(f'This is the total capital aported: {total_contribution:.1f} €')
        input('Press ENTER to continue.')
        print(f'This is the investment final capital: {final_capital:.1f} €')
        input('Press ENTER to continue.')
        print(f'This is your investment return: {investment_return:.1f} €')
        input('Press ENTER to continue.')

    elif option == '4':
        print('See you soon!')
        break

    else:
        print('Option not available now.')
