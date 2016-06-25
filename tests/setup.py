from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='datetimestats',
    author='Jim Haughwout',
    author_email='haughwout@alum.mit.edu',
    description='Useful math stats functions for collections of datetime objects',
    url='https://github.com/JimHaughwout/theword',
    download_url = 'https://github.com/JimHaughwout/datetimestats/tarball/1.0.0', 
    version='1.0.0',
    packages=['datetimestats', ],
    package_dir={'datetimestats':'datetimestats'},
    license='MIT',
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment'
    ],
)