def calculateLps(s):
    length = len(s) 
    lps = [0] * length
    matchedIdx = 0 
      
    idx = 1 
    while (idx < length) : 
        if (s[idx] == s[matchedIdx]) : 
            matchedIdx = matchedIdx + 1
            lps[idx] = matchedIdx 
            idx = idx + 1          
        else : 
            # a match has failed ... move back 
            if (matchedIdx != 0) : 
                matchedIdx = lps[matchedIdx-1] 
            else : 
                lps[idx] = 0
                idx = idx + 1
    return lps

def solution(s) : 
    # calculate the longest prop pref suffix like in KMP
    lps = calculateLps(s)
    # the maximum is stored at the last
    maximum = lps[len(s)-1] 
    return maximum


n = solution("aaaaaaa")
print(n)
