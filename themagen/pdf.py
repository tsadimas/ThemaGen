"""
Generate PDF attachemnts from Markdown tests 
"""
import sys
import subprocess

import themagen.log
import themagen.config
import themagen.users


_logger = themagen.log.get(__name__)
_pdf_engine = 'xelatex'
_font = 'NotoSans Nerd Font'

def generate():
    try:
        cfg = themagen.config.read()
        users = themagen.users.read_csv()
        for user in users:
            _create_pdf(user, cfg)
    except:
        _logger.error('program exit with error')
        sys.exit(1)


def _create_pdf(user: themagen.users.User, cfg):
    command = [
        'pandoc',
        f'--pdf-engine={_pdf_engine}',
        '-V',
        f'mainfont="{_font}"',
        '-V',
        'geometry:a4paper,margin=2cm',
        '-s',
        f'assets/files/{user.full_name_sanitized}.md',
        '-o',
        f'assets/files/{user.full_name_sanitized}.pdf'
    ]
    print(str(command))
    subprocess.run(command)
