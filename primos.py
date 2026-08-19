def e_primo(n):
    if(n < 2):
        return False;
    p = 2;
    while(n!=p):
        if(n%p == 0): return False;
        p+=1
    return True

print(e_primo(int(input())))