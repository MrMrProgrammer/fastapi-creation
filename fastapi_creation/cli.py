import typer
from pathlib import Path
from .layouts import LAYOUTS
from .utils import create_structure

app = typer.Typer(help="FastAPI Project Creation CLI")

@app.command()
def create(project_name: str = typer.Argument(..., help="Project name")):
    typer.echo("Select a template:")
    for i, name in enumerate(LAYOUTS.keys(), 1):
        typer.echo(f"{i}. {name}")
    choice = typer.prompt("Template number", default="1")
    try:
        structure_name = list(LAYOUTS.keys())[int(choice)-1]
    except (IndexError, ValueError):
        typer.echo("❌ Invalid choice")
        raise typer.Exit(code=1)

    project_path = Path.cwd() / project_name
    if project_path.exists():
        typer.echo(f"❌ Directory '{project_name}' already exists")
        raise typer.Exit(code=1)

    create_structure(project_path, LAYOUTS[structure_name])
    typer.echo(f"✅ Project '{project_name}' created with template '{structure_name}'")


def main():
    app()


if __name__ == "__main__":
    app()
