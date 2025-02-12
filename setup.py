from setuptools import setup, find_packages

setup(
    name='gh-robot-demo',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'RobotFramework==4.0.3',
        'requests==2.26.0',
        'robotframework-seleniumlibrary==6.0.0',
        'robotframework-requests==0.9.1',
        'pymysql==1.0.2',
        'jsonschema==4.4.0'
    ],
    entry_points={
        'console_scripts': [
            'run-tests=run_tests:main',
        ],
    },
)