# Import math Library
import math
import os
from pathlib import Path


def investment(original, time):
    # Calculate compound interest
    amount = original
    for i in range(time):
        amount = (amount - 1)*time
    
    return amount - 1 

output_dir = Path(os.environ.get("OUTPUT_DIR", "/out"))
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "resultat_banquier.txt"
output_file.write_text(f"{investment(math.e, 50)}")

# print(investment(math.e, 50))