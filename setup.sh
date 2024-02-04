!#/bin/sh
set -eux

#COCO Dataset
mkdir -p Datasets/coco/images
cd Datasets/coco/images

curl http://images.cocodataset.org/zips/train2017.zip --output train2017.zip
curl http://images.cocodataset.org/zips/val2017.zip --output val2017.zip
curl http://images.cocodataset.org/zips/test2017.zip --output test2017.zip
curl http://images.cocodataset.org/zips/unlabeled2017.zip --output unlabeled2017.zip

unzip train2017.zip
unzip val2017.zip
unzip test2017.zip
unzip unlabeled2017.zip

rm train2017.zip
rm val2017.zip
rm test2017.zip
rm unlabeled2017.zip

cd ../
curl http://images.cocodataset.org/annotations/annotations_trainval2017.zip --output annotations_trainval2017.zip
curl http://images.cocodataset.org/annotations/stuff_annotations_trainval2017.zip --output stuff_annotations_trainval2017.zip
curl http://images.cocodataset.org/annotations/image_info_test2017.zip --output image_info_test2017.zip
curl http://images.cocodataset.org/annotations/image_info_unlabeled2017.zip --output image_info_unlabeled2017.zip

unzip annotations_trainval2017.zip
unzip stuff_annotations_trainval2017.zip
unzip image_info_test2017.zip
unzip image_info_unlabeled2017.zip

rm annotations_trainval2017.zip
rm stuff_annotations_trainval2017.zip
rm image_info_test2017.zip
rm image_info_unlabeled2017.zip
