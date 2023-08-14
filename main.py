"""
@Author: Lake
@Date: 2023/8/14
"""
import pandas as pd

train = pd.read_csv(r"data/labeledTrainData.tsv", header=0, delimiter='\t', quoting=3)
