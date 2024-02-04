#!/bin/sh
set -eux

#COCO Dataset
mkdir -p Datasets/coco/images
cd Datasets/coco/images

get_data() {
    curl "$1" --output "$2"
    unzip "$2"
    rm "$2"
}

get_data "http://images.cocodataset.org/zips/train2017.zip" "train2017.zip"
get_data "http://images.cocodataset.org/zips/val2017.zip" "val2017.zip"
get_data "http://images.cocodataset.org/zips/test2017.zip" "test2017.zip"
get_data "http://images.cocodataset.org/zips/unlabeled2017.zip" "unlabeled2017.zip"

cd ../
get_data "http://images.cocodataset.org/annotations/annotations_trainval2017.zip" "annotations_trainval2017.zip"
get_data "http://images.cocodataset.org/annotations/stuff_annotations_trainval2017.zip" "stuff_annotations_trainval2017.zip"
get_data "http://images.cocodataset.org/annotations/image_info_test2017.zip" "image_info_test2017.zip"
get_data "http://images.cocodataset.org/annotations/image_info_unlabeled2017.zip" "image_info_unlabeled2017.zip"
