def getMyDivisor(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList

def solution(s):
    unit_list = []
    len_list = []
    unit_list = getMyDivisor(len(s))
    
    for i in range(1,len(s)):
        if i in unit_list:
            split = list(map(''.join, zip(*[iter(s)]*i)))
        else:
            split = list(map(''.join, zip(*[iter(s)]*i)))
            split.append(s[-(len(s)%i):])
        cnt = 1
                
        zip_list = ''
        for j in range(1,len(split)):
            if split[j-1] == split[j]:
                cnt += 1
            else:
                if cnt == 1:
                    zip_list += split[j-1]
                    cnt = 1
                else:
                    zip_list += str(cnt) + split[j-1]
                    cnt = 1
        if cnt == 1:
            zip_list += split[-1]
        else:
            zip_list += str(cnt) + split[-1]
        
        len_list.append(len(zip_list))        
    
    if len(s) == 1:
        return 1
    else:
        answer = min(len_list)
        return answer