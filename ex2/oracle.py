# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  oracle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/02 14:46:16 by cehenrot        #+#    #+#               #
#  Updated: 2026/04/02 16:44:10 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from dotenv import load_dotenv
import os


def load_var() -> None:
    load_dotenv()
    variables = {
        "MATRIX_MODE": 'mode',
        "DATABASE_URL": 'database',
        "API_KEY": 'api_key',
        "LOG_LEVEL": 'log_level',
        "ZION_ENDPOINT": 'zion'
    }
    for key, text in variables.items():
        value = os.getenv(key)
        print(f"{text.capitalize()}: {value}")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")

    print("\nConfiguration loaded:")
    load_var()


if __name__ == "__main__":
    main()
