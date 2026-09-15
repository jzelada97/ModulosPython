import importlib
import importlib.metadata
import sys


REQS = ['numpy', 'pandas', 'matplotlib', 'requests']


def check_dependencies() -> dict[str, bool]:
    statuses = {}
    for pkg in REQS:
        try:
            importlib.import_module(pkg)
            statuses[pkg] = True
        except Exception:
            statuses[pkg] = False
    return statuses


def print_dependency_report(statuses: dict[str, bool]) -> None:
    print('LOADING STATUS: Loading programs...')
    print('Checking dependencies:')
    for pkg, ok in statuses.items():
        if ok:
            try:
                mod = importlib.import_module(pkg)
                ver = getattr(mod, '__version__', 'unknown')
            except Exception:
                ver = 'unknown'
            print(f"[OK] {pkg} ({ver}) - ready")
        else:
            print(f"[MISSING] {pkg} - install with pip or Poetry")


def install_instructions() -> None:
    print('\nInstall with pip:')
    print('pip install -r ex1/requirements.txt')
    print('\nInstall with Poetry:')
    print('poetry install')


def run_analysis() -> None:
    try:
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
    except Exception as e:
        print('Cannot run analysis, missing libraries:', e)
        return
    print('Analyzing Matrix data...')
    data = np.random.normal(loc=0.0, scale=1.0, size=1000)
    print('Processing 1000 data points...')
    df = pd.DataFrame({'value': data})
    df['cumsum'] = df['value'].cumsum()
    print('Generating visualization...')
    plt.figure(figsize=(6, 4))
    plt.plot(df['cumsum'])
    plt.title('Matrix Signal Cumulative')
    plt.xlabel('Index')
    plt.ylabel('Cumulative Signal')
    out = 'matrix_analysis.png'
    plt.savefig(out)
    plt.close()
    print('Analysis complete!')
    print('Results saved to:', out)


def show_versions() -> None:
    # Comparison function: reports installed versions the same way regardless
    # of whether the environment was built with pip or Poetry - only the
    # dependency FILES differ (requirements.txt vs pyproject.toml/poetry.lock),
    # not how the installed distributions are introspected at runtime.
    print('\nInstalled packages (sample):')
    for name in ['numpy', 'pandas', 'matplotlib', 'requests']:
        try:
            ver = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            ver = 'not installed'
        print(f"- {name}: {ver}")


if __name__ == '__main__':
    statuses = check_dependencies()
    print_dependency_report(statuses)
    if not all(statuses.values()):
        install_instructions()
        sys.exit(0)
    show_versions()
    run_analysis()
