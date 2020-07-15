import os
from setuptools import setup

REQUIRES = [
"botbuilder-core>=4.5.0b5",
"botbuilder-schema>=4.5.0b5",
"recognizers_text_suite>=1.0.2a2",
"aiounittest>=1.3.0"
]

TESTS_REQUIRES = ["aiounittest>=1.3.0"]

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, "botbuilder", "community", "middleware", "text","recognizer", "about.py")) as f:
    package_info = {}
    info = f.read()
    exec(info, package_info)

with open(os.path.join(root, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=package_info["__title__"],
    version=package_info["__version__"],
    url=package_info["__uri__"],
    author=package_info["__author__"],
    description=package_info["__description__"],
    keywords="botbuilder bots ai botframework middleware text recognizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=package_info["__license__"],
    packages=[
        "botbuilder.community.middleware.text.recognizer",
    ],
    install_requires=REQUIRES + TESTS_REQUIRES,
    tests_require=TESTS_REQUIRES,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)