'''
Create date : 2021/12/20.
Update      : 2021/12/20.
Writer      : Nishimura Kairi
'''

def pleaseConfirm(caps):
    start = forward = backward = 0
    intervals = []
    for i in range(len(caps)):
        if caps[start] != caps[i]:
            intervals.append((start, i-1, caps[start]))
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i
    intervals.append((start, len(caps)-1, caps[start]))
    
    if caps[start] == 'F':
        forward += 1
    else:
        backward += 1
    
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    
    return intervals, flip
    

def main():
    cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
    cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']
    
    intervals, flip = pleaseConfirm(cap2)
    for t in intervals:
        # print(t)
        if t[2] == flip:
            print('People in positions {} through {} flip your caps!'.format(t[0], t[1]))

main()
