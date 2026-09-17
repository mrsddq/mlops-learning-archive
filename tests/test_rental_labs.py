"""Reproducibility checks for three small, bundled CSV examples."""
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
LABS = [
    "S2/9-DockerfilesPythonAppPackaging",
    "S2/10-DockerImagesContainersUploadingToDockerHub",
    "S3/11-PackagingMLModelsUsingPickleContainerizingWithDocker",
]


class RentalLabTests(unittest.TestCase):
    def test_runs_from_arbitrary_directory_with_repeatable_holdout(self):
        with tempfile.TemporaryDirectory() as outside:
            for lab in LABS:
                with self.subTest(lab=lab):
                    command = [sys.executable, str(ROOT / lab / "src/predict_rental.py")]
                    first = subprocess.run(command, cwd=outside, check=True, text=True, capture_output=True, timeout=30)
                    second = subprocess.run(command, cwd=outside, check=True, text=True, capture_output=True, timeout=30)
                    self.assertEqual(first.stdout, second.stdout)
                    match = re.search(r"Root Mean Squared Error \(RMSE\): ([0-9.eE+-]+)", first.stdout)
                    self.assertIsNotNone(match)
                    self.assertGreaterEqual(float(match.group(1)), 0)


if __name__ == "__main__":
    unittest.main()
