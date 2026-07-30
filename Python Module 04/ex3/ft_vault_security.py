from typing import Tuple, Optional


def secure_archive(filename: str, mode: str = 'r', content: Optional[str] = None) -> Tuple[bool, str]:
    try:
        if mode and mode.startswith('r'):
            with open(filename, 'r', encoding='utf-8') as f:
                data = f.read()
            return True, data
        else:
            # write mode
            with open(filename, 'w', encoding='utf-8') as f:
                if content is None:
                    content = ''
                f.write(content)
            return True, 'Content successfully written to file'
    except Exception as e:
        return False, str(e)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file'))
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('/etc/master.passwd'))
    print("Using 'secure_archive' to read from a regular file:")
    # Attempt to read a local file if available; adjust path as needed when running tests
    ok, content = secure_archive('ancient_fragment.txt')
    print((ok, content))
    print("Using 'secure_archive' to write previous content to a new file:")
    success, msg = secure_archive('preserved_fragment.txt', mode='w', content=content if ok else 'Sample content')
    print((success, msg))
