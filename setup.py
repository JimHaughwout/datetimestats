from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='datetimestats',
    author='Jim Haughwout',
    author_email='haughwout@alum.mit.edu',
    description='Useful math stats functions for collections of datetime objects',
    url='https://github.com/JimHaughwout/datetimestats',
    download_url = 'https://github.com/JimHaughwout/datetimestats/tarball/1.0.0', 
    version='1.0.0',
    keywords='datetime statistics mean median',
    packages=['datetimestats', ],
    package_dir={'datetimestats':'datetimestats'},
    install_requires=['pytz'],
    license='Apache Software License',
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)