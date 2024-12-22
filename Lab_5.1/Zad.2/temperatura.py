def c_to_f(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit,2)

def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return round(celsius,2)

def  c_to_k(celsius):
    kelvin = celsius + 273.15
    return round(kelvin,2)
