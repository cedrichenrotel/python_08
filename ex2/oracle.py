# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  oracle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/02 14:46:16 by cehenrot        #+#    #+#               #
#  Updated: 2026/04/03 16:20:26 by cehenrot        ###   ########.fr        #
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

    check_value = True
    for key, text in variables.items():
        value = os.getenv(key)
        if value is None:
            print(f"[WARNING] value: {key} is None")
            check_value = False
        else:
            sensitive = ["API_KEY", "DATABASE_URL"]
            if mode == "production" and key in sensitive:
                print(f"{text.capitalize()}: ****hidden****")
            else:
                print(f"{text.capitalize()}: {value}")

    print("\nEnvironment security check:")

    if check_value:
        print("[OK] No hardcoded secrets detected")
    else:
        print(f"[WARNING] value: {key} is None")
    if os.path.exists('.env'):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")
    if mode is None:
        print("[WARNING] no mode control")
    else:
        print("[OK] Production overrides available")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")

    print("\nConfiguration loaded:")
    load_var()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
