#!/usr/bin/env python3
"""
Problem 2: The banking problem.

  Start with e = 2.71828...
  Year k (k = 1..n): take 1 euro fee, then multiply by k.
  At the end (after n = 50 years): one more 1 euro fee to retrieve the money.

  u_0 = e,   u_k = k * (u_{k-1} - 1),   final = u_50 - 1

CHOICES
-------
1. Interpretation of the order: fee first, then multiplication, each year
   (as written). The final withdrawal fee is applied after year 50.
2. "e" is the true mathematical constant (not the truncated "2.71828"),
   since the banker says e. Computed to 150 digits from the series
   sum 1/k!, using Python's decimal module at 200-digit precision.
3. The key fact: the recursion multiplies any error in e by 50! ~ 3e64.
   So a float-precision e (1e-16 error) gives garbage. We show that
   explicitly, and show how many digits of e are needed.
4. Closed form used as a cross-check. Let u_k / k! = v_k. Then
   v_k = v_{k-1} - 1/(k-1)!, so
       u_n = n! * sum_{k>=n} 1/k!  =  1 + 1/(n+1) + 1/((n+1)(n+2)) + ...
   Hence u_50 ~ 1.02 and the final answer is ~ 0.02 euro, not a fortune.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
import math
import os
from pathlib import Path

N = 50
getcontext().prec = 200


def e_decimal(terms=120):
    """e to ~150+ digits via sum 1/k!."""
    s, term = Decimal(0), Decimal(1)
    for k in range(terms):
        s += term
        term /= (k + 1)
    return s


def invest(e_value, n=N, one=1):
    """Run the banker's scheme; returns amount before the final fee."""
    u = e_value
    for k in range(1, n + 1):
        u = (u - one) * k
    return u


def closed_form(n=N):
    """u_n = n! * sum_{k>=n} 1/k!  (exact tail series, Decimal)."""
    total, term = Decimal(0), Decimal(1)   # term = n!/k! , starts at k = n
    k = n
    while term > Decimal(10) ** -150:
        total += term
        k += 1
        term /= k
    return total



# ---------------------------------------------------------------------------
# Output: everything is printed AND collected, then written to a file.
# Directory: $OUTPUT_DIR (default "/out"); falls back to the current directory
# if the default is not writable.
# ---------------------------------------------------------------------------
_lines = []


def out(text=""):
    print(text)
    _lines.append(str(text))


def write_results(filename):
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/out"))
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except OSError as err:
        print(f"[warning] cannot use {output_dir} ({err}); writing to current directory")
        output_dir = Path(".")
    output_file = output_dir / filename
    output_file.write_text("\n".join(_lines) + "\n", encoding="utf-8")
    print(f"\nResults written to {output_file}")


def main():
    e = e_decimal()
    final_fee = 1

    u = invest(e)
    out(f"Fee-then-multiply for {N} years, starting from e (200-digit arithmetic)")
    out(f"  amount after year {N}:       {u:.12f} EUR")
    out(f"  after final 1 EUR fee:       {u - final_fee:.12f} EUR")

    cf = closed_form()
    out(f"  closed-form cross-check:     {cf - final_fee:.12f} EUR "
          f"(match: {abs((u - cf)) < Decimal(10) ** -100})")

    out("\nWhy it is fragile: errors in e are multiplied by 50! "
          f"= {math.factorial(N):.3e}\n")

    # 1) the banker's quoted value, truncated
    for label, ev in [("e = 2.71828 (as quoted)", Decimal("2.71828")),
                      ("e as Python float (64-bit)", Decimal(math.e))]:
        r = invest(ev) - final_fee
        out(f"  {label:<28s} -> {r:.6e} EUR")

    # 2) plain float arithmetic all the way
    f = math.e
    for k in range(1, N + 1):
        f = (f - 1.0) * k
    out(f"  all-float arithmetic          -> {f - 1.0:.6e} EUR")

    # 3) digits of e needed
    out("\nDigits of e needed for the result to be right to ~1 cent:")
    for d in (10, 30, 60, 65, 70, 80):
        ed = (e).quantize(Decimal(1).scaleb(-d))
        r = invest(ed) - final_fee
        out(f"  {d:3d} decimals -> {r:.4f} EUR")

    out(f"\nANSWER: about {float(u - final_fee):.4f} EUR "
          "(roughly 2 cents) - naive float arithmetic gives an absurd -4e48 EUR.")

    write_results("resultat_banking_llm.txt")


if __name__ == "__main__":
    main()