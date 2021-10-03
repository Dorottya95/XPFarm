def how_many_years (date1,date2):
    diff = int(date1[:4]) - int(date2[:4])
    return abs(diff)