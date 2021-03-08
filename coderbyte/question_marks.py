# Take an input string parameter and determine if exactly 3 question marks exist 
# between every pair of numbers that add up to 10.
# If so, return true, otherwise return false.

str1 = "arrb6????4xxbl5???eee5"
str2 = "acc?7??sss?3rr1??????5"
str3 = "5??aaaaaaaaaaaaaaaaaaa?5?5"
str4 = "9????1????9??1??9"
str5 = "aa6?9"


def QuestionMarks(s):
    q_count = 0
    first_num = 0
    band = False
    for ch in s:
        if ch.isdigit():
            if first_num + int(ch) == 10:
                if q_count == 3:
                    band = True
            first_num = int(ch)
            q_count = 0
        elif ch == '?':
            q_count += 1
    return band


if __name__ == '__main__':
    print(QuestionMarks(str1))
    print(QuestionMarks(str2))
    print(QuestionMarks(str3))
    print(QuestionMarks(str4))
    print(QuestionMarks(str5))
