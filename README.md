# Docker Image Generation Demo

A demonstration of building and hosting Docker images on GitHub using GitHub Actions and GitHub Container Registry (GHCR).

## Overview

This repository demonstrates how to set up automated Docker image builds that work seamlessly when forked, allowing each user to generate their own private Docker image hosted on GitHub Container Registry.

## Building Your Private Image

Due to licensing restrictions, pre-built images are not distributed. Each user must build their own image.

### Quick Start

1. **Fork this repository** to your GitHub account

2. **Enable GitHub Actions** in your fork:
   - Go to **Settings** → **Actions** → **General**
   - Under "Actions permissions", select **"Allow all actions and reusable workflows"**
   - Click **Save**

3. **Enable workflows** (if needed):
   - Go to the **Actions** tab in your forked repository
   - If workflows are disabled, click **"I understand my workflows, enable them"**

4. **Trigger the build**:
   - **Option A**: Push any commit to the `main` branch
   - **Option B**: Go to **Actions** tab → Select "Build Private Docker Image" → Click **"Run workflow"** → Click **"Run workflow"** button

5. **Set package visibility to Private**:
   - Go to your GitHub profile → **Packages**
   - Find the package named `docker-image-gen` (or your repo name)
   - Click on the package → **Package settings** → **Change visibility** → Select **Private**

### Using Your Image

Once built, your image will be available at:

```
ghcr.io/<your-username>/docker-image-gen:latest
```

#### Pull the image:

```bash
docker pull ghcr.io/<your-username>/docker-image-gen:latest
```

#### Run the container:

```bash
docker run -p 8000:8000 ghcr.io/<your-username>/docker-image-gen:latest
```

#### Access the application:

Visit `http://localhost:8000` in your browser to see the demo API response.

#### Authenticate with GHCR (if needed):

If you encounter authentication issues when pulling:

```bash
echo $GITHUB_TOKEN | docker login ghcr.io -u <your-username> --password-stdin
```

Or use a Personal Access Token (PAT) with `read:packages` permission.

## How It Works

### GitHub Actions Workflow

The workflow (`.github/workflows/docker-build.yml`) automatically:
- Builds a Docker image when triggered
- Pushes to GitHub Container Registry under your namespace
- Uses `github.repository` to automatically resolve to the fork owner's namespace
- Tags images with `latest` and commit SHA

### Key Features

- **Fork-friendly**: Uses `${{ github.repository }}` which automatically resolves to the fork owner's namespace
- **Manual trigger**: Includes `workflow_dispatch` for manual builds without commits
- **Automatic authentication**: Uses `GITHUB_TOKEN` with appropriate permissions
- **Multiple tags**: Tags images with branch name, SHA, and `latest`

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── docker-build.yml    # GitHub Actions workflow
├── app.py                      # Simple Python web server demo
├── Dockerfile                  # Docker image definition
├── requirements.txt            # Python dependencies (none for this demo)
├── .dockerignore              # Files to exclude from Docker build
└── README.md                  # This file
```

## License

See [LICENSE](LICENSE) file for details.

## Troubleshooting

### Workflow doesn't run in fork
- Ensure Actions are enabled in your fork's Settings
- Check that you've enabled workflows in the Actions tab
- Verify you have write access to the forked repository

### Can't pull the image
- Ensure the package visibility is set correctly (Private or Public)
- Authenticate with GHCR using your GitHub token
- Check that the workflow completed successfully

### Build fails
- Check the Actions tab for error logs
- Ensure the Dockerfile is valid
- Verify all required files are present in the repository
