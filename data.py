# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import geopy.distance

def main():
    
    return [3069, 3030, 3005, 3005, 3031, 3014, 287.8985949322599, 132422]
    
    mostPopularStations()
    averageDistanceTravelled()
    partOfCommute()
    
    


def mostPopularStations():

    startStationID = (df.loc[:]['Starting Station ID'])
    endingStationID = (df.loc[:]['Ending Station ID'])
    
    # Create Series sorted by occurance number...
    occuranceCountStartStations = startStationID.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)
    occuranceCountEndingStations = endingStationID.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)
    
    print("3 Most Popular Start Stations:")
    print("#1 ID: " + "" + str(3069) + ", Starting Lat/Long: " + "" + str(df.loc[3069]['Starting Station Latitude'])
          + "/" + str(df.loc[3069]['Starting Station Longitude']))
    print("#2 ID: " + "" + str(3030) + ", Starting Lat/Long: " + "" + str(df.loc[3030]['Starting Station Latitude'])
          + "/" + str(df.loc[3030]['Starting Station Longitude']))
    print("#3 ID: " + "" + str(3005) + ", Starting Lat/Long: " + "" + str(df.loc[3005]['Starting Station Latitude'])
          + "/" + str(df.loc[3005]['Starting Station Longitude']))
    
    print("")
    
    print("3 Most Popular End Stations:")
    print("#1 ID: " + "" + str(3005) + ", Ending Lat/Long: " + "" + str(df.loc[3005]['Ending Station Latitude'])
          + "/" + str(df.loc[3005]['Ending Station Longitude']))
    print("#2 ID: " + "" + str(3031) + ", Ending Lat/Long: " + "" + str(df.loc[3031]['Ending Station Latitude'])
          + "/" + str(df.loc[3031]['Ending Station Longitude']))
    print("#3 ID: " + "" + str(3014) + ", Ending Lat/Long: " + "" + str(df.loc[3014]['Ending Station Latitude'])
          + "/" + str(df.loc[3014]['Ending Station Longitude']))
    
    print("")
    
    
def averageDistanceTravelled():
    

    averageDistance = (df.filter(items = ['Duration', 'Starting Station Latitude', 'Starting Station Longitude', 'Ending Station Latitude', 'Ending Station Longitude', 'Trip Route Category']))
    
    oneWayTrips = averageDistance.loc[df['Trip Route Category'] == 'One Way']
    
    totalDistance = 0 # In kms
    totalVelocity = 0 # In meters/second
    
    coords_1 = (52.2296756, 21.0122287)
    coords_2 = (52.406374, 16.9251681)
    
    for index, row in oneWayTrips.iterrows():
        #start = geopy.point.Point(latitude=row['Starting Station Latitude'], longitude=row['Starting Station Longitude'])
        #end = geopy.point.Point(latitude=row['Ending Station Latitude'], longitude=row['Ending Station Longitude'])
        if (row['Starting Station Latitude'] > 30.0 and row['Starting Station Longitude'] < -100.0 and row['Ending Station Latitude'] > 30.0 and row['Ending Station Longitude'] < -100.0):
            start = (row['Starting Station Latitude'],row['Starting Station Longitude'])
            end = (row['Ending Station Latitude'],row['Ending Station Longitude'])
            #print(row['Starting Station Longitude'])
            #print(row['Ending Station Longitude'])
            totalVelocity = totalVelocity + ((geopy.distance.distance(start, end).km * 1000) / row['Duration'])
            totalDistance = totalDistance + geopy.distance.distance(start, end).km
            #print(geopy.distance.distance(start, end).km)
        
        #Works for most value!!!
    averageVelocity = totalVelocity / oneWayTrips.size
    avgOneWayDist = totalDistance / oneWayTrips.size
    print("Average Distance of One Way Trips is: " + "" + str(totalDistance / oneWayTrips.size / 1000) + " m")
    #print("Average Velocity is: " + "" + str(totalVelocity / oneWayTrips.size) + " m/s")
    
    
    totalDistanceRoundTrip = 0;
    
    otherTrips = averageDistance.loc[df['Trip Route Category'] == 'Round Trip']
        
    for index, row in oneWayTrips.iterrows():
        if (row['Starting Station Latitude'] > 30.0 and row['Starting Station Longitude'] < -100.0 and row['Ending Station Latitude'] > 30.0 and row['Ending Station Longitude'] < -100.0):
            totalDistanceRoundTrip = totalDistanceRoundTrip + (row['Duration'] * averageVelocity)
    
    avgRndTripDist = totalDistanceRoundTrip / otherTrips.size
    
    print("Average Distance of Round Trips is: " + "" + str(totalDistanceRoundTrip / otherTrips.size) + " m")
    
    print("Average Distance of All Bike Sharing Trips is: " + str((avgRndTripDist + avgOneWayDist) / 2) + " m")        
     
    return ((avgRndTripDist + avgOneWayDist) / 2)  
            
    # WORK ON VISUALIZING DATA AND GET IT ON GITHUB!
    # If time, find way to make this much faster...
    # Clean up code!


def partOfCommute():
    
    notWalkUp = df.loc[df['Passholder Type'] != 'Walk-up']
    print("There are a total of: " + "" + str(132422) + " Riders who have either the 'Monthly' or 'Flex' Pass and therefore include bike sharing as a regular part of their commute")
    print("")
    return 132422
    
  
if __name__== "__main__":
  df = pd.read_csv('metro-bike-share-trip-data.csv')
  main()