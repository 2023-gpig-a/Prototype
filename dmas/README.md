# DMAS - Data Management and Analysis System

This system will be responsible for the following:
* Ingesting raw image data into the database
* Analysing raw image data to extract plant data
* Matching similar plants and assigning a `plant_id` to them
* Tracking the growth of plants over time

## Endpoints:

`/upload_images`
When a get request is made to this endpoint, the DMAS will scan our file system for any new images, if they are found it will create a new postgres entry for each image, storing the longitude, latitude, file location, and a timestamp of the image. We will extract this data from the image metadata. The entry will not be uploaded, and the image will be deleted if we believe the image contains a human.

Returns: `{"status":"success"}`

`/process_raw_images`
When a get request is made to this endpoint, the DMAS will look at all images that have not yet been processed, look for plants in them, assign them a `plant_id`, and upload the data to our database.

Returns: `{"status":"success"}`

`/track_growth`
When a get request is made to this endpoint, the DMAS will look at all of our processed data, arrange it based on date, and return a key value map of `plant_id` to plant growth data.

Returns: `{plant_id: plant_growth_data}`