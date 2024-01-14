from datetime import datetime, timedelta


def free_time(busy_periods):
    busy_periods.sort(key=lambda x: x['start'])
    work_start_time = datetime.strptime('09:00', "%H:%M")
    work_end_time = datetime.strptime('21:00', "%H:%M")

    free_periods = []

    first_busy_start = datetime.strptime(busy_periods[0]['start'], "%H:%M")
    current_time = work_start_time
    if work_start_time < first_busy_start:
        while current_time + timedelta(minutes=30) <= datetime.strptime(busy_periods[0]['start'], "%H:%M"):
            free_periods.append({'start': current_time.strftime("%H:%M"),
                                 'stop': (current_time + timedelta(minutes=30)).strftime("%H:%M")})
            current_time += timedelta(minutes=30)

    for i in range(len(busy_periods) - 1):
        current_time = datetime.strptime(busy_periods[i]['stop'], "%H:%M")
        while current_time + timedelta(minutes=30) <= datetime.strptime(busy_periods[i + 1]['start'], "%H:%M"):
            free_periods.append({'start': current_time.strftime("%H:%M"),
                                 'stop': (current_time + timedelta(minutes=30)).strftime("%H:%M")})
            current_time += timedelta(minutes=30)

    last_busy_end = datetime.strptime(busy_periods[-1]['stop'], "%H:%M")
    if last_busy_end < work_end_time:
        current_time = datetime.strptime(busy_periods[-1]['stop'], "%H:%M")
        while current_time + timedelta(minutes=30) <= datetime.strptime('21:00', "%H:%M"):
            free_periods.append({'start': current_time.strftime("%H:%M"),
                                 'stop': (current_time + timedelta(minutes=30)).strftime("%H:%M")})
            current_time += timedelta(minutes=30)

    return free_periods


busy_periods = [
    {'start': '10:30', 'stop': '10:50'},
    {'start': '18:40', 'stop': '18:50'},
    {'start': '14:40', 'stop': '15:50'},
    {'start': '16:40', 'stop': '17:20'},
    {'start': '20:05', 'stop': '20:20'}
]

free_periods = free_time(busy_periods)

print(free_periods)

