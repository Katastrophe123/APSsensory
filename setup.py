from setuptools import find_packages , setup
#from typing import List

def get_requirements()->list[str]:
    
    reuiremets_list = list[str] = []
    return reuiremets_list

setup(
    name = 'sensor',
    version = "0.0.1",
    author = "Kanishk",
    author_eamil = "kanishksinghparihar64@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements() ,#["pymongo"]
    
    
)