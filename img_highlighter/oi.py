#!/usr/bin/env python3

# https://github.com/KillianLucas/open-interpreter/

import interpreter
import os


def read_context_files(start_dir):
    start_dir = os.path.abspath(start_dir)

    # Initialize the result
    result = ''

    # Start from the given directory
    current_dir = start_dir

    while True:
        # Try to open the context.txt file in the current directory
        try:
            with open(os.path.join(current_dir, 'context.txt'), 'r') as file:
                # Prepend the file content to the result
                result = file.read() + '\n' + result
        except FileNotFoundError:
            pass

            # If the current directory is either the root or 'oi', stop
        if current_dir == '/' or os.path.basename(current_dir) == 'oi':
            break

            # Go up to the parent directory
        current_dir = os.path.dirname(current_dir)

    return result


# Test the function with the current directory
print(interpreter.system_message + '\n' + read_context_files('./'))

# interpreter.chat("Plot AAPL and META's normalized stock prices")
# Executes a single command
interpreter.auto_run = True
interpreter.chat()  # Starts an interactive chat
#
# interpreter.system_message += """
# Run shell commands with -y so the user doesn't have to confirm them.
# """
# print(interpreter.system_message)
