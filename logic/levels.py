def get_level(level):
    if level == 1:
        return 1, 10, 3, 'all'
    elif level == 2:
        return 11, 99, 4, 'all'
    elif level == 3:
        return 100, 999, 6, 'all'
    elif level == 4:
        return 2, 100, 5, 'even'
    elif level == 5:
        return 3, 60, 4, 'multiple3'
    elif level == 6:
        return 4, 80, 4, 'multiple4'
    elif level == 7:
        return 5, 100, 4, 'multiple5'
    elif level == 8:
        return 6, 120, 4, 'multiple6'
    elif level == 9:
        return 7, 140, 4, 'multiple7'
    elif level == 10:
        return 8, 160, 4, 'multiple8'
    elif level == 11:
        return 9, 180, 4, 'multiple9'
    elif level == 12:
        return 10, 200, 4, 'multiple10'
    elif level == 13:
        return 2, 100, 5, 'prime'
    elif level == 14:
        return 1, 200, 5, 'squareroot'
    elif level == 15:
        return 1, 200, 5, 'cuberoot'
    return 1, 10, 3, 'all'
