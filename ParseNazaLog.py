# Change history
# 2014/07/20 - at Lookat command




import simplekml
import csv

filename = raw_input("Enter CSV file: ")

#Setup csv structure
order = ['Time', 'Mode', 'Battery_Voltage', 'Latitude', 'Longitude', 'GPS Altitude', 'COG', 'Speed', 'VSI', 'Fix', 'NumSat', 'Altitude', 'Heading', 'Pitch', 'Roll', 'RC-A', 'RC-E', 'RC-T', 'RC-R', 'RC-U', 'RC-X1', 'RX-X2']
csvReader = csv.DictReader(open(filename),order)

kml = simplekml.Kml()

# Skip the header line.
csvReader.next()

# Read GPS data from each row in CSV file
coordinates=[]
count = 0;

for row in csvReader:

  if row["Fix"]!= "No fix":          # Discard invalid GPS data
     lat = float(row["Latitude"])
     lon = float(row["Longitude"])
     dataset = (lon,lat,float(row["GPS Altitude"]))
     coordinates.append(dataset)
     count=count+1

lin = kml.newlinestring(name="Pathway", description="FlightPath", coords=coordinates)

lin.style.linestyle.color = simplekml.Color.yellowgreen
lin.style.linestyle.width = 2  #  pixels
lin.altitudemode = simplekml.AltitudeMode.absolute
lin.extrude = 1

# Add default viewpoint closest to last coordinates
lin.lookat.gxaltitudemode = simplekml.GxAltitudeMode.relativetoseafloor
lin.lookat.latitude = lat
lin.lookat.longitude = lon
lin.lookat.range = 1000
lin.lookat.heading = 56
lin.lookat.tilt = 78

kml.save(filename +".kml")

print("{0} lines processed".format(count))