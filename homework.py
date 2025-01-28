def calculate_net_salary():
    try:
        gross_salary = input("Enter the gross salary: ")
        gross_salary = float(gross_salary)

        if gross_salary < 0:
            print("Gross salary cannot be negative.")
            return

    except ValueError:
        print("Invalid input: Gross salary must be a number.")
        return

    try:

        num_children = input("Enter the number of children: ")
        num_children = int(num_children)

        if num_children < 0:
            print("Number of children cannot be negative.")
            return

    except ValueError:
        print("Invalid input: Number of children must be an integer.")
        return


    if gross_salary < 1000:
        tax_rate = 10
    elif gross_salary < 2000:
        tax_rate = 12
    elif gross_salary < 4000:
        tax_rate = 14
    else:
        tax_rate = 18


    if gross_salary < 2000:
        child_tax_cut = 1 * num_children
    else:
        child_tax_cut = 0.5 * num_children

    effective_tax_rate = max(tax_rate - child_tax_cut, 0)

    net_salary = gross_salary * (1 - effective_tax_rate / 100)

    print(f"Net salary: {net_salary:.2f}")

calculate_net_salary()