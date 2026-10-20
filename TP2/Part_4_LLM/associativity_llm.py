"""
Problem 1: How often is (x + y) + z == x + (y + z) ?

The question is under-specified, so here are the choices I made.
They are part of the result.

CHOICES
-------
1. "number" = IEEE 754 binary64 floating-point (Python `float`, a C double),
   the default number type on nearly every machine. Mathematically the answer
   would be 100% (addition of reals is associative), so the interesting
   question is about floats.
2. Rounding mode = round-to-nearest, ties-to-even (the IEEE default; this is
   what Python uses).
3. "How often" requires a probability distribution. Main result: x, y, z are
   independent and uniform on [0, 1). Reason: it is the most common default
   ("random()"), and every value is finite (no NaN / inf, which would make
   == fail trivially because NaN != NaN, or overflow to inf).
   Other distributions are reported too, because the answer depends heavily
   on that choice.
4. Sampling: Monte Carlo with N = 10,000,000 triples and a fixed seed, so the
   run is reproducible. Uses numpy (vectorised float64 arithmetic is the same
   IEEE arithmetic as scalar Python floats). Falls back to pure Python with
   fewer samples if numpy is missing.
5. "Equal" = exactly equal bit patterns (==). No tolerance: a tolerance would
   change the question into "approximately associative".
6. Cases where both sides are inf/NaN are excluded by construction (finite
   inputs, magnitudes far from overflow).
"""
import random
import sys
import os
from pathlib import Path

SEED = 12345
N = 10_000_000       # numpy
N_PURE = 1_000_000   # pure python fallback

try:
    import numpy as np
except ImportError:
    np = None


def pct_numpy(draw, n=N):
    """draw(rng, n) -> array of n float64 numbers."""
    rng = np.random.default_rng(SEED)
    x, y, z = draw(rng, n), draw(rng, n), draw(rng, n)
    with np.errstate(all="ignore"):
        eq = ((x + y) + z) == (x + (y + z))
    return 100.0 * eq.mean()


def pct_pure(draw, n=N_PURE):
    rnd = random.Random(SEED)
    eq = 0
    for _ in range(n):
        x, y, z = draw(rnd), draw(rnd), draw(rnd)
        if (x + y) + z == x + (y + z):
            eq += 1
    return 100.0 * eq / n


# name -> (numpy sampler, pure-python sampler)
DISTRIBUTIONS = {
    "uniform [0, 1)                 (MAIN RESULT)": (
        lambda r, n: r.random(n),
        lambda r: r.random()),
    "uniform [-1, 1)": (
        lambda r, n: r.uniform(-1, 1, n),
        lambda r: r.uniform(-1, 1)),
    "uniform [0, 1000)": (
        lambda r, n: r.uniform(0, 1000, n),
        lambda r: r.uniform(0, 1000)),
    "standard normal": (
        lambda r, n: r.standard_normal(n),
        lambda r: r.gauss(0, 1)),
    "log-uniform magnitude 1e-10..1e10, random sign": (
        lambda r, n: 10.0 ** r.uniform(-10, 10, n) * r.choice([-1.0, 1.0], n),
        lambda r: 10.0 ** r.uniform(-10, 10) * r.choice([-1.0, 1.0])),
    "integers 0..1000 stored as floats (exact)": (
        lambda r, n: r.integers(0, 1001, n).astype(np.float64),
        lambda r: float(r.randint(0, 1000))),
}



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
    engine = "numpy" if np is not None else "pure Python"
    n = N if np is not None else N_PURE
    out(f"Type: IEEE 754 binary64, round-to-nearest-even | engine: {engine} | "
          f"samples: {n:,} | seed: {SEED}\n")
    out("Percentage of triples with (x+y)+z == x+(y+z):\n")
    for name, (np_draw, py_draw) in DISTRIBUTIONS.items():
        p = pct_numpy(np_draw) if np is not None else pct_pure(py_draw)
        out(f"  {name:<50s} {p:6.2f} %")
    out("\nAnswer (x, y, z i.i.d. uniform in [0, 1)): about 83 %.")

    write_results("resultat_associativity_llm.txt")


if __name__ == "__main__":
    sys.exit(main())