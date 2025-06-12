# Loan Calculator

This is a command-line loan calculator written in Python. It supports calculating both annuity and differentiated loan payments based on user-supplied parameters.

---

## Features

- Calculate **annuity payments** (fixed monthly payments)
- Calculate **differentiated payments** (payments decrease over time)
- Compute loan principal, number of periods, or monthly payment depending on which parameters are provided
- Calculate overpayment amount
- Validate input parameters and handle incorrect or missing inputs gracefully

---

## Usage

Run the program from the command line with the following arguments:
python3 creditcalc.py –type=TYPE –principal=PRINCIPAL –payment=PAYMENT –periods=PERIODS –interest=INTEREST


### Arguments

- `--type` (required): Type of payment calculation. Must be either `annuity` or `diff` (differentiated).
- `--principal`: Loan principal amount (float).
- `--payment`: Monthly payment amount (float).
- `--periods`: Number of months to repay the loan (integer).
- `--interest` (required): Annual interest rate (as a percentage, float).

---

## Examples

Calculate differentiated payments:
python3 creditcalc.py –type=diff –principal=1000000 –periods=10 –interest=10


Calculate annuity monthly payment:
python3 creditcalc.py –type=annuity –principal=500000 –periods=24 –interest=7.8


Calculate loan principal:
python3 creditcalc.py –type=annuity –payment=8722 –periods=120 –interest=5.6

---

## Notes

- For `diff` type, the `--payment` argument should **not** be provided.
- All numeric parameters must be positive.
- The program will output `Incorrect parameters` and exit if input validation fails.
- Interest rate must always be provided.
- Payments are rounded up to the nearest integer as per banking standards.

---

## Requirements

- Python 3.x

---

## How to run

1. Save the `creditcalc.py` script.
2. Open terminal or command prompt.
3. Run the script with appropriate arguments as shown above.

---

## License

This project is provided as-is for educational purposes.
