# GeoPlanner

GeoPlanner is a soil investigation planning app for civil engineering projects.

The app should allow to set the number and depth of soundings needed to complete a geotechnical survey given some basic details on the project such as structural type, function, dimensions, expected stratigraphy, etc. Provisions should also be made to allow for specification of amount and type of undisturbed samples, and lab tests. Finally, once a survey plan is reached, it should be posible to calculate the related cost and plot a map and report. Compliance with international codes is also a desirable feature.

# Significant advances:

- Created a list of construction classes that indicate minimum number of test points and a distance coefficient for each class.

- Created a list of variability types that define a maximum basic distance between points according to geological background.

- Created an algorithm to generate random polygons. This will be useful for testing.

- Created an algorithm to generate a grid of points with a specified resolution inside the polygon bounds.

- Created an algorithm to filter points in the grid that fall within the polygon.

# To do:

- Create a function that calculates the maximum distance between test points based on construction class and variability type.

- Create an offset polygon inside the main polygon to filter the points in the grid. This would avoid points falling in the polygon boundary. Offset distance should be about 2 to 5 meters.


Work in progress..