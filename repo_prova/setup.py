from setuptools import setup, find_packages

setup(
    name='repo_prova',
    version='0.1',
    packages=find_packages(),
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of the project.',
    long_description=open('README.md').read(),
    install_requires=[],  # List your project dependencies here
    url='http://example.com/your/project',
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)