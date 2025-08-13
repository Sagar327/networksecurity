'''
The setup.py file is used to build and distribute the package. It is a Python script that contains metadata about
the package, such as its name, version, and dependencies. Here is an example of a setup
.py file for a package called "my_package":

'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function returns a list of requirements.
    """
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt","r") as file:
            #Read lines from file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and  requirement!="-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Sagar",
    author_email="sagargahlyan738@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

