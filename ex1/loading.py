# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  loading.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/01 15:14:09 by cehenrot        #+#    #+#               #
#  Updated: 2026/04/03 09:56:13 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import importlib
except ImportError as e:
    print(f"[ERROR] package not found: {e}")
    sys.exit(1)


def checking_dependencies() -> None:
    packages = [
        'pandas',
        'requests',
        'matplotlib',
        'numpy'
    ]

    for item in packages:
        try:
            module = importlib.import_module(item)
            version = module.__version__
            print(f"[OK] {item} {version}")
        except ImportError as e:
            print(f"[ERROR] checking_independance: package -> {e} [KO]")


def generate_data() -> np.ndarray:
    data = np.random.randn(1000)
    return data


def analyze_data(data: np.ndarray) -> pd.DataFrame:
    if data is None or not isinstance(data, np.ndarray):
        print("invalid data")
        return None
    try:
        df = pd.DataFrame(data, columns=["matrix_signal"])
        return df
    except Exception as e:
        print(f"[ERROR] analyze_data: {e}")
    return None


def data_visualisation(df: pd.DataFrame) -> None:
    name_png = "matrix_matrix_analysis.png"
    try:
        plt.hist(df['matrix_signal'], bins=30)
        plt.savefig(name_png)
    except (KeyError, AttributeError) as e:
        print(f"[ERROR] data_visual: {e} [KO]")
        return
    print("\nAnalysis complete!")
    print(f"Results saved to: {name_png}")
    return


def main() -> None:
    print("LOADING STATUS: Loading programs...")

    print("\nChecking dependencies:")
    checking_dependencies()
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    data = generate_data()
    rst = analyze_data(data)

    print("Generating visualization...")
    data_visualisation(rst)


if __name__ == "__main__":
    main()
