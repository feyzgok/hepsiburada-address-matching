from pathlib import Path
import numpy as np
import pandas as pd

base_dir = Path(__file__).resolve().parent
samp_path = base_dir / 'data' / 'sample_submisson.csv'
test_path = base_dir / 'data' / 'test.csv'
train_path = base_dir / 'data' / 'train.csv'

df_train = pd.read_csv(train_path)
