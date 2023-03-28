from setuptools import setup




def get_requirements_list:->
    with open('requirements.txt')as requirement


PROJECT_NAME="housing",
VERSION="0.0.2",
AUTHOR="sandhya",
DESCRIPTION="this is housing price prediction",
PACKAGES=find_packages()





setup(

name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()




)