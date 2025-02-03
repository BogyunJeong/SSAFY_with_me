num_01 = str(input()) # 1번 입력
num_02 = str(input()) # 2번 입력

for num_Index in range (len(num_02)-1, -1, -1): # 각 자리별로 계산하게 반복함
    print(f'{int(num_01)*int(num_02[num_Index])}') # 자릿수별 곱셈 구하기
print(f'{int(num_01)*int(num_02)}') # 진짜배기 곱셈 구하기