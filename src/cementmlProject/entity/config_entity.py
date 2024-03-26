from dataclasses import dataclass
from pathlib import Path




## entity is custom return type function unllike inbuilt one ,here this @ dataclass is used as decorator fur custom return type fn, frozen=True ,it won't be acepting other cariable type ,it'll give error

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

##next step is updating confuguration manager in src which will return all this paths in one shot
    
