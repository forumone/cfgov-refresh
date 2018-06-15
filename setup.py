import os
from setuptools import find_packages, setup


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


with open('README.md') as f:
    long_description = f.read()

install_requires = [
    'Django>=1.8,<1.9',
    'wagtail>=1.13,<1.14',
]

testing_extras = [
    'mock>=2.0.0',
    'coverage>=3.7.0',
]

setup(
    name='cfgov',
    url='https://github.com/cfpb/wagtail-treemodeladmin',
    author='CFPB',
    author_email='tech@cfpb.gov',
    description=' Django project protecting American consumers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='CC0',
    version_format='{tag}.dev{commitcount}+{gitsha}',
    packages=['cfgov/v1'],
    include_package_data=True,
    package_data={
    },
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
    },
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Wagtail :: 1',
        'Framework :: Wagtail :: 2',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'License :: Public Domain',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    setup_requires=[
        'cfgov_setup==1.2',
        'setuptools-git-version==1.0.3',
    ],
    frontend_build_script='frontend.sh',
)
