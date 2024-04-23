from setuptools import setup

setup(
   name='mtracker',
   version='1.0',
   description='Provides a decorator for memory usage tracking. The part of FOSS course.',
   license='MIT',
   author='Darya Nikiforova',
   author_email='darya.n.2004@mail.com',
   url='https://github.com/Darya778/setup_test',
   packages=['mtracker'], 
   install_requires=['numpy==1.26.4', 'setuptools==59.6.0'],
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)
