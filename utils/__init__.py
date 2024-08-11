# __init__.py: This makes the utils directory a package which is much cleaner and more organized. It also allows you to import functions from the selenium_utils.py file directly as a package.

# The utils/__init__.py file serves several purposes in a Python project:
# 1. Package Initialization: It indicates that the utils directory should be treated as a Python package. This allows you to import modules from the utils directory using the package name.
# 2. Namespace Management: It helps in managing the namespace for the package. You can define what is exposed when the package is imported.
# 3. Package Configuration: You can include package-level variables, functions, or import statements that should be available when the package is imported.
# 4. Compatibility: It ensures compatibility with older versions of Python that require an __init__.py file to recognize a directory as a package.


from .selenium_utils import click_element, navigate_back

__all__ = ['click_element', 'navigate_back']
