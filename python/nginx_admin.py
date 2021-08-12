#!/usr/bin/env python3

from pathlib import Path

CONF_FILE_LOCATIONS = (
    '/usr/local/nginx/conf',
    '/etc/nginx',
    '/usr/local/etc/nginx',
)


class Setting:
    def __init__(self):
        self.file_path = None
        self.lineno = 0
        self.name = ''
        self.is_commented_out = False


class SimpleDirective(Setting):
    def __init__(self):
        super().__init__()
        self.value = ''


class BlockDirective(Setting):
    def __init__(self):
        super().__init__()
        self.end_lineno = 0



class Configuration:
    def __init__(self):
        self.user = None



class ConfigurationParser:

    @staticmethod
    def strip_comments(line):
        try:
            hash_index = line.index('#')
        except ValueError:
            return line
        else:
            return line[:hash_index]

    def parse(self, config_path):
        config = Configuration()
        with open(str(config_path), 'r') as nginx_conf:
            for line_number, line in enumerate(nginx_conf, 1):
                line = self.strip_comments(line)
                line = line.strip()
                if not line:
                    continue
                print(line)

                if line.endswith(';'):
                    self.handle_main_setting




                if line_number > 15:
                    break
        return config


def main():
    parser = ConfigurationParser()
    config = parser.parse(Path('/etc/nginx/nginx.conf'))





if __name__ == '__main__':
    main()