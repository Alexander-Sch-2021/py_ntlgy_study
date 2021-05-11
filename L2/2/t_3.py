boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) != len(girls):
    print('Внимание, кто-то может остаться без пары!')
else:
    print('Идеальные пары:')
    for i in range(len(boys)):
        print(boys[i], 'и', girls[i])
