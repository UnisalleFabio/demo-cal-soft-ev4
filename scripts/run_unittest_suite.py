from __future__ import annotations

import argparse
import json
import os
import sys
import unittest
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Ejecuta una suite de unittest y guarda un resumen en JSON.",
    )
    parser.add_argument(
        "--suite-name",
        required=True,
        help="Nombre legible de la suite.",
    )
    parser.add_argument(
        "--pattern",
        required=True,
        help="Patrón de descubrimiento para unittest.",
    )
    parser.add_argument(
        "--results-file",
        required=True,
        help="Ruta del archivo JSON de salida, relativa a la raíz del proyecto.",
    )
    return parser.parse_args()


def build_summary(args: argparse.Namespace, result: unittest.TestResult) -> dict[str, object]:
    failures = len(result.failures)
    errors = len(result.errors)
    skipped = len(getattr(result, "skipped", []))
    expected_failures = len(getattr(result, "expectedFailures", []))
    unexpected_successes = len(getattr(result, "unexpectedSuccesses", []))

    passed = result.testsRun - failures - errors - skipped - expected_failures - unexpected_successes
    successful = result.wasSuccessful() and result.testsRun > 0

    return {
        "suite_name": args.suite_name,
        "pattern": args.pattern,
        "ran": result.testsRun,
        "passed": max(passed, 0),
        "failures": failures,
        "errors": errors,
        "skipped": skipped,
        "expected_failures": expected_failures,
        "unexpected_successes": unexpected_successes,
        "successful": successful,
    }


def write_results(results_file: Path, summary: dict[str, object]) -> None:
    results_file.parent.mkdir(parents=True, exist_ok=True)
    results_file.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def write_github_outputs(summary: dict[str, object]) -> None:
    github_output = os.getenv("GITHUB_OUTPUT")
    if not github_output:
        return

    with Path(github_output).open("a", encoding="utf-8") as handle:
        for key, value in summary.items():
            handle.write(f"{key}={value}\n")


def main() -> int:
    args = parse_args()
    project_root = Path(__file__).resolve().parents[1]
    results_file = project_root / args.results_file

    suite = unittest.defaultTestLoader.discover(
        start_dir=str(project_root / "tests"),
        pattern=args.pattern,
    )

    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
    result = runner.run(suite)

    summary = build_summary(args, result)
    write_results(results_file, summary)
    write_github_outputs(summary)

    print(
        f"Resumen de {args.suite_name} guardado en {results_file} "
        f"({summary['passed']}/{summary['ran']} pruebas aprobadas)."
    )

    if summary["successful"]:
        return 0

    if summary["ran"] == 0:
        print(f"La suite {args.suite_name} no encontró pruebas para el patrón {args.pattern}.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
