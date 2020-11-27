# Дается число x, нужно найти такое число y,
# чтобы оно было больше или равно x и нацело делилось на 5
def closest_mod_5(x):
    return x if x % 5 == 0 else closest_mod_5(x+1)


'''
короткое решение
def closest_mod_5(x):
    return (x + 4) // 5 * 5
'''
print(closest_mod_5(6))
