'''
Convert to the quaternary numeral system of the tines!
(as described in Vernor Vinge's "A Fire Upon the Deep")
'''

def toQuaternary(decimalInput):
    try:
        if "." in decimalInput:
                decimalInput = float(decimalInput)
        decimalInput = int(decimalInput)
    except:
        return "not allowed"
    negative = False
    if decimalInput == 0:
        return "O"
    elif decimalInput < 0:
        decimalInput *= -1
        negative = True
    quaternaryOutput = ""
    while decimalInput != 0:
        remainder = decimalInput % 4
        if remainder == 0:
            quaternaryOutput = "O" + quaternaryOutput
        elif remainder == 1:
            quaternaryOutput = "I" + quaternaryOutput
        elif remainder == 2:
            quaternaryOutput = "X" + quaternaryOutput
        else:
            quaternaryOutput = "Δ" + quaternaryOutput
        decimalInput //= 4
    if negative:
        return "-" + quaternaryOutput
    return quaternaryOutput

while (True):
    number = input("number: ")
    if number == "exit":
        break;
    print(toQuaternary(number))
