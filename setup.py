from setuptools import find_packages, setup

from liboocen import version


exclude_from_packages=('docs', 'scripts')


setup(
    name='liboocen',
    version='.'.join(map(str, version)),
    url='https://github.com/PurpleBlock/liboocen',
    author='The Developers of PurpleBlock',
    author_email='https://github.com/PurpleBlock/liboocen/issues',
    description='PurpleBlock',
    long_description=open('README.rst').read(),
    # download_url=
    license='MIT',
    # setup_requires=[],
    tests_require=('pytest', 'coverage', 'pytest-cov'),
    # install_requires=requires,
    packages=find_packages(exclude=exclude_from_packages),
    include_package_data=True,
    # ext_modules=extensions,
    scripts=[],
    # extras_require={},
    # zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)

