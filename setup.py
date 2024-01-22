from setuptools import find_packages, setup
from typing import List

hyphen_e = "-e ."  #written to automatically run the setup file

def get_requirements(file_path:str)->List[str]:
    
    reqs = []
    with open(file_path) as f:
        reqs = f.readlines()
        reqs = [r.replace("\n", "")  for r in reqs]

        if hyphen_e in reqs:
            reqs.remove(hyphen_e)

    return reqs

setup(
    name= 'ml_project',
    version = '0.0.1',
    author= 'sandeep mutkule',
    author_email ='sandeepmutkule7@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)