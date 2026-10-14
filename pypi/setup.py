from setuptools import setup

setup(
    name="ironbedtruck-data",
    version="1.0.0",
    description="🚛 IronBedTruck — Premium truck parts catalog data for F-150, Silverado, RAM 1500 & Tundra. Free USA shipping over $99.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://ironbedtruck.com",
    author="IronBedTruck",
    author_email="support@ironbedtruck.com",
    license="MIT",
    packages=["ironbedtruck"],
    keywords=[
        "truck-parts","f-150","silverado","ram-1500","tundra","tacoma",
        "mud-flaps","running-boards","tonneau-cover","lift-kit","wheels",
        "led-light-bar","fender-flares","bed-liner","grille","bumper",
        "automotive","aftermarket-parts","pickup-truck","ironbedtruck"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
)
