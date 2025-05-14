from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="mathhelper",
    version="0.0.1",
    author="José Roberto",
    author_email="jrobertovl@gmail.com",
    description="Um pacote auxiliar de matemática simples com operações básicas e avançadas",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jrobertovl/mathhelper",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
