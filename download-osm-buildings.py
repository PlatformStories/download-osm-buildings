import json
import os
import requests
import subprocess

input_ports_location = '/mnt/work/input/'
output_ports_location = '/mnt/work/output/'

# Get bounding box
bbox = json.load(open(os.path.join(input_ports_location, 'ports.json')))['bbox']

# Create output directory
output_dir = os.path.join(output_ports_location, 'geojson')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
os.chdir(output_dir)

# Retrieve footprints
print 'Retrieving footprints from Overpass'
with open('buildings.osm', 'w') as f:
    r = requests.get(url='http://www.overpass-api.de/api/xapi_meta?*[building=yes][bbox=' + bbox + ']')
    f.write(r.text.encode('ascii','ignore'))

# Convert .osm to .geojson
print 'Converting to geojson'
convert = 'ogr2ogr -f GeoJSON buildings.geojson buildings.osm multipolygons'
proc = subprocess.Popen([convert], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = proc.communicate()

# Delete osm file
delete = 'rm buildings.osm'
proc = subprocess.Popen([delete], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = proc.communicate()

print 'Done'
