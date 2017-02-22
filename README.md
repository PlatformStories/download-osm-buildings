# download-osm-buildings

A GBDX task that downloads OSM building footprints using the [Overpass API](http://wiki.openstreetmap.org/wiki/Overpass_API).
You can find an example of using download-osm-buildings [here](http://gbdxstories.digitalglobe.com/osm-lulc/).


## Run

In a Python terminal:

```python
import gbdxtools
from os.path import join
import uuid

gbdx = gbdxtools.Interface()

dob = gbdx.Task('download-osm-buildings')

# Specify bounding box in W, S, E, N
dob.inputs.bbox = '-73.96, 40.67, -73.89, 40.75'

# Run gbdx workflow and save output geojson under platform-stories/trial-runs/random_str
wf = gbdx.Workflow([dob])
random_str = str(uuid.uuid4())
output_location = join('platform-stories/trial-runs', random_str)
wf.savedata(maxtree.outputs.geojson, output_location)
wf.execute()
```

## Input ports

| Name  | Type |  Description | Required |
|-------|--------------|----------------|----------------|
| bbox | String | Bounding box in W, S, E, N. | True |


## Output ports

| Name  | Type | Description                                    |
|-------|---------|---------------------------------------------------|
| geojson | Directory | Contains buildings.geojson. |


## Development

### Build the Docker image

You need to install [Docker](https://docs.docker.com/engine/installation/).

Clone the repository:

```bash
git clone https://github.com/digitalglobe/download-osm-buildings
```

Then:

```bash
cd download-osm-buildings
docker build -t download-osm-buildings .
```

### Try out locally

Create a container in interactive mode and mount the sample input under `/mnt/work/input/`:

```bash
docker run -v full/path/to/sample-input:/mnt/work/input -it download-osm-buildings
```

Then, within the container:

```bash
python /download-osm-buildings.py
```

Confirm that the tileset is present in your account.

### Docker Hub

Login to Docker Hub:

```bash
docker login
```

Tag your image using your username and push it to DockerHub:

```bash
docker login
docker tag download-osm-buildings yourusername/download-osm-buildings
docker push yourusername/download-osm-buildings
```

The image name should be the same as the image name under containerDescriptors in download-osm-buildings.json.

Alternatively, you can link this repository to a [Docker automated build](https://docs.docker.com/docker-hub/builds/).
Every time you push a change to the repository, the Docker image gets automatically updated.

### Register on GBDX

In a Python terminal:

```python
import gbdxtools
gbdx = gbdxtools.Interface()
gbdx.task_registry.register(json_filename='download-osm-buildings.json')
```

Note: If you change the task image, you need to reregister the task with a higher version number
in order for the new image to take effect. Keep this in mind especially if you use Docker automated build.
