# vim:fileencoding=utf-8
import os
from typing import Optional

from powerline.lib.unicode import out_u
from powerline.theme import requires_segment_info
from powerline.segments import Segment, with_docstring


@requires_segment_info
def virtualenv(pl, segment_info, venv_mode='indicator') -> Optional[str]:
    '''Returns whether we are in a Python virtualenv.'''
    basename = os.path.basename(segment_info['environ'].get('VIRTUAL_ENV', ''))
    if not basename:
        return None

    if venv_mode == 'indicator':
        return 'venv'
    elif venv_mode == 'fullname':
        return basename
