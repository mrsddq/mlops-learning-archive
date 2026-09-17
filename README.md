# MLOps Learning Archive

Structured MLOps learning archive covering data workflows, Docker, Kubernetes, Jenkins, Kubeflow, monitoring, and deployment practice.

This repository is maintained as a learning archive. It supports the active `rental-price-mlops-pipeline` and `python-ml-project-template` repos by preserving deeper notes and labs.

## Structure

```text
S1/  ML workflow foundations, Spark, dataframes
S2/  Docker, preprocessing, model packaging
S3/  Kubernetes, pods, deployments, services
S4/  DevOps principles, Jenkins, Kubeflow setup
S5/  Kubeflow, Katib, EKS, pipelines
S6/  advanced MLOps labs
S7/  advanced MLOps labs
docs/
  learning-path.md
  portfolio-extraction-plan.md
```

## How This Repo Should Be Used

- Keep it as a revision archive.
- Extract polished projects into separate repos.
- Use `docs/learning-path.md` to navigate the material.
- Use `docs/portfolio-extraction-plan.md` to decide what should become showcase work.

## Related Active Repos

- `rental-price-mlops-pipeline`
- `python-ml-project-template`
- `devops-learning-archive`

Next upgrade: use `docs/portfolio-extraction-plan.md` to choose one lab that can become a focused, reproducible project.

## Reproduce the small rental labs

The three Docker packaging lessons use bundled CSV data and a seeded 80/20 holdout split. Their scripts locate data relative to the script, so the working directory does not change the result. From the repository root with Python 3.12:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install numpy pandas 'scikit-learn>=1.4,<2'
python -m unittest discover -s tests -v
python S2/9-DockerfilesPythonAppPackaging/src/predict_rental.py
```

The test executes each of the three scripts twice from an unrelated directory and compares its output. It verifies local file resolution and repeatability, not model accuracy on real rental markets. The Docker smoke workflow separately builds and runs the three images. No cloud account, GPU, or external dataset is required for these checks.

Earlier notebooks, Spark examples, and cloud setup notes remain course material; they are not covered by the Python smoke test. The lesson named for pickle packaging currently trains and prints predictions rather than demonstrating a complete artifact registry or serving API. Course attribution and existing notes are retained.
