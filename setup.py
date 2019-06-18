import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bio_embeddings",
    version="0.0.1",
    author="Christian Dallago",
    author_email="christian.dallago@tum.de",
    description="A package to generate or retrieve NLP embeddings for bioinformatics applications",
    long_description=long_description,
    install_requires=["torch", "allennlp", "numpy", "gensim"],
    long_description_content_type="text/markdown",
    url="https://github.com/sacdallago/api.embed.protein.properties",
    packages=setuptools.find_packages(exclude=["notebooks", "webserver"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)