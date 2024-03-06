from setuptools import setup

setup(
    name='simple_site',
    version='0.01',
    py_modules=['simple_site'],
    entry_points={
        'console_scripts': [
            'simple_site = simple_site:main'
        ]
    },
    package_data={
        'simple_site': ['templates/template_backend.service']
    },
    install_requires=[
        'setuptools'
    ]
)
