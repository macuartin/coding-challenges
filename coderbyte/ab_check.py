# challenge: https://coderbyte.com/information/AB%20Check

def ABCheck(strParam):

    # code goes here
    i = 0
    has_3 = 'false'
    while i < len(strParam)-4:
        if strParam[i] == 'a' and strParam[i+4] == 'b':
            has_3 = 'true'
        elif strParam[i] == 'b' and strParam[i+4] == 'a':
            has_3 = 'true'
        i += 1
    return has_3


# keep this function call here
print ABCheck(raw_input())
