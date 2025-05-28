import shutil
from pathlib import Path
from copier import run_copy

project_dir = Path(__file__).parent.parent.parent

template_dir = project_dir / Path("template_project")
destination = project_dir / Path("target")

shutil.rmtree(destination, ignore_errors=True)

answers = {
    "project_name": "pytask-common",
    "description": "tbd",
    "module_name": "pytask",
    "package_name": "pytask",
}

# Create a project from a local path
run_copy(str(template_dir), str(destination), data=answers)
