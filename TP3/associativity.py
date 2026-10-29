import argparse
import random
import os
from pathlib import Path


def check_associativity(repetitions):
    num_of_cases_not_equal = 0
    for i in range(repetitions):

        # Generate three random numbers between 0 and 1 (result 82,2%)
        x = random.random()
        y = random.random()
        z = random.random()

        # Generate three random numbers between 1 and 1000000 (result 100%)
        # x= random.randint(1, 1000000)
        # y= random.randint(1, 1000000)
        # z= random.randint(1, 1000000)
        value1 = (x + y) + z
        value2 = x + (y + z)

        if value1 == value2:
            num_of_cases_not_equal += 1
    print(f'Percentage of cases where the two values are equal: {num_of_cases_not_equal/repetitions*100}%')

if __name__ == "__main__":
    # Parse arguments at runtime
    parser = argparse.ArgumentParser(description="Check associativity with own code.")
    parser.add_argument('--repetitions', type=int, required=True, help="Number of repetitions for the check.")


    args = parser.parse_args()

    # Run the property check with runtime arguments
    check_associativity(args.repetitions)



#For running with Docker
# output_dir = Path(os.environ.get("OUTPUT_DIR", "/out"))
# output_dir.mkdir(parents=True, exist_ok=True)

# output_file = output_dir / "resultat_associativity.txt"
# output_file.write_text(f"{num_of_cases_not_equal/1000000*100}%")

# print(f'Percentage of cases where the two values are equal: {num_of_cases_not_equal/1000000*100}%')
#For running with nix
# output_file = Path("./resultat_associativity.txt")
# output_file.write_text(f"{num_of_cases_not_equal/1000000*100}%")

# print(f'Percentage of cases where the two values are equal: {num_of_cases_not_equal/1000000*100}%')