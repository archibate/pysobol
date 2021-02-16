import setuptools
import pysobol

setuptools.setup(
    name='pysobol',
    version='0.0.1',
    author='archibate',
    author_email='1931127624@qq.com',
    url='https://github.com/archibate/pysobol',
    description='Efficient Sobol sequence generator with NumPy',
    long_description=pysobol.__doc__,
    license='MIT',
    keywords=['graphics', 'renderer'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Games/Entertainment :: Simulation',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
    ],
    packages=setuptools.find_packages(),
)
