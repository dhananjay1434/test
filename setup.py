from setuptools import setup, find_packages

setup(
    name='axiom-tools',
    version='1.0.0',
    packages=find_packages(),
    author='Team Axiom',
    description='A red-teaming toolkit for probing systemic LLM vulnerabilities.',
    install_requires=['openai>=1.0', 'numpy'],
)
