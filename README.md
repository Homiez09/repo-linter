# Repo Linter

![Repo Linter Example](เดี๋ยวมาใส่จ้า)

Repo Linter is a tool designed to help developers ensure that their GitHub repository names follow best practices for naming conventions, particularly for **kebab-case** formatting. This tool can be easily integrated into your workflow to automatically suggest, enforce, and even update repository names based on common conventions.

## Why Repo Linter?

Naming repositories can sometimes be tricky. Inconsistent naming conventions can lead to confusion and make it harder to manage projects. This tool aims to simplify and standardize the naming process, ensuring that your repositories follow a consistent and readable format.

By using Repo Linter, you’ll be able to:
- Enforce **kebab-case** naming conventions for all repositories.
- Suggest standardized names for repositories that don't follow the convention.
- Provide an easy way to rename repositories to improve consistency across your projects.

## Features

- **Automatic Naming Suggestions**: The tool checks the name of your repositories and suggests a proper **kebab-case** format.
- **Approve or Edit**: Once a name suggestion is made, you can either approve it or manually edit the name.
- **GitHub Integration**: The tool integrates directly with GitHub, fetching your repositories and processing them automatically.
- **CLI Support**: A simple command-line interface (CLI) to use the linter from your terminal.

## Installation

To use Repo Linter, you need to have Python installed. Once that is done, you can install the necessary dependencies.

### Steps :

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/repo-linter.git
   cd repo-linter
    ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your GitHub token:
   - Create a GitHub personal access token with the `repo` scope. [https://github.com/settings/personal-access-tokens](https://github.com/settings/personal-access-tokens)

## Usage

Once you’ve set up Repo Linter, you can use it directly from the command line.

## Linting Repositories

To check your repositories, run the following command:

```bash
python main.py lint-repos "YourGitHubUsername" "YourGitHubToken"
```

Replace `YourGitHubUsername` with your GitHub username.

Replace `YourGitHubToken` with your GitHub Personal Access Token.

## Suggestions and Approvals
Once the linting process is complete, you will be shown the current repository names and the suggested names in kebab-case format. You can approve the suggested names or manually edit them.

```bash
🚨 Current Repository: Repo Linter
💡 Suggested Repository Name: repo-linter
Do you want to use the suggested name? (y/n/edit) [n]: y
✅ Changed name to repo-linter successfully
```

You will be prompted to either approve the name or make edits.
