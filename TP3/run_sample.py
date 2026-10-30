"""Run sampled Python configurations repeatedly and save their results."""
import argparse
import csv
import subprocess
import sys
from pathlib import Path

from associativity_variant import DISTRIBUTIONS, REPETITIONS


FACTORS = (
    "Language",
    "Repetitions",
    "DistributionCoverage",
    "RandomNumberGenerator",
    "TypeOfProblem",
)
OUTPUT_COLUMNS = (
    "config_id",
    "origin_of_config",
    *FACTORS,
    "run_number",
    "seed",
    "answer_percent",
    "actual_engine",
)


def main():
    parser = argparse.ArgumentParser(
        description="Run each Python sample configuration repeatedly."
    )
    parser.add_argument(
        "sample_csv", nargs="?", type=Path,
        default=Path(__file__).with_name("sample.csv"))
    parser.add_argument("--runs", type=int, default=3,
                        help="independent runs per Python configuration (default: 3)")
    parser.add_argument("--seed", type=int, default=1,
                        help="base seed; each run uses base seed + run number")
    parser.add_argument(
        "-o", "--output", type=Path,
        default=Path(__file__).with_name("results.csv"))
    parser.add_argument("--python", default=sys.executable,
                        help="Python executable used to run each variant")
    args = parser.parse_args()
    if args.runs <= 0:
        parser.error("--runs must be positive")

    sample_path = args.sample_csv.resolve()
    output_path = args.output.resolve()
    variant_path = Path(__file__).with_name("associativity_variant.py").resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with sample_path.open(newline="", encoding="utf-8-sig") as sample_file:
        reader = csv.DictReader(sample_file)
        missing = {"config_id", "origin_of_config", *FACTORS} - set(reader.fieldnames or ())
        if missing:
            parser.error(f"{sample_path} is missing columns: {', '.join(sorted(missing))}")
        python_configs = [
            row for row in reader if row.get("Language", "").strip() == "Python"
        ]

    if not python_configs:
        parser.error(f"{sample_path} contains no Python configurations")

    with output_path.open("w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        for config in python_configs:
            for run_number in range(1, args.runs + 1):
                seed = args.seed + run_number - 1
                try:
                    repetitions = REPETITIONS[config["Repetitions"].strip()]
                    distribution = config["DistributionCoverage"].strip()
                    if distribution not in DISTRIBUTIONS:
                        raise ValueError(f"unsupported distribution {distribution!r}")
                    rng_kind = config["RandomNumberGenerator"].strip()
                    if rng_kind not in (
                        "PythonRandomModule",
                        "SeededNumPyOrPythonFallback",
                    ):
                        raise ValueError(f"unsupported Python RNG {rng_kind!r}")
                    problem = config["TypeOfProblem"].strip()
                    if problem not in ("Associativity", "Distributivity"):
                        raise ValueError(f"unsupported problem {problem!r}")
                except (KeyError, ValueError) as error:
                    raise ValueError(
                        f"invalid Python configuration {config.get('config_id')}: {error}"
                    ) from error

                command = [
                    args.python,
                    str(variant_path),
                    "--repetitions", str(repetitions),
                    "--distribution", distribution,
                    "--rng", rng_kind,
                    "--problem", problem,
                    "--seed", str(seed),
                ]
                completed = subprocess.run(
                    command, capture_output=True, text=True
                )
                if completed.returncode != 0:
                    raise RuntimeError(
                        f"variant failed for {config['config_id']} run {run_number} "
                        f"(exit {completed.returncode}):\n{completed.stderr}"
                    )
                try:
                    answer, engine = completed.stdout.strip().split(",", maxsplit=1)
                    answer_percent = float(answer)
                except (ValueError, TypeError) as error:
                    raise RuntimeError(
                        f"unexpected output from {variant_path}: "
                        f"{completed.stdout!r}"
                    ) from error

                writer.writerow({
                    "config_id": config["config_id"],
                    "origin_of_config": config["origin_of_config"],
                    **{factor: config[factor] for factor in FACTORS},
                    "run_number": run_number,
                    "seed": seed,
                    "answer_percent": answer_percent,
                    "actual_engine": engine,
                })
                output_file.flush()

    print(
        f"Wrote {len(python_configs) * args.runs} runs "
        f"({len(python_configs)} Python configurations; C++ rows skipped) "
        f"to {output_path}"
    )


if __name__ == "__main__":
    main()
