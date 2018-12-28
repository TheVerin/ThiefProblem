from django.shortcuts import render
import pandas as pd
from thief_main.models import Thief


def mass_checker(mass_1=1, mass_2=1, car_load=10):
    solutions = []
    for i in range(int(car_load/mass_1)):
        for j in range(int(car_load/mass_2)):
            if i * mass_1 + j * mass_2 <= car_load:
                solutions.append([i, j])
    return solutions


def profit_counter(solutions, prize_1=1, prize_2=1):
    solutions_df = pd.DataFrame(solutions, columns=('NumberOfA', 'NumberOfB'))
    solutions_df['Profit'] = solutions_df['NumberOfA'] * prize_1 + solutions_df['NumberOfB'] * prize_2
    solutions_df = solutions_df.sort_values(['Profit'], ascending=False)
    best = solutions_df.head(1)
    return best


def final(request):
    thief_name = 'You'
    name_1 = 'Ring'
    name_2 = 'Necklace'
    mass_1 = 1
    mass_2 = 1
    prize_1 = 1
    prize_2 = 1
    car_load = 10
    res = 1
    num_a = 0
    num_b = 0

    if request.GET.get('thief_name'):
        thief_name = request.GET.get('thief_name')
        name_1 = request.GET.get('name_1')
        name_2 = request.GET.get('name_2')
        mass_1x = request.GET.get('mass_1')
        mass_1 = int(mass_1x)
        mass_2x = request.GET.get('mass_2')
        mass_2 = int(mass_2x)
        prize_1x = request.GET.get('prize_1')
        prize_1 = int(prize_1x)
        prize_2x = request.GET.get('prize_2')
        prize_2 = int(prize_2x)
        car_load_x = request.GET.get('car_load')
        car_load = int(car_load_x)

        a = mass_checker(mass_1, mass_2, car_load)
        b = profit_counter(a, prize_1, prize_2)
        num_a = b.iloc[0]['NumberOfA']
        num_b = b.iloc[0]['NumberOfB']
        res = b.iloc[0]['Profit']

    obj = Thief.objects.create(
        thief_name=thief_name,
        name_1=name_1,
        name_2=name_2,
        mass_1=mass_1,
        mass_2=mass_2,
        prize_1=prize_1,
        prize_2=prize_2,
        car_load=car_load,)
    obj.save()

    return render(
        request,
        'index.html',
        {
            'thief_name': thief_name,
            'name_1': name_1,
            'name_2': name_2,
            'mass_1': mass_1,
            'mass_2': mass_2,
            'prize_1': prize_1,
            'prize_2': prize_2,
            'car_load': car_load,
            'res': res,
            'num_a': num_a,
            'num_b': num_b,
        }
    )
