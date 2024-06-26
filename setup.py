from setuptools import setup
from typing import List

#Declaring variables for setup function
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Syam Sundar"
DESCRIPTION="This is a First FSDS Nov Batch Machine Learning Project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"
def get_requirements_list()->List[str]:
    """
    Description: This function going to return list of requirement mention in
    requirements.txt file
    return this function is goint to return a list which contain name of
    libraries mentioned in requirements..txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement _file:
        return requirement_file.readlines()
setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()

)
