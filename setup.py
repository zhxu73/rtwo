import os
import setuptools
from rtwo.version import get_version, read_requirements

readme = open('README.md').read()
dependencies, requirements = read_requirements('requirements.txt')

#print dependencies
#print requirements
#dependencies = [
#'git+git://github.com/openstack/python-glanceclient.git#egg=python-glanceclient',
#'git+git://github.com/openstack/python-keystoneclient.git#egg=python-keystoneclient',
#'git+git://github.com/openstack/python-novaclient.git#egg=python-novaclient',
#'git+git://github.com/openstack/python-neutronclient.git#egg=python-neutronclient',
#'git+git://github.com/iPlantCollaborativeOpenSource/rfive.git#egg=rfive'
#'git+git://github.com/iPlantCollaborativeOpenSource/python-irodsclient.git',
#'git+git://github.com/jmatt/threepio.git',
#]
#requirements = [
#  'requests==2.2',
#  'paramiko==1.11',
#  'apache-libcloud',
#  'python-glanceclient',
#  'python-keystoneclient',
#  'python-novaclient',
#  'python-neutronclient',
#  'rfive==0.1.4',
#  'pycommands',
#  'threepio',
#]
long_description = """
rtwo %s
A unified interface into multiple cloud providers.

To install use pip install git+git://git@github.com:iPlantCollaborativeOpenSource/rtwo.git

----

%s

----

For more information, please see: https://github.com/iPlantCollaborativeOpenSource/rtwo
""" % (get_version('short'), readme)

setuptools.setup(
    name='rtwo',
    version=get_version('short'),
    author='jmatt',
    author_email='jmatt@jmatt.org',
    description="A unified interface into multiple cloud providers.",
    long_description=long_description,
    license="Apache License, Version 2.0",
    url="https://github.com/iPlantCollaborativeOpenSource/rtwo",
    packages=setuptools.find_packages(),
    dependency_links=dependencies,
    install_requires=requirements,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries",
        "Topic :: System",
        "Topic :: System :: Clustering",
        "Topic :: System :: Distributed Computing",
        "Topic :: System :: Systems Administration"
    ])
