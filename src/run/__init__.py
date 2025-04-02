import shutil
from pathlib import Path
from copier import run_copy

workspace_dir = Path(__file__).parent.parent.parent

template_dir = workspace_dir / Path("template_workspace")
destination = workspace_dir / Path("target")

shutil.rmtree(destination, ignore_errors=True)

answers = {
    "workspace_name": "Sample-Workspace",
    "module_name": "sample_module_main",
    "packages": [
        {
            "project_name": "Sample01",
            "description": "Sample package description",
            "module_name": "sample_module_01",
            "package_name": "sample_package_01",
        },
        {
            "project_name": "Sample02",
            "description": "Sample package description",
            "module_name": "sample_module_02",
            "package_name": "sample_package_02",
        }
    ],
}

# Create a project from a local path
run_copy(str(template_dir), str(destination), data=answers)

destination = destination / answers["workspace_name"] / "packages"

for package in answers["packages"]:
    package_dir = destination / package["project_name"]

    template_dir = workspace_dir / Path("template_project")

    # Create a project from a local path
    run_copy(str(template_dir), str(destination), data=package)
