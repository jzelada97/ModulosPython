import sys
import subprocess
from pathlib import Path

ROOT = Path('.')
modules = [f'Python Module {i:02d}' for i in range(0, 11)]

results = []

for m in modules:
    mod_path = ROOT / m
    if not mod_path.exists():
        continue
    for ex in sorted(mod_path.glob('ex*')):
        if not ex.is_dir():
            continue
        for py in sorted(ex.glob('*.py')):
            if py.name == '__init__.py':
                continue
            cmd = [sys.executable, str(py)]
            header = f'--- Running {m}/{ex.name}/{py.name} ---'
            print(header)
            try:
                # Run the script with working directory set to the module folder
                import os
                env = os.environ.copy()
                env['PYTHONPATH'] = str(mod_path)
                # Use script path relative to module folder to avoid duplicated path parts
                rel_script = os.path.join(ex.name, py.name)
                proc = subprocess.run([sys.executable, rel_script], capture_output=True, text=True, timeout=20, cwd=str(mod_path), env=env)
                out = proc.stdout
                err = proc.stderr
                print(out, end='')
                if err:
                    print('STDERR:')
                    print(err)
                results.append((str(py), proc.returncode, out, err))
            except subprocess.TimeoutExpired:
                print('Timed out')
                results.append((str(py), -1, '', 'Timed out'))
            except Exception as e:
                print('Error running script:', e)
                results.append((str(py), -1, '', str(e)))

print('\nSummary:')
for path, code, _, err in results:
    status = 'OK' if code == 0 else f'FAIL ({code})'
    print(f'{path}: {status}')

# Exit with non-zero if any failure
if any(code != 0 for _, code, _, _ in results):
    sys.exit(1)
else:
    sys.exit(0)
