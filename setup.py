from setuptools import setup, find_packages

setup(
    name='first_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
    ],
) 
