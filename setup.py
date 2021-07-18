from setuptools import setup

setup(
    name='localsonly',
    version='0.0.1',
    packages=['localsonly'],
    install_requires = ["numpy", "scipy","qutip"],
    url='https://github.com/timevans/locals-only',
    license='',
    author='Tim Evans',
    author_email='tim@opacityquantum.com',
    description='A simple python library for building matrix product operator local Hamiltonians and finding their ground states using DMRG.'
)

