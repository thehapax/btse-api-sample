from setuptools import setup
from Cython.Build import cythonize

def main():

    cython_kwargs = {
        "language": "c++",
        "language_level": 3,
    }

    setup(
        # ext_modules = cythonize("helloworld.pyx")
        ext_modules=cythonize(["*.pyx"], **cython_kwargs),
    )

if __name__ == "__main__":
    main()
