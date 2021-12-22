'''
Create date : 2021/12/22.
Update      : 2021/12/22.
Writer      : Nishimura Kairi
'''

def best_time_to_party(schedule):
    times = []
    for c in schedule:
        times.append((c[0], 'start'))
        times.append((c[1], 'end'))
    sort_list(times)
    max_cnt, best_time = choose_time(times)

    print('Best time to append the party is at', best_time, 'o\'clock',
          ':', max_cnt, 'celebrities will be attending!')


def sort_list(times):
    for i in range(len(times)-1):
        k = i
        for j in range(i, len(times)):
            if times[k][0] > times[j][0]:
                k = j
        times[i], times[k] = times[k], times[i]

def choose_time(times):
    cnt = 0
    max_cnt = best_time = 0
    for time in times:
        if time[1] == 'start':
            cnt += 1
        elif time[1] == 'end':
            cnt -= 1
        if cnt > max_cnt:
            max_cnt = cnt
            best_time = time[0]
    
    return max_cnt, best_time

if __name__ == "__main__":
    schedule = [(6.0, 8.0), (6.0, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
            (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]
    best_time_to_party(schedule)