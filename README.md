# BeCode CI/CD GitHub Actions Challenge

This repository demonstrates a simple CI/CD pipeline with GitHub Actions for a BeCode challenge. It uses a small Streamlit application to show how a deployment environment can change application behavior through the `APP_ENV` variable.

The goal is not to deploy a production application. Instead, the project simulates Dev, QA, and Prod deployments so the GitHub Actions workflow, branch strategy, and GitHub Environments approval flow are easy to understand.

## Repository Structure

```text
.
├── .github/
│   └── workflows/
│       ├── ci.yml              # Runs linting and tests on pull requests to main
│       └── cd.yml              # Simulates deployments for dev, qa, and main
├── app/
│   └── streamlit_app.py        # Streamlit app with environment-based styling
├── assets/
│   ├── Capture d'écran 2026-05-29 120950.png
│   ├── Capture d'écran 2026-05-29 121124.png
│   ├── Capture d'écran 2026-05-29 122845.png
│   ├── Capture d'écran 2026-05-29 123756.png
│   └── Capture d'écran 2026-05-29 123829.png
├── tests/
│   └── test_app.py             # Tests for environment configuration
├── main.py                     # Small entry point for checking the app config
├── pytest.ini                  # Ensures tests can import the local app package
├── requirements.txt            # Python dependencies
└── README.md
```

## Tech Stack

- Python
- Streamlit
- Pytest
- Ruff
- GitHub Actions
- GitHub Environments

## CI/CD Overview

The project has two GitHub Actions workflows:

- **CI**: runs on pull requests targeting `main`.
- **CD**: runs on pushes to `dev`, `qa`, and `main`.

The CI workflow installs the Python dependencies, checks code quality with Ruff, and runs the test suite with Pytest.

The CD workflow simulates deployments by checking which branch was pushed and then running the matching deployment job:

- Push to `dev` deploys to **Dev**.
- Push to `qa` deploys to **QA**.
- Push to `main` deploys to **Prod**.

## Branch Strategy

The intended flow is:

```text
feature branch -> dev -> qa -> main
```

Typical workflow:

1. Create a feature branch for your changes.
2. Merge the feature branch into `dev` to trigger a Dev deployment.
3. Merge `dev` into `qa` to trigger a QA deployment.
4. Merge `qa` into `main` to trigger CI and, after approval, a Prod deployment.

## Continuous Integration

CI is triggered when a pull request is opened or updated against `main`.

```yaml
on:
  pull_request:
    branches:
      - main
```

The CI workflow runs:

```bash
ruff check .
pytest
```

This helps confirm that code is formatted consistently, linted, and covered by the existing tests before changes are merged into `main`.

## Continuous Deployment

CD is triggered when code is pushed to one of the deployment branches:

```yaml
on:
  push:
    branches:
      - dev
      - qa
      - main
```

### Dev Deployment

Push or merge changes into the `dev` branch:

```bash
git checkout dev
git merge feature/my-change
git push origin dev
```

Expected deployment log:

```text
🚀 Deployed to 'Dev'
APP_ENV: dev
```

### QA Deployment

Push or merge changes into the `qa` branch:

```bash
git checkout qa
git merge dev
git push origin qa
```

Expected deployment log:

```text
🚀 Deployed to 'QA'
APP_ENV: qa
```

### Prod Deployment

Push or merge changes into the `main` branch:

```bash
git checkout main
git merge qa
git push origin main
```

Expected deployment log after approval:

```text
🚀 Deployed to 'Prod'
APP_ENV: prod
```

## GitHub Environments

The CD workflow uses GitHub Environments to separate deployment targets:

- `Dev`
- `QA`
- `Prod`

Each deployment job declares its environment in `.github/workflows/cd.yml`:

```yaml
environment:
  name: Prod
```

GitHub Environments make deployments more visible in the repository and allow extra protection rules, such as required reviewers, to be added per environment.

## Production Approval

The `Prod` environment should be configured in GitHub with a required reviewer. This creates a manual approval step before the production deployment job can continue.

To configure this in GitHub:

1. Go to **Settings**.
2. Open **Environments**.
3. Select or create `Prod`.
4. Enable **Required reviewers**.
5. Add the reviewer who must approve production deployments.

With this setup, pushes to `main` start the Prod deployment, but the deployment waits until the required reviewer approves it.

## Streamlit App Behavior

The Streamlit app reads `APP_ENV` and updates the title and background color:

| `APP_ENV` | Title | Background |
| --- | --- | --- |
| `dev` | Dev Environment | Green |
| `qa` | QA Environment | Yellow |
| `prod` | Production Environment | Red |

If `APP_ENV` is missing or unknown, the app falls back to the Dev configuration.

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app with the default Dev environment:

```bash
streamlit run app/streamlit_app.py
```

Run the app for a specific environment:

```bash
APP_ENV=dev streamlit run app/streamlit_app.py
APP_ENV=qa streamlit run app/streamlit_app.py
APP_ENV=prod streamlit run app/streamlit_app.py
```

## Screenshots

### Pull Request Deployment Status

![Pull request deployment status](assets/Capture%20d%27%C3%A9cran%202026-05-29%20120950.png)

### GitHub Actions Deployment Jobs

![GitHub Actions deployment jobs](assets/Capture%20d%27%C3%A9cran%202026-05-29%20121124.png)

### Dev Deployment Checks

![Dev deployment checks](assets/Capture%20d%27%C3%A9cran%202026-05-29%20122845.png)

### QA Deployment Checks

![QA deployment checks](assets/Capture%20d%27%C3%A9cran%202026-05-29%20123756.png)

### Prod Deployment Checks

![Prod deployment checks](assets/Capture%20d%27%C3%A9cran%202026-05-29%20123829.png)

## Checks

Before submitting changes, run:

```bash
pytest
ruff check .
git status
```

## Learning Outcomes

This challenge demonstrates how to:

- Build a basic CI workflow for pull requests.
- Build a branch-based CD workflow.
- Use GitHub Actions conditions to choose the correct deployment job.
- Pass an environment variable into a deployment step.
- Use GitHub Environments to separate Dev, QA, and Prod.
- Protect production deployments with manual approval.
- Connect a small application behavior change to deployment environment configuration.
