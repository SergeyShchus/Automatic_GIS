# START #

conda install -c esri arcgis

conda install -c esri -c fastai -c pytorch arcgis=1.8.1 scikit-image=0.15.0 pillow=6.2.2 libtiff=4.0.10 fastai=1.0.60 pytorch=1.4.0 torchvision=0.5.0 --no-pin

# For TensorFlow support (optional), use the following command:
conda install -c esri -c fastai -c pytorch arcgis=1.8.1 scikit-image=0.15.0 pillow=6.2.2 libtiff=4.0.10 fastai=1.0.60 pytorch=1.4.0 torchvision=0.5.0 tensorflow-gpu=2.1.0 --no-pin

#For Multispectral data support (optional and needed only for Anaconda users)
conda install gdal=2.3.3

conda upgrade -c esri arcgis

from arcgis.gis import GIS
my_gis = GIS()
m = my_gis.map()
m







#OSM Runner

* Create a new environment with Conda
    * conda create -n osm_dash python=3.6 -y

* Activate new environment
    * activate osm_dash

* Install ArcGIS API for Python
    * conda install arcgis -c esri -y

* Install Jupyter Dashboard
    * conda install jupyter_dashboards -c conda-forge -y

* Install requests, pyproj, pyshp
    * conda install requests pyproj pyshp -y

* Install osm_runner
    * pip install osm-runner

* Run 'jupyter notebook' with environment activated and navigate to this notebook on your system

* Set the org_url, username, and password for the GIS variable in the first cell of this notebook
