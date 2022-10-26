from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="pacote_teste",
    version="0.0.1",
    author="adriano",
    author_email="webmail.adriano@gmail.com",
    description="Pacote de Teste",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyberwork/dio-geracao-tech-unimed-bh-criando-pacote-python"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)