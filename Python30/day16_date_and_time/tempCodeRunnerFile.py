dates = [
    "2026-05-10",
    "2024-12-01",
    "2027-03-15"
] 

def filter_future_dates(dates):
    now = datetime.today()
    print(now)
    result = []

    for date in dates:
        to_check = datetime.strptime(date, '%Y-%m-%d') 
        print((to_check - now).days)

        if (to_check - now).days > 0:
            result.append(date) 
    return result

print(filter_future_dates(dates))