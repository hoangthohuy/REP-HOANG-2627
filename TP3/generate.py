import subprocess
import sys
from pathlib import Path
from jinja2 import Template

template = Template(Path("assoc.py.jinja").read_text())
properties = {"assoc_add 32-bit float (single precision)": ("(x + y) + z", "x + (y + z)","np.float32(random.random())"),
              "assoc_mul 32-bit float (single precision)": ("(x * y) * z", "x * (y * z)","np.float32(random.random())"),
              "assoc_add 64-bit float (double precision)": ("(x + y) + z", "x + (y + z)","random.random()"),
              "assoc_mul 64-bit float (double precision)": ("(x * y) * z", "x * (y * z)","random.random()"),}
Path("generated").mkdir(exist_ok=True)
for name, (lhs, rhs, type_of_numbers) in properties.items():
    path = Path(f"generated/{name}.py")
    path.write_text(template.render(lhs=lhs, rhs=rhs, repetitions=10000 ,type_of_numbers=type_of_numbers))
    result = subprocess.run([sys.executable, path], capture_output=True, text=True)
    print(name, result.stdout.strip())