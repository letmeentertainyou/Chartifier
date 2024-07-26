from setuptools import Extension
from setuptools import setup

module = Extension("rhythm_utils", sources=["packed_char_array/array.c", "rhythm_utils.c", "rhythm_utils_module.c"], extra_compile_args=["-Wall"])

setup(
    name="rhythm_utils",
    version="1.0.0",
    description="An example Python C extension module",
    url="https://github.com/letmeentertainyou/Chartifier",
    author="Lars S",
    author_email="",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    ext_modules=[module],
    py_modules=["rhythm"],
)
