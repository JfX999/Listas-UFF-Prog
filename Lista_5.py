#1 Palindromo
s = (str(input("Digite: ")))

def eh_palindromo(s):
    if len(s) <= 1:
        return True
    
    if s[0] == s[-1]:
        return eh_palindromo(s[1:-1])

    return False

print(eh_palindromo(s))