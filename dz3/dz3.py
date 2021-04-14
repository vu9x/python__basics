import os
from shutil import copyfile


def collect_templates(root_dir):
    for root, dir, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                dir_name = os.path.join('templates', os.path.basename(root))
                if not os.path.exists(dir_name):
                    os.makedirs(dir_name)

                copyfile(os.path.join(root, file), os.path.join(dir_name, file))


if __name__ == '__main__':
    root_directory = os.path.dirname(os.path.realpath(__file__))
    collect_templates(root_directory)
