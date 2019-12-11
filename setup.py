import setuptools

setuptools.setup(
    name='vajra-microservice',
    version='0.0.1',

    author="Setient, Ltd.",
    author_email="info@setient.io",

    description='Docker image tests',

    url="https://github.com/setientltd/vajra-microservice",

    dependency_links=open("requirements.txt").read().split("\n"),

    packages=['test'],

    include_package_data=True,

    python_requires='>=2.7',
    setup_requires=['setuptools-git'],

)
