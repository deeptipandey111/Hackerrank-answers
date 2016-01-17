def max_toys(prices, rupees):
    #Compute and return final answer over here
    answer = -1
    p = sorted(prices)
    s = 0
    for i in range(len(p)):
        if sum(p[:i])>rupees:
            break
        else :
            answer += 1
            s = sum(p[:i])
    
    return answer

if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    prices = map(int, raw_input().split())
    print max_toys(prices, k)
