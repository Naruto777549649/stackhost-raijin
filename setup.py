from setuptools import setup

requirements = ['requests', 'asyncio', 'aiohttp']
readme = ''
with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='KURO-HACKS',
    author='RyomenSukuna53',
    author_email='sufyan532011@gmail.com',
    version='0.0.1',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/Naruto777549649/stackhost-raijin',
    license='GNU General Public License v3.0',
    classifiers=[
        'Framework :: AsyncIO',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Build Tools',
    ],
    description='A shared hosting platform for students and developers offering affordable and free plans for testing and deploying projects.',
    include_package_data=True,
    keywords=['server', 'docker', 'kubernet', 'database', 'free', 'code', 'hosting', 'development'],
    install_requires=requirements,
)
