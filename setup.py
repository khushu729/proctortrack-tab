import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="proctortrack-tab",
    version="0.1",
    install_requires=["setuptools"],
    requires=[],
    packages=["proctortrack_tab"],
    description='ProctorTrack XBlock',
    long_description=README,
    entry_points={
        "openedx.course_tab": [
            "proctortrack_tab = proctortrack_tab.tab:ProctorTrackTab"
        ]
    }
)