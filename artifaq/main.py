import click
import os
import shutil
import sys
import git

@click.command()
@click.option(
    '--template',
    '-t',
    default="https://github.com/artifaq/template.git",
    prompt='Enter template GitHub URL to deploy',
    help='GitHub repository URL for the template to clone'
)
@click.option(
    '--project-name',
    '-p',
    prompt='Enter project name (directory name)',
    help='Name of the directory where the repository will be cloned'
)
def init(template, project_name):
    print(f'Initializing Artifaq...')
    print(f'Deploying template from {template}...')

    try:
        if os.path.exists(project_name):
            print(f"Error: Directory '{project_name}' already exists. Please choose a different project name.")
            sys.exit(1)

        git.Repo.clone_from(template, project_name)
        print(f'Template {template} cloned successfully into {project_name}!')

        git_dir = os.path.join(project_name, '.git')
        if os.path.exists(git_dir):
            shutil.rmtree(git_dir)
            print(f"Removed .git directory from {project_name}.")

        print(f'Artifaq initialized successfully!')

    except git.exc.GitError as e:
        print(f"Failed to clone the repository. Error: {e}")
        sys.exit(1)
    except OSError as e:
        print(f"Failed to remove .git directory. Error: {e}")
        sys.exit(1)


@click.group()
def main():
    pass

main.add_command(init)

if __name__ == '__main__':
    main()