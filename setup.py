from setuptools import setup

requirements = ['requests', "asyncio"]
readme = ''
with open("README.md", encoding="utf-8") as f:
    readme = f.read()
setup(
    name='stackhost',
    author='iShiKki',
    author_email='ishikkiakabane@gmail.com',
    version='0.0.1',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/ishikki-akabane/stackhost',
    license='GNU General Public License v3.0',
    classifiers=[
        "Framework :: AsyncIO",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        "Natural Language :: English",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Build Tools",

    ],
    description='',
    include_package_data=True,
    keywords=['server', 'hosting', 'docker', 'kubernet', 'database', 'free', 'code'],
    install_requires=requirements
)
