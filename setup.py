from setuptools import setup, find_packages

setup(
    name = "incuna-profiles",
    packages = find_packages(),
    include_package_data=True,
    version = "0.1",
    description = "Incuna specific user profiles extensions.",
    author = "Incuna Ltd",
    author_email = "admin@incuna.com",
    url = "http://incuna.com/",
    install_requires=[
        'django-orderable>=1.0.1'
    ],
    # download_url = "http://chardet.feedparser.org/download/python3-chardet-1.0.1.tgz",
    # long_description = """"""
)
