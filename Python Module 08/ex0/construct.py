import sys
import os
from typing import Optional


def in_virtualenv() -> bool:
    # Preferred checks for virtual environment
    if hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix:
        return True
    if hasattr(sys, 'real_prefix'):
        return True
    if 'VIRTUAL_ENV' in os.environ:
        return True
    return False


def find_site_packages() -> Optional[str]:
    # Try to locate the active site-packages for current interpreter
    for p in sys.path:
        if 'site-packages' in p:
            return p
    return None


def main() -> None:
    print('MATRIX STATUS:')
    if in_virtualenv():
        print("You're in the construct")
        print(f"Current Python: {sys.executable}")
        venv = os.environ.get('VIRTUAL_ENV') or os.path.dirname(sys.executable)
        print(f"Virtual Environment: {os.path.basename(venv)}")
        print(f"Environment Path: {venv}")
        print('SUCCESS: You\'re in an isolated environment!')
        sp = find_site_packages()
        if sp:
            print('Package installation path:')
            print(sp)
        else:
            print('Package installation path: Not found via sys.path')
    else:
        print("You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print('Virtual Environment: None detected')
        print("WARNING: You're in the global environment!")
        print('The machines can see everything you install.')
        print('To enter the construct, run:')
        print('python -m venv matrix_env')
        print('source matrix_env/bin/activate # On Unix')
        print('matrix_env\\Scripts\\activate # On Windows')
        print('Then run this program again.')


if __name__ == '__main__':
    main()
