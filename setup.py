from setuptools import setup, find_packages

setup(
name="gpu-sidechannel-experiment",
version="0.1.0",
description="Safe experiment harness to measure CPU timer jitter under GPU load.",
author="Alex Goldstein",
packages=find_packages(where="src"),
package_dir={"": "src"},
install_requires=[
"numpy",
"pandas",
"matplotlib",
],
entry_points={
"console_scripts": [
"run-gpuexp = gpuexp.run_experiment:main",
],
},
include_package_data=True,
)