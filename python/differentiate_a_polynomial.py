def derivative(f,x):
    f = f.replace(' ','')
    coef,power,x_count = [],[],f.count('x')
    while f.count('x') > 0:
        x_index = f.index('x')
        plus_index = f.index('+',x_index) if '+' in f[x_index:] else len(f) - 1
        minus_index = f.index('-',x_index) if '-' in f[x_index:] else len(f) - 1
        sign_index = min(plus_index,minus_index)
        coef += [1] if x_index == 0 else [-1] if f[x_index-1] == '-' else [float(f[:x_index])]
        if (x_index < len(f) - 1) and (f[x_index+1] == '^'):
            power += [float(f[x_index+2:sign_index])] if sign_index < len(f) - 1 else [float(f[x_index+2:sign_index+1])]
        else:
            power += [1]
        f = f[sign_index + 1:] if f[sign_index] == '+' else f[sign_index:] if  f[sign_index] == '-' else ''
    return sum(coef[i]*power[i]*x**(power[i]-1) for i in range(x_count))
'''
Calculate the derivative of f(x) at a given x.
Coefficients, powers and constants must be real numbers only, without brackets
and powers don't have signs (+/-).
'''
print(derivative('-2x^5+5x^3-3x^0.5+10000',10)) # returns -98500.47