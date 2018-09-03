from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='nnir',
    version='0.0.1',
    description='Python package to train neural networks to classify data',
    long_description=long_description,
    author='PlanetGazer8360',
    author_email='ml.learner.8359@gmail.com',
    long_description_content_type="text/markdown",
    url="https://github.com/Nesac128/NNIR",
    install_requires=['tensorflow==1.9.0', 'Pillow==5.1.0',
                      'scikit-learn==0.19.1', 'numpy==1.14.5',
                      'opencv-python==3.4.0.12', 'pandas==0.22.0',
                      'click==6.7', 'pydub==0.22.0', 'sox==1.3.3',
                      'scipy', 'png'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)
