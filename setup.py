from setuptools import setup, find_packages

setup(
    name='stlarray',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'numpy-stl',
        'astropy',
    ],
    include_package_data=True,
)
