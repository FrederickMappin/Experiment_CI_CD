## Learning GitHub Actions

This repository is a hands-on practice project for learning how GitHub Actions automates code quality checks in a Python codebase.

## Goal

Use small, practical workflows to understand how CI (Continuous Integration) works when code is pushed or reviewed in pull requests.

## What I Am Learning

- How to trigger workflows on `push` and `pull_request`
- How to set up a Python environment in GitHub Actions
- How to install project dependencies in a clean runner
- How to run linting and tests automatically
- How workflow feedback helps catch issues before merge

## Purpose of `ci.yml`

The workflow file at `.github/workflows/ci.yml` is your main CI pipeline.

It is designed to:

1. Run on every push to `main` and every pull request targeting `main`.
2. Check out your repository code.
3. Install Python `3.10`.
4. Install dependencies from `requirements.txt`.
5. Run `flake8` to enforce linting standards.
6. Run `pytest` to validate functionality through tests.

In short, `ci.yml` helps ensure that new changes are clean, testable, and less likely to break the project.

## Docker Packaging Workflow

The workflow file `.github/workflows/docker-publish.yml` builds a Docker image for this project and packages it as a workflow artifact.

It runs on pushes to `main` (and can be started manually with `workflow_dispatch`) and does the following:

1. Checks out your code.
2. Builds the image using `Dockerfile` at the repository root.
3. Exports the built image as `simplecalculator-image.tar`.
4. Uploads that tar file as a GitHub Actions artifact.

### Download the Package

After the workflow runs, open the workflow run in GitHub and download the artifact named `simplecalculator-docker-image`.

You can load it locally with:

`docker load -i simplecalculator-image.tar`

## Why This Matters

By using this workflow, you get fast and consistent validation of your code. This builds good engineering habits and makes collaboration safer as the project grows.
