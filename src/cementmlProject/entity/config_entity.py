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


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: float
    max_depth: float
    max_features: str
    min_samples_leaf: float
    min_samples_split: float
    n_estimators: float
    target_column: str



