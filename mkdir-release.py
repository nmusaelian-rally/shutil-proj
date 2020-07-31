USAGE = """
Usage: python mkdir-release.py {version}

       e.g. python mkdir-release.py 1.1.0
"""

import sys, os
from shutil import copyfile
import re

RELEASES_ROOT = '../playground/lac/replicated/releases'
YAML_FILES = ['release.yaml.j2', 'stable.yaml', 'support.yaml']

def update_file(stable, version):
    with open(stable, 'r') as f:
        content = f.read()

    with open(stable, 'w') as f2:
        f2.write(re.sub('(-\d+)', f'-{version}', content.replace('-dev', '-prod')))


def main(args):
    version = args[0]
    new_release_dir = f'{RELEASES_ROOT}/GA/{version}'
    if not os.path.exists(new_release_dir):
        os.makedirs(new_release_dir)

    if not os.listdir(new_release_dir):
        for yf in YAML_FILES:
            copyfile(f'{RELEASES_ROOT}/{yf}', f'{new_release_dir}/{yf}')
    else:
        print(f'{new_release_dir} is not empty. Goodbye!')

    stable = f'{new_release_dir}/stable.yaml'
    update_file(stable, version)

if __name__ == '__main__':
    main(sys.argv[1:])