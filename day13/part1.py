button_cost = {'A':3, 'B':1}
total_cost = 0

def split_input(line:str):
    x, y = line.split(": ")[1].split(", ")
    x_int = int(x[2::])
    y_int = int(y[2::])
    return (x_int, y_int)

def calc_the_thing(button_A, button_B, prize):
    # print(f"{prize=}, {button_A=}, {button_B=}")
    """
    Solves for x and y given two linear equations:
    button_A[0]*x + button_B[0]*y = prize[0]
    button_A[1]*x + button_B[1]*y = prize[1]

    Parameters:
    button_A (tuple): Coefficients of x in the two equations.
    button_B (tuple): Coefficients of y in the two equations.
    prize (tuple): Right-hand side values of the equations.

    Returns:
    tuple: (x, y), the solution of the equations.
    """
    # Extract values for better readability
    a1, a2 = button_A
    b1, b2 = button_B
    c1, c2 = prize

    # Eliminate x by multiplying equations to match x coefficients
    coeff1 = a2
    coeff2 = a1

    # Scale the equations
    scaled_eq1 = (coeff1 * a1, coeff1 * b1, coeff1 * c1)
    scaled_eq2 = (coeff2 * a2, coeff2 * b2, coeff2 * c2)

    # Subtract scaled equations to eliminate x
    b_combined = scaled_eq2[1] - scaled_eq1[1]
    c_combined = scaled_eq2[2] - scaled_eq1[2]

    # Solve for y
    y = c_combined / b_combined

    # Substitute y into one of the original equations to solve for x
    x = (c1 - b1 * y) / a1

    if x%1!=0 or y%1!=0:
        # print("This machine has no answer")
        return None
    else:
        return x, y



with open("input.txt") as f:
    button_A = None
    button_B = None
    prize = None
    for line in f:
        if "A" in line:
            button_A = split_input(line)
        if "B" in line:
            button_B = split_input(line)
        if "Prize" in line:
            prize = split_input(line)
            machine_result = calc_the_thing(button_A, button_B, prize)
            if machine_result:
                #TODO do something with the results
                total_cost += (machine_result[0] * button_cost['A']) + (machine_result[1] * button_cost['B'])
                print(machine_result)


print(f"De laagste kosten zijn: {total_cost}")


