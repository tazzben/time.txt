try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

long_desc = """
	Time.txt allows you to track and analyze your time (sheets) using plain text files. With this tool you can see what your spending your time on, search based on categories, projects, number of hours, dates or some combination of the aforementioned list. The format of the time file is completely freeform and consistent with the GTD style of todos.
"""


setup(name="time.txt",
      version=1.0,
      description="Time.txt allows you to track and analyze your time (sheets) using plain text files.",
      author="Ben Smith",
      author_email="ben@wbpsystems.com",
      url="https://github.com/tazzben/time.txt",
      license="MIT",
      packages=[],
      scripts=['ttime'],
      package_dir={},
      long_description=long_desc,
      classifiers=[
          'Topic :: Text Processing',
          'Environment :: Console',
          'Development Status :: 5 - Production/Stable',
          'Operating System :: POSIX',
          'Intended Audience :: Developers',
          'Intended Audience :: End Users/Desktop'
      ]
     )