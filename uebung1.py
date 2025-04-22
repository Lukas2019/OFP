def m_to_cm(meter):
    meter = float(meter)
    return meter*100

user_input= input("Länge in Meter: ")

print(str(m_to_cm(user_input))+" m")