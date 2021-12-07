from setuptools import find_packages, setup

readme = open('README.md', 'r').read()

setup(
    name="fastapi_misskey",
    packages=find_packages(),
    version="0.0.1",
    description="Misskey authentication to FastAPI",
    long_description=readme,
    long_description_content_type="text/markdown",
    author='yupix',
    license='MIT',
    install_requires=['fastapi==0.70.0', 'uvicorn==0.15.0', 'aiohttp==3.8.1', 'aiocache==0.11.1'],
    python_requires='>=3.5',
    url='https://github.com/yupix/fastapi-misskey'
)
