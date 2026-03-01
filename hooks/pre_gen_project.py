"""
Pre-generation hook to add derived variables to the context.
"""
import sys

# We can't easily modify the context object itself in Cookiecutter version 1.x
# but in 2.x it's possible.
# However, a simpler way is to just use the logic in the filenames
# or use the double underscore trick if supported.
