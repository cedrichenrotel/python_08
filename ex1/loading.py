#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  loading.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/01 15:14:09 by cehenrot        #+#    #+#               #
#  Updated: 2026/04/01 20:21:42 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

try:
    import random
    import importlib
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError as e:
    print(f"[ERROR] package not found: {e}")


def checking_dependencies() -> None:
    packages = [
        'pandas',
        'numpy',
        'matplotlib'
    ]

    for item in packages:
        module = importlib.import_module(item)
        version = module.__version__
        print(f"[OK] {item} {version}")

    np.random.randn(1000)


def main() -> None:
    print("LOADING STATUS: Loading programs...")

    checking_dependencies()
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")


if __name__ == "__main__":
    main()
