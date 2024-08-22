from setuptools import find_packages, setup

setup(
    name="CarSalesPrediction",  # Replace with your project name
    version="0.1.0",
    description="A machine learning project to predict car sales.",
    author="Ailneni Santhosh",  # Replace with your name
    author_email="santhoshainleni@gmail.com",  # Replace with your email
    url="https://github.com/yourusername/CarSalesPrediction",  # Replace with your project's GitHub URL
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
        "scikit-learn>=0.22.0",
        "matplotlib>=3.1.0",
        "seaborn>=0.10.0",
        "flask>=1.1.0",
        "gunicorn>=20.0.0",  # If using Gunicorn for deployment
        "PyYAML>=5.3.0",  # For YAML config files
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'run_model=src.model:main',  # Example command-line tool
        ],
    },
)
