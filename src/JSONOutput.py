import os
import jsonpickle
from pathlib import Path

from src.utils.Singleton import Singleton
from src.Catalogue import Catalogue
from src.Configuration import Configuration

class JSONOutput(Singleton, object):

    dump_file_path = os.path.join(Path(os.path.dirname(__file__)).parent, 'www/assets/libsearch.json')

    def dump_info(self, catalogue: Catalogue):
        dump = {
            'catalogue': catalogue,
            'libraries': Configuration().cultuurconnect['branches']
        }
        with open(self.dump_file_path, 'w') as catalogue_cache:
            catalogue_cache.write(jsonpickle.encode(dump, unpicklable=False))
