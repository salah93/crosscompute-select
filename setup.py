from os.path import abspath, dirname, join
from setuptools import find_packages, setup


ENTRY_POINTS = """
[crosscompute.types]
select = crosscompute_select:SelectType
"""
FOLDER = dirname(abspath(__file__))
DESCRIPTION = '\n\n'.join(open(join(FOLDER, x)).read().strip() for x in [
    'README.rst'])
setup(
    name='crosscompute-select',
    version='0.6.3',
    description='Select tag data type plugin for CrossCompute',
    long_description=DESCRIPTION,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'License :: OSI Approved :: MIT License',
    ],
    author='Salah Ahmed',
    author_email='salah93@crosscompute.com',
    keywords='web crosscompute',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    setup_requires=[
        'pytest-runner'
    ],
    install_requires=[
        'crosscompute>=0.6.3',
    ],
    entry_points=ENTRY_POINTS)
