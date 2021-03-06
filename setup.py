from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mediapipe-test-csxstudios",
    version="0.0.1",
    author="csxstudios",
    author_email="csx@csxstudios.com",
    description="A small mediapipe test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/csxstudios/mediapipe-test",
    project_urls={
        "Bug Tracker": "https://github.com/csxstudios/mediapipe-test/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
)