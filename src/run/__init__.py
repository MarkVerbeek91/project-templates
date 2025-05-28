import shutil
from pathlib import Path
from copier import run_copy


WORKSPACE_DIR = Path(__file__).parent.parent.parent

WORKSPACE_TEMPLATE_DIR = WORKSPACE_DIR / Path("python-workspace-template")
PROJECT_TEMPLATE_DIR = WORKSPACE_DIR / Path("python-project-template")
TARGET_DIR = WORKSPACE_DIR / Path("target")

shutil.rmtree(TARGET_DIR, ignore_errors=True)


def create_workspace():
    """Create a workspace with sample packages."""

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
            },
        ],
    }

    # Create a project from a local path
    run_copy(str(WORKSPACE_TEMPLATE_DIR), str(TARGET_DIR), data=answers)

    workspace_name = str(answers["workspace_name"])
    TARGET_DIR = TARGET_DIR / workspace_name / "packages"

    for package in list(answers["packages"]):
        package_dir = TARGET_DIR / package["project_name"]

        WORKSPACE_TEMPLATE_DIR = WORKSPACE_DIR / Path("template_project")

        # Create a project from a local path
        run_copy(str(WORKSPACE_TEMPLATE_DIR), str(TARGET_DIR), data=package)


def create_project():
    """Create a project with sample packages."""
    pass

