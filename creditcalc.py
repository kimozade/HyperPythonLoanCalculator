import math
import argparse

def check_parameters(args):
    if args.type not in ["annuity", "diff"]:
        return False
    
    if args.interest is None:
        return False
        
    if args.type == "diff" and args.payment is not None:
        return False
        
    # Check that all provided values are positive
    for value in [args.principal, args.payment, args.periods, args.interest]:
        if value is not None and value < 0:
            return False
            
    # Count how many parameters are provided (excluding type and interest)
    params = [args.principal, args.payment, args.periods]
    count = sum(1 for p in params if p is not None)
    if count != 2:  # We need exactly 2 (third will be calculated)
        return False
        
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--principal", type=float)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)
    parser.add_argument("--payment", type=float)
    parser.add_argument("--type", type=str)
    
    try:
        args = parser.parse_args()
        if not check_parameters(args):
            print("Incorrect parameters")
            return

        P = args.principal
        n = args.periods
        I = args.interest
        A = args.payment
        T = args.type

        i = I / 12 / 100  # monthly rate

        def print_time(months):
            years = months // 12
            months = months % 12
            parts = []
            if years == 1:
                parts.append("1 year")
            elif years > 1:
                parts.append(f"{years} years")
            if months == 1:
                parts.append("1 month")
            elif months > 1:
                parts.append(f"{months} months")
            print("It will take " + " and ".join(parts) + " to repay this loan!")

        if T == "annuity":
            if P is None:
                P = A * ((1 + i)**n - 1) / (i * (1 + i)**n)
                total = 0
                m = 1
                while m <= n:
                    D = P / n + i * (P - (P * (m - 1)) / n)
                    total += math.ceil(D)
                    m += 1
                print(f"Your loan principal = {int(round(P))}\nOverpayment = {math.ceil((A * n) - P)}")
            elif A is None:
                A = P * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
                monthly_payment_ceil = math.ceil(A)
                overpayment = monthly_payment_ceil * n - P
                print(f"Your monthly payment = {monthly_payment_ceil}!")
                print(f"Overpayment = {int(overpayment)}")
            elif n is None:
                n = math.log(A / (A - i * P), 1 + i)
                n_ceil = math.ceil(n)
                print_time(n_ceil)
                print(f"Overpayment = {int(math.ceil(A * n_ceil) - P)}")
        elif T == "diff":
            if P is None:
                P = A / n
                total = 0
                m = 1
                while m <= n:
                    D = P / n + i * (P - (P * (m - 1)) / n)
                    total += math.ceil(D)
                    m += 1
                print(f"Your loan principal = {int(round(P))}\nOverpayment = {math.ceil(total - P)}")
            elif A is None:
                total = 0
                m = 1
                while m <= n:
                    D = P / n + i * (P - (P * (m - 1)) / n)
                    print(f"Month {m}: payment is {math.ceil(D)}")
                    total += math.ceil(D)
                    m += 1
                print(f"Overpayment = {math.ceil(total - P)}")
    except:
        print("Incorrect parameters")

if __name__ == '__main__':
    main()