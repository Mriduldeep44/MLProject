from setuptools import find_packages, setup
from typing import List # becuase list was unrecoginisable


Hyphen='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if Hyphen in requirements:
            requirements.remove(Hyphen)
    return requirements        

setup(
    name='Ml Project',
    version='0.0.1',
    author='Mridul',
    author_email="eathan.mridul44@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
    
)
## it is basically meta data information about my project


'''
The setup.py file is used to define the metadata and configuration for your Python project.
It’s crucial when you want to distribute your project as a package, either to PyPI (Python Package Index)
or for others to install easily using a tool like pip
'''