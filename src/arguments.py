# File: arguments.py
"""
This file contains functions to parse command line arguments
"""

import argparse 

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log-level', dest='log_level', default='WARNING',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help='Set the logging level (default: %(default)s)')
    parser.add_argument("--DEBUG", action="store_true", help="Run the program in debug mode")

    return parser.parse_args()