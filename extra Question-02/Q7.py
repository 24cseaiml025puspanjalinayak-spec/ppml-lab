def palindrome_check(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome_check(s[1:-1])

print(palindrome_check("pop"))  