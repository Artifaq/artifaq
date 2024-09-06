import os
import typer
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

app = typer.Typer()

def create_project_structure(project_name: str):
    base_path = Path(project_name)
    base_path.mkdir(exist_ok=True)

    # Créer la structure du projet
    (base_path / "app").mkdir()
    (base_path / "app" / "api").mkdir()
    (base_path / "app" / "api" / "v1").mkdir()
    (base_path / "app" / "core").mkdir()
    (base_path / "app" / "models").mkdir()
    (base_path / "app" / "repositories").mkdir()
    (base_path / "app" / "services").mkdir()
    (base_path / "tests").mkdir()

def render_template(template_name: str, context: dict, output_path: Path):
    templates_dir = Path(__file__).parent / "templates"
    env = Environment(loader=FileSystemLoader(str(templates_dir)))
    template = env.get_template(template_name)
    content = template.render(context)

    with output_path.open("w") as f:
        f.write(content)

@app.command()
def init(project_name: str):
    """
    Initialise un nouveau projet basé sur my-fastapi-framework.
    """
    typer.echo(f"Initialisation du projet {project_name}...")

    create_project_structure(project_name)

    context = {
        "project_name": project_name,
    }

    # Render templates
    render_template("main.py.jinja", context, Path(project_name) / "main.py")
    render_template("pyproject.toml.jinja", context, Path(project_name) / "pyproject.toml")
    render_template("README.md.jinja", context, Path(project_name) / "README.md")

    typer.echo(f"Projet {project_name} initialisé avec succès!")
    typer.echo("Pour commencer, exécutez les commandes suivantes:")
    typer.echo(f"cd {project_name}")
    typer.echo("poetry install")
    typer.echo("poetry run uvicorn main:app --reload")

if __name__ == "__main__":
    app()

