# It was a debugging problem
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        # This line was initially like ->  if s[i] = t[i] which was wrong. (Assignment instead of equal operation)
        if s[i] == t[i]:
            # This line was -> res = '0' which was wrong becase we need to append the result to the previous res each time, so res = res + '0' (or res = res + '1' for the else part)
            res += '0';
        else:
            res += '1';

    return res

s = input()
t = input()
print(strings_xor(s, t))



