# Visualization of Geo-Spacial Prediction project

Settings
===
This project is written in Python through Eclipse IDE(Pydev is also required).<br />
Data was separated with code when implementing. Please modify src/Constant/filelocations.py to rebuild path to DATA.<br />

To run
===
There are several functions in this project.<br />
1. To transform data with adresses into geo location postion(Latitude, Longitude), please run src/locating/google.py or   src/locating/osm.py. <br />
  They share same functionality, but with different performance. Open Street Map(OSM) is open source map system, but with limited ability to transform address to geo location. Google, on the other hand, has copyright issue, but powerful.<br />

2. To eliminate duplicate data, please run src/datapreprocess/duplicate_eliminator.py<br /> 
  Some geospacial prediction model doesn't support duplicate features in data. It would be good to remove them before taking data into algorithm. Also, creating voronoi diagram, you can not have two data point on same geo location position.<br />

3. To create json file for visualization on map, please run src/vorplots/plot.py<br />
  Geojson data is a special format of json, which can be added in map as extra layer and can be recognized by most of web browsers.<br />

4. To create map for your data, please run src/MapCreating/build.py<br />
  Note: you need to change value of geocoder.osm('dublin,ireland') by replacing 'dublin,ireland' to anywhere you are interested and also fit your data.<br />
  The map will be generated in the place you setted in src/Constant/filelocations.py<br />

Examples
===
Dublin House Price Voronoi Diagram<br />
![alt tag](https://github.com/wuga214/GeoSpatialPredictionVisualization/blob/master/dublin2013.png)

San Francisco House Price Voronoi Diagram<br />
![alt tag](https://github.com/wuga214/GeoSpatialPredictionVisualization/blob/master/houseprice.png)

United States Temperature Voronoi Digram 01/01/2015<br />
![alt tag](https://github.com/wuga214/GeoSpatialPredictionVisualization/blob/master/ustemperature.png)

More alive examples can be found under folder DEMOs.

Contects
===
Mr.Wu<br />
Oregon State University<br />
U.S.A<br />
[Email](wug2@oregonstate.edu)
