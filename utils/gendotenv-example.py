"""
Esse é script para criar um arquivo de configuração de sua aplicação local.

O arquivo pode ser renomeado porém é recomendável que o mesmo esteja declarado no arquivo 
.gitignore, para que suas configurações locais, como endereço de banco, estejam expostas no github
"""

import random
import os
from pathlib import Path, PurePosixPath, PureWindowsPath
from string import ascii_letters, digits


# Base path
BASE = Path(__file__).resolve().parent.parent


def seckey_gen():
    chars = "!?@#$%^&*()" + ascii_letters + digits
    size = 57
    secret_key = "".join(random.sample(chars, size))
    return secret_key


def get_database_info():
    secret_key = seckey_gen()

    dbname = input('dbname: ').strip()
    dbuser = input('dbuser: ').strip()
    dbpassword = input('dbpassword: ').strip()
    dbhost = input('dbhost: ').strip()

    CONFIGS = f"""
    SECRET_KEY = '{secret_key}'
    DEBUG = 'True'
    ALLOWED_HOSTS = '127.0.0.1'

    DBNAME = f'{dbname}'
    DBUSER = f'{dbuser}'
    DBPASSWORD = f'{dbpassword}'
    DBHOST = f'{dbhost}'
    """

    return CONFIGS


def create_dotenv():
    configs = get_database_info()

    if os.name == 'nt':
    # To Windows
        BACKEND = PureWindowsPath(BASE).joinpath('backend')
        SETTINGS = PureWindowsPath(BACKEND).joinpath('settings')

        with open(f'{SETTINGS}\.env', 'w') as settings_file:
            settings_file.write(configs)
    else:
        # To Linux
        BACKEND = PurePosixPath(BASE).joinpath('backend')
        SETTINGS = PurePosixPath(BACKEND).joinpath('settings')
        
        with open(f'{SETTINGS}/.env', 'w') as settings_file:
            settings_file.write(configs)


if __name__ == '__main__':
    create_dotenv()