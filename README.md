# UCL_DZZT7_DISSERTATION
The codes and data used for the Dissertation Thesis of candidate number DDZT7 at University College London

Mask2Former.ipynb - This script contains the Mask2Former image segmentation model. Use this
to process and get the image segmentation masks for all the street-view
images.

Results_processing.ipynb - This script processes all the image segmentation results to calculate urban
visual indices such as walkability, GVI, motorization and visual enclosure.

Equirec2Perspec.py - This script defines functions and helper functions that transform an
equirectangular panoramic image into images with normal perspective
views. To actually run it use the pano2norm.py script where the functions
are called in a main function.

pano2norm.py - Use this script to turn the panoramic images into normal perspective view
images. Change the variables input_directory and output_directory
according to your source and output directories. Put this in the same
directory with Equirec2Perspec.py for this to work.

Amsterdam.zip - The original image dataset. 4,900 Panoramic Street-View Images taken from
various locations in Amsterdam.

900_pano.zip - 900 panoramic Images randomly selected from the original dataset. This
is provided because the results of random selection cannot be replicated.

3600_svi.zip - 3600 normal perspective images. We split the 900 panoramas into four
view angles (0, 90, 120, 270), producing 900*4 = 3,600 stree-view images.
You can reproduce this dataset by using 900_pano as the input to
pano2norm.py

INDELING_STADSDEEL.csv - The shapefile of the 9 boroughs of Amsterdam. Available at the Amsterdam
government website.

DERTIG.csv - The street network shapefile of Amsterdam. You can use this to calculate
the service areas of the metro and tram network and greenspaces. Available
at the Amsterdam government website.

postcodes4-buurten.csv - The shapefile of all postcodes in Amsterdam, and we use this to calculate
the aggregated averages of the Indices. Available at the Amsterdam
government website.

TRAMMETRO_PUNTEN_2024.csv - The metro and tram station of Amsterdam. Use this in combination with
the road network shapefile to calculate the service areas of the stations.
Available on the Amsterdam government website.

TRAMMETRO_LIJNEN_2024.csv - The metro and tram lines of Amsterdam.

PARKPLANTSOENGROEN.csv - The shapefile of all green spaces (parks, sports fields) in Amsterdam. Use
this in combination with the road network shapefile to calculate the service
areas of the green spaces. Available on the Amsterdam government website.

QGIS - Download QGIS (or any GIS with similar functionalities) Use this to visualise all of the results and findings. Although any similar
GIS software also works.


