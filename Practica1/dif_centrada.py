def aprox_derivada(f,x,h=0.0001):
    df =(f(x+h) - f(x-h))/(2.0*h)
    return df
	
def aprox_2a_derivada(f,x,h=0.0001):
    ddf =(f(x+h) - 2.0*f(x) + f(x-h))/h**2
    return ddf