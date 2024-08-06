from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
        Read requirements from a text file and return them as a list of strings.
    '''
    requirements =[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements=[req.replace('\n',' ') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='mlProject',
    version='0.0.1',
    author='Rahul',
    author_email='rahulrachhoya0@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirments.txt')
)