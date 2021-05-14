stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}

print('Максимальный объем продаж на рекламном канале:', *[s[0] for s in stats.items() if s[1] == max(stats.values())])
