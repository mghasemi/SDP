from distutils.core import setup

setup(
    name='SDP',
    version='1.0.0',
    author='Mehdi Ghasemi',
    author_email='mghasemi@ntu.edu.sg',
    packages=['SDP'],
    #scripts=[''],
    url='',
    license='LICENSE.txt',
    description='A generic python wraper for SDP solvers.',
    long_description=open('README.txt').read(),
    #install_requires=[
    #    "cvxopt",
    #    "pysdp",
    #],
)
