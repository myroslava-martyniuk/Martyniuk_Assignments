def f_to_c(temp_f: str):
    temp_c = 5/9*(int(temp_f) - 32)
    return str(int(temp_c))+"В°C"

def c_to_f(temp_c: str):
    temp_f = (9*int(temp_c))/5+32
    return str(int(temp_f))+"В°F"
