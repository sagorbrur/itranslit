__version__="1.0.2"

from wasabi import msg
from itranslit.utils import is_torch_available

if is_torch_available():
    from itranslit.transliterate import Translit

if not is_torch_available():
    msg.fail("torch not available. Please install pytorch 1.7.0+")