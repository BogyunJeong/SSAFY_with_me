total_Price = int(input()) # 총액 입력

total_Goods = int(input()) # 물건의 종류 수 입력

goods_list = [] # 굿즈 가격을 저장할 리스트 추가

for goods_Index in range(0, total_Goods): # 종류 수 만큼 반복
    
    goods = list(map(int, input().split())) # 굿즈의 가격과 갯수를 입력받음
    goods_Total_Price = goods[0] * goods[1] # 가격 X 갯수 저장
    goods_list.append(goods_Total_Price) # 리스트에 추가

if total_Price == sum(goods_list): # 처음 입력한 총액이 리스트내 물건들의 총액과 같을시
    print('Yes') # 예스 예스 예스!
else:
    print('No') # 아님 말고.