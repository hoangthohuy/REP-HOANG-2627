import random
import os
from pathlib import Path

num_of_cases_not_equal = 0
for i in range(1000000):

    # Generate three random numbers between 0 and 1 (result 82,2%)
    x= random.random()
    y= random.random()
    z =random.random()

    # Generate three random numbers between 1 and 1000000 (result 100%)
    # x= random.randint(1, 1000000)
    # y= random.randint(1, 1000000)
    # z= random.randint(1, 1000000)
    value1 = x * (y + z)

    

    value2 =  x * y + x * z
    

    if value1 == value2:
        num_of_cases_not_equal += 1

#For running with Docker
output_dir = Path(os.environ.get("OUTPUT_DIR", "/out"))
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "resultat_distributivity.txt"
output_file.write_text(f"{num_of_cases_not_equal/1000000*100}%")

print(f'Percentage of cases where the two values are equal: {num_of_cases_not_equal/1000000*100}%')
#For running with nix
# output_file = Path("./resultat_distributivity.txt")
# output_file.write_text(f"{num_of_cases_not_equal/1000000*100}%")

# print(f'Percentage of cases where the two values are equal: {num_of_cases_not_equal/1000000*100}%')