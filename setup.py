# This will automatically find out all the packages that are available in the directory we have created
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Warisha',
    author_email='warishafatima2810@gmail.com',
    packages=find_packages(),  
    # find_packages() will check all folders if we have __initi__.py then consider those as package and builds it
    install_requires=get_requirements('requirements.txt')
)