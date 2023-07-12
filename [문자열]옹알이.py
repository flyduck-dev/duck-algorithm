def solution(babbling):
    answer = 0
    pronunciations = ["aya", "ye", "woo", "ma"]
    
    for ba in babbling:
        for pronunciation in pronunciations:
            if pronunciation in ba:
                ba = ba.replace(pronunciation, " ")   
        if len(ba.strip()) == 0:
            answer += 1

    return answer
