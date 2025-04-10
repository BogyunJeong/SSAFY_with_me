def comb(idx,cnt):
    # 원하는 개수만큼 선택
    if cnt == K:
        print(check)
        return
    # 원하는 개수만큼 요소를 선택하지 못한 상태
    if idx == N:
        return
    check[idx] = 1
    comb(idx + 1,cnt + 1) # idx번쨰 요소를 조합에 포함
    check[idx] = 0
    comb(idx+1, cnt) # idx 번째 요소를 조합에 포함 시키지 않음

arr = [1,2,3,4,5]
N = len(arr)
K = 3
check = [0] * N

comb(0,0)