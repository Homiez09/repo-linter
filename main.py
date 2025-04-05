import requests
import re
import typer
from typing import Optional

app = typer.Typer()

GITHUB_API_URL = "https://api.github.com/users/{owner}/repos?per_page=100&page={page}"

def is_kebab_case(name: str) -> bool:
    return bool(re.match(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', name))

def suggest_kebab_case(name: str) -> str:
    return name.lower().replace(" ", "-").replace("_", "-")

def is_owner_in_repo_name(name: str, owner: str) -> bool:
    return owner.lower() in name.lower()

def is_repo_disabled(repo: dict) -> bool:
    return repo.get("disabled", False)

def get_repos(owner: str, token: str):
    repos = []
    page = 1
    while True:
        url = GITHUB_API_URL.format(owner=owner, page=page)
        headers = {"Authorization": f"token {token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            current_page_repos = response.json()
            if not current_page_repos:
                break
            repos.extend(current_page_repos)
            page += 1
        else:
            raise Exception(f"Failed to fetch repos: {response.status_code}")
    return repos

@app.command()
def lint_repos(owner: str, token: str):
    try:
        repos = get_repos(owner, token)
        
        if not repos:
            typer.echo("❌ No repositories found.")
            return
        
        for repo in repos:
            current_name = repo['name']
            if is_repo_disabled(repo):
                typer.echo(f"❌ Repo '{current_name}' is disabled.")
                continue
            
            if is_owner_in_repo_name(current_name, owner):
                typer.echo(f"✅ Repo '{current_name}' is already in the correct format.")
                continue
            
            if not is_kebab_case(current_name):
                suggested_name = suggest_kebab_case(current_name)
                typer.echo(f"\n🚨 Current Repository: {current_name}")
                typer.echo(f"💡 Suggested Repository Name: {suggested_name}")
                
                choice = typer.prompt("Do you want to use the suggested name? (y/n/edit)", default="n")
                if choice.lower() == "y":
                    change_repo_name(owner, current_name, suggested_name, token)
                    typer.echo(f"✅ Changed name to {suggested_name} successfully")
                elif choice.lower() == "edit":
                    new_name = typer.prompt("Enter new name", default=suggested_name)
                    
                    change_repo_name(owner, current_name, new_name, token)
                    typer.echo(f"✅ Changed name to {new_name} successfully")
                else:
                    typer.echo("❌ No changes made.")
            else:
                typer.echo(f"✅ Repo '{current_name}' is already in kebab-case.")
    except Exception as e:
        typer.echo(f"❌ Error: {e}")

def change_repo_name(owner: str, current_name: str, new_name: str, token: str):
    url = f"https://api.github.com/repos/{owner}/{current_name}"
    headers = {"Authorization": f"token {token}"}
    data = {"name": new_name}
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code != 200:
        raise Exception(f"Failed to rename repo: {response.status_code}")

if __name__ == "__main__":
    app()
