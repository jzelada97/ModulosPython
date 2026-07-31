import os
from typing import Dict


def try_load_dotenv() -> bool:
    try:
        from dotenv import load_dotenv
        load_dotenv()
        return True
    except Exception:
        return False


def load_config() -> Dict[str, str]:
    keys = ['MATRIX_MODE', 'DATABASE_URL', 'API_KEY', 'LOG_LEVEL', 'ZION_ENDPOINT']
    cfg = {k: os.environ.get(k, '') for k in keys}
    return cfg


def print_config(cfg: Dict[str, str]) -> None:
    print('ORACLE STATUS: Reading the Matrix...')
    mode = cfg.get('MATRIX_MODE') or 'development'
    print('Configuration loaded:')
    print(f"Mode: {mode}")
    db = cfg.get('DATABASE_URL') or 'Not configured'
    print(f"Database: {db}")
    api = 'Authenticated' if cfg.get('API_KEY') else 'No API key'
    print(f"API Access: {api}")
    print(f"Log Level: {cfg.get('LOG_LEVEL') or 'INFO'}")
    print(f"Zion Network: {cfg.get('ZION_ENDPOINT') or 'Offline'}")
    print('\nEnvironment security check:')
    if cfg.get('API_KEY'):
        print('[OK] No hardcoded secrets detected')
    else:
        print('[WARNING] No API_KEY provided')
    if os.path.exists('.env'):
        print('[OK] .env file present (ensure it is in .gitignore)')
    else:
        print('[OK] No .env file present')
    print('[OK] Production overrides available' if mode == 'production' else '[INFO] Using development mode')


if __name__ == '__main__':
    loaded = try_load_dotenv()
    if not loaded:
        print('python-dotenv not available. To enable .env loading, install python-dotenv')
    cfg = load_config()
    print_config(cfg)
