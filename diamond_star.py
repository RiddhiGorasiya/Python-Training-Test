rows = 5
# upper
for i in range(1, rows + 1):
    spaces = rows - i 
    stars = 2 * i -1
    print(' ' * spaces + '*' * stars)
# lower
for i in range(rows - 1, 0, -1):
    spaces = rows - i 
    stars = 2 * i -1
    print(' ' * spaces + '*' * stars)