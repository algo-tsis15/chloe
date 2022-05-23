def solution(n):
    answer = 0
    dp = [0] * 60001
    
    for i in range(3):
        dp[i] = i
        
    for i in range(3, n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 1000000007
    
    return dp[n]

    # 배열을 사용하지않고 단순 스와핑의 경우는 밖에서 return 하는 곳에서 나누기해도 시간 초과 나지 않음