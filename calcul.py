def calcul(num_1_ok, operator_ok, num_2_ok):
    result = int
    if operator_ok == "+":
        result = num_1_ok + num_2_ok
    elif operator_ok == "-":
        result = num_1_ok - num_2_ok
    elif operator_ok == "/":
        if num_1_ok == 0 or num_2_ok == 0:
            print("Division par 0 impossible")
        else:
            result = num_1_ok / num_2_ok
    elif operator_ok == "*":
        result = num_1_ok * num_2_ok
    return(result)