# cook your dish here
for _ in range(int(input())):
    fastest_finish_time, chef_finish_time = map(int, input().split(' '))
    print('YES') if chef_finish_time <= fastest_finish_time * 1.07 else print('NO')