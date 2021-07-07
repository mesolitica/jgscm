from setuptools import setup

with open('requirements.txt') as fopen:
    req = list(filter(None, fopen.read().split('\n')))

setup(
    name="jgscm",
    description="Jupyter Google Cloud Storage ContentsManager",
    version="0.1.9",
    license="MIT",
    author="Husein Zolkepli",
    author_email="husein@mesolitica.com",
    url="https://github.com/mesolitica/jgscm",
    download_url="https://github.com/mesolitica/jgscm",
    packages=["jgscm"],
    keywords=["jupyter", "ipython", "gcloud", "gcs"],
    install_requires=req,
    package_data={"": ["requirements.txt", "LICENSE", "README.md"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries"
    ]
)
