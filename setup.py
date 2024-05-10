from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()


def get_requirements(fname):
    """Takes requirements from requirements.txt and returns a list."""
    with open(fname) as fp:
        reqs = list()
        for lib in fp.read().split("\n"):
            # Ignore pypi flags and comments
            if not lib.startswith("-") or lib.startswith("#"):
                reqs.append(lib.strip())
        return reqs


install_requires = get_requirements("requirements.txt")

setup(
    name='tgstat-api-client',
    version='0.1.0',
    description='Python client for TgStat API',
    long_description=long_description,
    url='https://github.com/bodaue/tgstat-api-client',
    author='Bodaue',
    author_email='tim-online@mail.ru',
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    python_requires='>=3.10',
)
