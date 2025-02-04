data = list(map(int, input().split())) # 받아 적을 공간을 만든다.

if data[0] == data[1] and data[1] == data[2]: # 3개가 다 똑같을 경우 간단하다. 1?000점을 만들 식 1개만 만들면 된다.
    print(f'{10000+data[0]*1000}')
elif data[0] == data[1] or data[1] == data[2] or data[0] == data[2]: # 2개일 경우 각각의 경우의 수를 다 나열한다.
    if data[0] == data[1] and data[1] == data[2]:
        same_Value = data[1] # 1번 데이터를 키값으로 밸류에 저장
    elif data[1] == data[2] or data[0] == data[2]:
        same_Value = data[2] # 2번 데이터를 키값으로 밸류에 저장
    else:
        same_Value = data[0] # 0번 데이터를 키값으로 밸류에 저장
    print(1000+same_Value*100) # 그리고 키값으로 저장된 중복된 밸류를 집어넣어서 출력하면 된다.
else:
    print(f'{max(data)*100}') # 간단하다 가장 높은 수가 출력되게 max를 이용하면 끝!