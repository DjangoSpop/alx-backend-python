import os
import re

def add_docstrings(directory):
    """
    Recursively adds docstrings to all Python files in the given directory.

    Args:
        directory (str): The path to the directory containing the Python files.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                add_docstring_to_file(file_path)

def add_docstring_to_file(file_path):
    """
    Adds a basic docstring to the given Python file.

    Args:
        file_path (str): The path to the Python file.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Check if the file already has a docstring
    if lines and re.match(r'\s*"""', lines[0]):
        return

    # Add a module docstring
    module_docstring = '"""Module docstring goes here."""\n'
    lines.insert(0, module_docstring)

    # Add function docstrings
    for i, line in enumerate(lines):
        if re.match(r'\s*def\s+\w+\(', line):
            function_docstring = '\n    """\n    Function docstring goes here.\n    """\n'
            lines.insert(i + 1, function_docstring)

    with open(file_path, 'w') as file:
        file.writelines(lines)

    print(f'Added docstrings to {file_path}')

# Example usage
