def solution(record):
    answer = []
    uid_nick = {}
    
    for rec in record:
        if rec.startswith('E') or rec.startswith('C'):
            _, uid, nick = rec.split()
            uid_nick[uid] = nick
    
    for rec in record:
        if rec.startswith('E'):
            _, uid, nick = rec.split()
            answer.append(uid_nick[uid] + "님이 들어왔습니다.")
        elif rec.startswith('L'):
            _, uid = rec.split()
            answer.append(uid_nick[uid] + "님이 나갔습니다.")
    
    return answer