import os
import json
import random
import argparse

from monai.config import print_config
from monai.apps import download_and_extract
from monai.apps.auto3dseg import AutoRunner

import yaml

print_config()
root_dir = "/workspace"
work_dir = os.path.join(root_dir, "work_dir")


def autogen_datalist():
    msd_task = "Task09_Spleen"
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)
    # Download dataset
    resource = "https://msd-for-monai.s3-us-west-2.amazonaws.com/Task09_Spleen.tar"

    compressed_file = os.path.join(root_dir, os.path.basename(resource))
    dataroot = os.path.join(root_dir, msd_task)

    if not os.path.exists(dataroot):
        download_and_extract(resource, compressed_file, root_dir)

    test_dir = os.path.join(dataroot, "imagesTs/")
    train_dir = os.path.join(dataroot, "imagesTr/")
    label_dir = os.path.join(dataroot, "labelsTr/")
    datalist_json = {"testing": [], "training": []}

    datalist_json["testing"] = [
        {"image": "./imagesTs/" + file} for file in os.listdir(test_dir) if (".nii.gz" in file) and ("._" not in file)
    ]

    datalist_json["training"] = [{"image": "./imagesTr/" + file, "label": "./labelsTr/" + file, "fold": 0} for file in os.listdir(train_dir) if (".nii.gz" in file) and ("._" not in file)]  # Initialize as single fold

    random.shuffle(datalist_json["training"])

    num_folds = 5
    fold_size = len(datalist_json["training"]) // num_folds
    for i in range(num_folds):
        for j in range(fold_size):
            datalist_json["training"][i * fold_size + j]["fold"] = i

    datalist_file = os.path.join(work_dir, "msd_" + msd_task.lower() + "_folds.json")
    with open(datalist_file, "w", encoding="utf-8") as f:
        json.dump(datalist_json, f, ensure_ascii=False, indent=4)
    print(f"Data root is: {dataroot}")
    print(f"Datalist is saved to {datalist_file}")
    return dataroot, datalist_file


def autogen_input(dataroot, datalist):
    # save it to yaml input.yaml
    input_dict = {
        "name": "Task09_Spleen",
        "task": "segmentation",
        "modality": "CT",
        "datalist": datalist,
        "dataroot": dataroot,
        "multigpu": True,
    }
    input_file = os.path.join(work_dir, "task.yaml")
    with open(input_file, "w") as f:
        yaml.dump(input_dict, f)
    print(f"Input is saved to {input_file}")
    return input_dict


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_node", type=int, default=1)
    num_node = parser.parse_args().num_node

    if not os.path.exists(root_dir):
        os.makedirs(root_dir)
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)
    dataroot, datalist = autogen_datalist()
    input_cfg = autogen_input(dataroot, datalist)
    # runner = AutoRunner(input=input_cfg, algos=['segresnet'])
    # if num_node > 1:
    #     runner.set_device_info(num_nodes=num_node)
    # runner.run()
