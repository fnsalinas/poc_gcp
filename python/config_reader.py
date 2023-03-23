

from typing import Dict, List, Tuple, Any
import json
from glob import glob

folder_path: str = "/home/ubuntu/workspace/fsalinas/poc_gcp/config/*"

json_files: List[Dict[str, Any]] = sorted(glob(folder_path))



print(json_files)

