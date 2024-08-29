import os
import shutil
import subprocess
import logging
from sys import stderr
from hatchling.builders.hooks.plugin.interface import BuildHookInterface

# Set up logging for better debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        super().initialize(version, build_data)
        logging.info("Starting build process for Open Webui frontend")

        # Check for npm presence
        npm = shutil.which("npm")
        if npm is None:
            logging.error("NodeJS `npm` is required for building Open Webui but it was not found")
            raise RuntimeError("NodeJS `npm` is required for building Open Webui but it was not found")

        logging.info("Running `npm install`")
        try:
            subprocess.run([npm, "install"], check=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"`npm install` failed with error: {e}")
            raise

        logging.info("Running `npm run build`")
        os.environ["APP_BUILD_HASH"] = version
        try:
            subprocess.run([npm, "run", "build"], check=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"`npm run build` failed with error: {e}")
            raise

        logging.info("Build process completed successfully")

        # AI-driven enhancement: Dynamic configuration based on build data
        self.apply_dynamic_configuration(build_data)

    def apply_dynamic_configuration(self, build_data):
        # Example AI-driven enhancement: Adjust configuration based on build data
        # This is a placeholder for actual AI logic which could use machine learning models
        logging.info("Applying dynamic configuration based on build data")
        # Example placeholder code:
        if build_data.get("optimize"):
            logging.info("Applying optimization configuration")
            # Apply optimization settings
            # e.g., subprocess.run(["npm", "run", "optimize"], check=True)
