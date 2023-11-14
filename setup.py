from setuptools import setup, find_packages

package_name = "repo_prova"

setup(
    name=package_name,
    version='0.0.1',
    packages=['repo_prova'], #find_packages(),
    package_data={'': ['*.csv']},
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of the project.',
    long_description=open('README.md').read(),
    install_requires=[
        "langchain",
        "openai"
        ],  # List your project dependencies here
    url='https://github.com/yingji/repo_prova',
    python_requires='>=3.6.0',
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)