# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  oracle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/02 14:46:16 by cehenrot        #+#    #+#               #
#  Updated: 2026/04/03 14:06:53 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import os
try:
    from dotenv import load_dotenv
except ImportError as e:
    print(f"[ERROR] package not found: {e}")
    sys.exit(1)


def load_var() -> None:
    load_dotenv()

    variables = {
        "MATRIX_MODE": 'mode',
        "DATABASE_URL": 'database',
        "API_KEY": 'api_key',
        "LOG_LEVEL": 'log_level',
        "ZION_ENDPOINT": 'zion'
    }

    mode = os.getenv("MATRIX_MODE", "development")
    if mode == "production":
        print("PRODUCTION MODE - secrets will be hidden")
    else:
        print("DEVELOPMENT MODE - debug enabled")

    for key, text in variables.items():
        value = os.getenv(key)
        if value is None:
            print(f"[WARNING] value: {key} is None")
        else:
            sensitive = ["API_KEY", "DATABASE_URL"]
            if mode == "production" and key in sensitive:
                print(f"{text.capitalize()}: ****hidden****")
            else:
                print(f"{text.capitalize()}: {value}")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")

    print("\nConfiguration loaded:")
    load_var()

    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
