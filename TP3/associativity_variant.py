"""Run one Python associativity/distributivity feature-model configuration."""
import argparse
import random

try:
    import numpy as np
except ImportError:
    np = None


REPETITIONS = {
    "ten": 10,
    "fifty": 50,
    "fiveThousand": 5_000,
    "OneMillion": 1_000_000,
    "tenMillion": 10_000_000,
}

DISTRIBUTIONS = {
    "SuiteUniformZeroToOne": "uniform_0_1",
    "UniformMinusOneToOne": "uniform_minus1_1",
    "UniformZeroToOneThousand": "uniform_0_1000",
    "StandardNormal": "normal",
    "LogUniformMagnitudeRandomSign": "log_uniform_signed",
    "IntegerZeroToOneThousandAsFloat": "integer_0_1000",
}


def python_draw(rng, distribution):
    if distribution == "uniform_0_1":
        return rng.random()
    if distribution == "uniform_minus1_1":
        return rng.uniform(-1.0, 1.0)
    if distribution == "uniform_0_1000":
        return rng.uniform(0.0, 1000.0)
    if distribution == "normal":
        return rng.gauss(0.0, 1.0)
    if distribution == "log_uniform_signed":
        magnitude = 10.0 ** rng.uniform(-10.0, 10.0)
        return magnitude * rng.choice((-1.0, 1.0))
    if distribution == "integer_0_1000":
        return float(rng.randint(0, 1000))
    raise ValueError(f"Unsupported distribution: {distribution}")


def numpy_draw(rng, distribution, repetitions):
    if distribution == "uniform_0_1":
        return rng.random(repetitions)
    if distribution == "uniform_minus1_1":
        return rng.uniform(-1.0, 1.0, repetitions)
    if distribution == "uniform_0_1000":
        return rng.uniform(0.0, 1000.0, repetitions)
    if distribution == "normal":
        return rng.standard_normal(repetitions)
    if distribution == "log_uniform_signed":
        magnitude = 10.0 ** rng.uniform(-10.0, 10.0, repetitions)
        signs = rng.choice((-1.0, 1.0), repetitions)
        return magnitude * signs
    if distribution == "integer_0_1000":
        return rng.integers(0, 1001, repetitions).astype("float64")
    raise ValueError(f"Unsupported distribution: {distribution}")


def equal_count(x, y, z, problem):
    if problem == "Associativity":
        return (x + y) + z == x + (y + z)
    return x * (y + z) == x * y + x * z


def run(repetitions, distribution, rng_kind, problem, seed):
    if rng_kind == "SeededNumPyOrPythonFallback" and np is not None:
        rng = np.random.default_rng(seed)
        x, y, z = (numpy_draw(rng, distribution, repetitions) for _ in range(3))
        with np.errstate(all="ignore"):
            equal = equal_count(x, y, z, problem)
        return float(100.0 * np.count_nonzero(equal) / repetitions), "numpy"

    rng = random.Random(seed)
    equal = 0
    for _ in range(repetitions):
        x = python_draw(rng, distribution)
        y = python_draw(rng, distribution)
        z = python_draw(rng, distribution)
        if equal_count(x, y, z, problem):
            equal += 1
    engine = ("python-random" if rng_kind == "PythonRandomModule"
              else "python-fallback")
    return 100.0 * equal / repetitions, engine


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repetitions", type=int, required=True)
    parser.add_argument("--distribution", choices=DISTRIBUTIONS, required=True)
    parser.add_argument(
        "--rng",
        choices=("PythonRandomModule", "SeededNumPyOrPythonFallback"),
        required=True,
    )
    parser.add_argument(
        "--problem", choices=("Associativity", "Distributivity"), required=True
    )
    parser.add_argument("--seed", type=int, required=True)
    args = parser.parse_args()
    if args.repetitions <= 0:
        parser.error("--repetitions must be positive")

    answer, engine = run(
        args.repetitions,
        DISTRIBUTIONS[args.distribution],
        args.rng,
        args.problem,
        args.seed,
    )
    print(f"{answer:.12g},{engine}")


if __name__ == "__main__":
    main()
