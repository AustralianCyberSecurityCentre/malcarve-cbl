"""Build the c-dependencies for malcarve to function."""

# hatch_build.py
import os
import subprocess

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    """Build the c-dependencies for malcarve to function."""

    def initialize(self, version, build_data):
        """Build the c-dependencies for malcarve to function."""
        ext_dir: str = os.path.join(os.path.dirname(__file__), "malcarve_cbl/ext")
        build_script_path: str = os.path.join(ext_dir, "build.sh")
        subprocess.run(build_script_path, check=True)  # noqa: S603
