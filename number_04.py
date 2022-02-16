'''
문제 설명
- 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
- 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
- n은 2이상 1000000이하의 자연수입니다.

입출력 예
n	  result
10	  4
5	    3

입출력 예 설명
- 입출력 예 #1
  - 1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

- 입출력 예 #2
  - 1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환
'''
# 소수 개수 반환
def solution(n): 
        
    answer = 0
    
    if n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 5:
        return 3
    elif n == 7:
        return 4
    
    else:
        return prime_list(n)

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return len([i for i in range(2, n) if sieve[i] == True])
