from setuptools import setup, find_packages

setup(
    name='progeny_scores',
    version='1.0.0',
    author='AR',
    author_email='ar@example.com',
    packages=find_packages(),
    install_requires=[
        'resdk>=21.0.0',  
        'decoupler>=1.5.0',
        'omnipath>=1.0.8',
        'tabulate >= 0.9.0',
    ],
    entry_points={
        'console_scripts': [
            'progeny-scores=progeny_scores.cli:main',
        ],
    },
)