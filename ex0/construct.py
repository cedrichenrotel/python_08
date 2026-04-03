#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  construct.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/01 08:57:20 by cehenrot        #+#    #+#               #
#  Updated: 2026/04/03 11:53:51 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import os
import site


def check_execution_env() -> bool:
    return sys.prefix != sys.base_prefix


def current_status() -> None:
    name_venv = os.path.basename(sys.prefix)
    virtual_env_pack = site.getsitepackages()
    absolute_path = sys.executable

    if check_execution_env():
        print(f"Current Python: {absolute_path}")
        print(f"Virtual Environment: {name_venv}")
        print(f"Environment Path: {sys.prefix}")

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting "
              "the global system.")

        print("Package installation path")
        print(virtual_env_pack[0])
    else:
        print(f"Current Python: {absolute_path}")
        print("Virtual Environment: None detected")

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:"
              "\npython -m venv matrix_env"
              "\nsource matrix_env/bin/activate # On Unix"
              "\nmatrix_env\\Scripts\\activate # On Windows")

        print("\nThen run this program again.")


def is_venv() -> None:
    print("MATRIX STATUS: Welcome to the construct")
    print()
    current_status()


def not_is_venv() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print()
    current_status()


def main() -> None:
    if check_execution_env():
        is_venv()
    else:
        not_is_venv()


if __name__ == "__main__":
    main()
