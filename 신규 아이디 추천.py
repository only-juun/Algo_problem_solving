def step1(new_id):
    return new_id.lower()

def step2(new_id):
    s = ''.join(char for char in new_id
                      if char =='-' or char =='_' or 
                      char == '.' or char.isalnum())
    return s

def step3(new_id):
    s = ''
    for i in range(len(new_id)):
        if i == 0:
            s += new_id[i]
        elif (new_id[i] == '.') & (new_id[i-1] == '.'):
            continue
        else:
            s += new_id[i]
                
    return s
    
def step4_1(new_id):
    if new_id[0] == '.':
        return new_id[1:]
    else:
        return new_id
    
    
def step4_2(new_id):
    s1 = new_id[::-1]
    s2 = ''
    if s1[0] == '.':
        s2 += s1[1:]
        return s2[::-1]
    else:
        return s1[::-1]
    
def step5(new_id):
    if new_id == '':
        return 'a'
    else:
        return new_id
    
def step6(new_id):
    if len(new_id) > 15:
        return new_id[:15]
    else:
        return new_id
    
def step7(new_id):
    s = ''.join(new_id)
    if len(new_id) < 3:
        while(len(s) < 3):
            s += new_id[len(new_id)-1]
        return s
    else:
        return new_id

def solution(new_id):
    new_id = step1(new_id)
    new_id = step2(new_id)
    
    if new_id == '':
        new_id = step5(new_id)
    else:
        new_id = step3(new_id)
        
        new_id = step4_1(new_id)
        
        if new_id == '':
            new_id = step5(new_id)
        else:
            new_id = step4_2(new_id)
            
            new_id = step6(new_id)
            new_id = step4_2(new_id)

    answer = step7(new_id)
    return answer