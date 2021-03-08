# challenge: https://coderbyte.com/information/Questions%20Marks

def QuestionsMarks(strParam):
    q_count = 0
    first_num = 0
    band = 'false'
    for ch in strParam:
        if ch.isdigit():
            if first_num + int(ch) == 10:
                if q_count == 3:
                    band = 'true'
            first_num = int(ch)
            q_count = 0
        elif ch == '?':
            q_count += 1
    return band


# keep this function call here
print QuestionsMarks(raw_input())
