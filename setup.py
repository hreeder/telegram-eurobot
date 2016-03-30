from distutils.core import setup
from pip.req import parse_requirements

install_reqs = parse_requirements("requirements.txt", session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='telegram-eurobot',
    version='0.1.0',
    packages=['eurobot', 'eurobot.commands'],
    url='https://github.com/hreeder/telegram-eurobot/',
    license='MIT',
    author='Harry Reeder',
    author_email='harry@harryreeder.co.uk',
    description='',
    install_requires=reqs,
    entry_points={
        'console_scripts': [
            'eurobot = eurobot.bot:main'
        ]
    }
)
