def m_to_f(meter: str):
    feet = (int(meter) / 0.3048)
    return str(int(feet))+"ft"

def f_to_m(feet: str):
    meter = (int(feet)) * 0.3048
    return str(int(meter))+"m"