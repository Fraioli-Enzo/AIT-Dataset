# Dataset Collection and Management

This repository contains several datasets sourced from [Roboflow](https://universe.roboflow.com/).  
It also includes a custom dataset located in the `RoboflowDataset` folder, which is a homemade combination of the other datasets.

## Folder Structure

- `RoboflowDataset`  
  A custom dataset created by merging and modifying existing Roboflow datasets.

## Dataset Management

- The `DatasetManegement.py` script is a base for managing and transforming datasets.
- You can use it to:
  - Modify existing datasets
  - Merge multiple datasets
  - Create new datasets based on your own criteria

## How to Use

1. Open `DatasetManegement.py`.
2. Edit the script to fit your needs:
   - Define how datasets should be combined or filtered.
   - Adjust paths or parameters based on your local setup.

> This script is not a plug-and-play tool. It provides a flexible base that you need to adapt depending on your specific use case.
