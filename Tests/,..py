def weight(name, eat_during_the_day, lose_during_the_day):
    if eat_during_the_day > lose_during_the_day:
        msg = name + ' дохуя жрет'
    else:
        msg= name + ' недоедает'
    return msg
print(weight('коля', 1000, 1500))
