# Source Code

Source code for the mac_changer.

### Programming Language: Python 3.8

### Libraries Used:
- **subprocess:** The *subprocess* module allows you to spawn new processes, connect to their
input/output/error pipes, and obtain their return codes. Used to interact with command line
arguments.
- **argparse:** The *argparse* module makes it easy to write user-friendly command-line interfaces. The
program defines what arguments it requires, and argparse will figure out how to parse those out of
sys.argv.
- **re:** The *re (Regular Expression or regex)* module is used to search within a string using a sequence
of characters that define a search pattern. It is used here to get MAC Address.
- **random:** The *random* module implements pseudo-random number generators for various
distributions. Used for Random MAC Generation Algorithm.
- **sys:** The *sys* module provides access to some variables used or maintained by the interpreter and
to functions that interact strongly with the interpreter.
- **termcolor:** The *termcolor* module is used for ANSII color formatting for
output in terminal.
