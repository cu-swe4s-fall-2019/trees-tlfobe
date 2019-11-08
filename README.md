# Tree

[![Build Status](https://travis-ci.com/cu-swe4s-fall-2019/trees-tlfobe.svg?branch=master)](https://travis-ci.com/cu-swe4s-fall-2019/trees-tlfobe)

## Installation

This package uses the following packages.

- sys
- os
- argparse
- matplotlib
- time
- random

The only one that should be installed is `matplotlib`. The following snippet can be used to install `matplotlib`:
```
conda install matplotlib --yes
```

## Usage

The main program used in this repository is `insert_key_value_pairs.py`. This program can be used to time and benchmark various data structures with different types of data types. This script has the following input flags:

- `--data_struct`: The data structure to store key/value pairs in. Options are `hash`, `AVL` and `tree`.
- `--data_file`: The data file to read key/value pairs from.
- `--n_values`: The number of values to pull from the `data_file`
- `--sub_sample`: The fraction of values to pull when searching data structures. Default value is `0.2`
- `--outfile`: Output file for graphing of benchmarks.

An example of how this program is used is shown below.

```
python insert_key_value_pairs.py --data_struct hash --data_file rand.txt --n_values 10000 --sub_sample 0.5 --outfile images/hash_rand_10000.png
```

## Results

