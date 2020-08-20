# Imports
import sys
sys.path.append('../../PythonWrapper')
from ObjectCubePython import *

# Set the database location
#Parameters.getParameters().add( "MonetDB_database", "objectcube" )
Parameters.getParameters().add( "MonetDB_database", "objectcube" )
hub = Hub.getHub()


#############################################################################################
tagset = AlphanumericalTagSet('Hike').create()
hikeDimension = tagset.createPersistentDimension( tagset.fetchOrAddTag("Hike") )
hikeNode = hikeDimension.getRoot()
node = hikeDimension.addNode( hikeNode.id, tagset.fetchOrAddTag("Day 1") )
node = hikeDimension.addNode( hikeNode.id, tagset.fetchOrAddTag("Day 2") )
node = hikeDimension.addNode( hikeNode.id, tagset.fetchOrAddTag("Day 3") )
node = hikeDimension.addNode( hikeNode.id, tagset.fetchOrAddTag("Day 4") )
node = hikeDimension.addNode( hikeNode.id, tagset.fetchOrAddTag("Day 5") )
#############################################################################################

#############################################################################################
tagset = AlphanumericalTagSet('Location').create()
locationDimension = tagset.createPersistentDimension( tagset.fetchOrAddTag("Location") )
rootNode = locationDimension.getRoot()

cabinsNode = locationDimension.addNode( rootNode.id, tagset.fetchOrAddTag("Cabin"))
#locationDimension.addNode( cabinsNode.id, tagset.fetchOrAddTag("Landmannalaugar") )
locationDimension.addNode( cabinsNode.id, tagset.fetchOrAddTag("Hrafntinnusker") )
locationDimension.addNode( cabinsNode.id, tagset.fetchOrAddTag("Hvanngil") )
locationDimension.addNode( cabinsNode.id, tagset.fetchOrAddTag("Emstrur") )
locationDimension.addNode( cabinsNode.id, tagset.fetchOrAddTag("Thorsmork") )

glacierNode = locationDimension.addNode( rootNode.id, tagset.fetchOrAddTag("Glacier"))
locationDimension.addNode( glacierNode.id, tagset.fetchOrAddTag("Eyjafjallajokull") )
locationDimension.addNode( glacierNode.id, tagset.fetchOrAddTag("Steinsholtsjokull") )
locationDimension.addNode( glacierNode.id, tagset.fetchOrAddTag("Myrdalsjokull") )

caveNode = locationDimension.addNode( rootNode.id, tagset.fetchOrAddTag("Cave"))
locationDimension.addNode( caveNode.id, tagset.fetchOrAddTag("Songhellir") )
locationDimension.addNode( caveNode.id, tagset.fetchOrAddTag("Snorrariki") )

oasisNode = locationDimension.addNode( rootNode.id, tagset.fetchOrAddTag("Oasis"))
locationDimension.addNode( oasisNode.id, tagset.fetchOrAddTag("Landmannalaugar") )
#locationDimension.addNode( oasisNode.id, tagset.fetchOrAddTag("Thorsmork") )
locationDimension.addNode( oasisNode.id, tagset.fetchOrAddTag("Langidalur") )

montainNode = locationDimension.addNode( rootNode.id, tagset.fetchOrAddTag("Mountain"))
#locationDimension.addNode( montainNode.id, tagset.fetchOrAddTag("Hrafntinnusker") )
locationDimension.addNode( montainNode.id, tagset.fetchOrAddTag("Sodull") )
locationDimension.addNode( montainNode.id, tagset.fetchOrAddTag("Unicorn") )
locationDimension.addNode( montainNode.id, tagset.fetchOrAddTag("Katla") )
locationDimension.addNode( montainNode.id, tagset.fetchOrAddTag("Utigonguhofdar") )
locationDimension.addNode( montainNode.id, tagset.fetchOrAddTag("Storkonufell") )
locationDimension.addNode( montainNode.id, tagset.fetchOrAddTag("Blahnukur") )
locationDimension.addNode( montainNode.id, tagset.fetchOrAddTag("Haskerdingur") )
locationDimension.addNode( montainNode.id, tagset.fetchOrAddTag("Svartihryggur") )
locationDimension.addNode( montainNode.id, tagset.fetchOrAddTag("Valahnukur") )
locationDimension.addNode( montainNode.id, tagset.fetchOrAddTag("Utigonguhofdi") )
locationDimension.addNode( montainNode.id, tagset.fetchOrAddTag("Hattafell") )

riverNode = locationDimension.addNode( rootNode.id, tagset.fetchOrAddTag("River"))
locationDimension.addNode( riverNode.id, tagset.fetchOrAddTag("Markarfljot") )
locationDimension.addNode( riverNode.id, tagset.fetchOrAddTag("Krossa") )
locationDimension.addNode( riverNode.id, tagset.fetchOrAddTag("Fremri Emstrua") )
locationDimension.addNode( riverNode.id, tagset.fetchOrAddTag("Blafjallakvisl") )
locationDimension.addNode( riverNode.id, tagset.fetchOrAddTag("Thronga") )

hotspringsNode = locationDimension.addNode( rootNode.id, tagset.fetchOrAddTag("Hot Spring"))
locationDimension.addNode( hotspringsNode.id, tagset.fetchOrAddTag("Brennisteinsalda"))
locationDimension.addNode( hotspringsNode.id, tagset.fetchOrAddTag("Storihver"))

lakeNode = locationDimension.addNode( rootNode.id, tagset.fetchOrAddTag("Lakes"))
locationDimension.addNode( lakeNode.id, tagset.fetchOrAddTag("Alftavatn") )

canyonNode = locationDimension.addNode( rootNode.id, tagset.fetchOrAddTag("Canyon"))
locationDimension.addNode( canyonNode.id, tagset.fetchOrAddTag("Markarfljotsgljufur") )
locationDimension.addNode( canyonNode.id, tagset.fetchOrAddTag("Slyppugil") )
locationDimension.addNode( canyonNode.id, tagset.fetchOrAddTag("Bjorgil") )
#############################################################################################



#############################################################################################
tagset = AlphanumericalTagSet('Geology').create()
# Create Geology hir
geologyDim = tagset.createPersistentDimension( tagset.fetchOrAddTag("Geology") )
rootNode = geologyDim.getRoot()
geologyDim.addNode( rootNode.id, tagset.fetchOrAddTag("Flint"))
geologyDim.addNode( rootNode.id, tagset.fetchOrAddTag("Liparit"))
geologyDim.addNode( rootNode.id, tagset.fetchOrAddTag("Lava"))
geologyDim.addNode( rootNode.id, tagset.fetchOrAddTag("Ash"))
#############################################################################################



#############################################################################################
tagset = AlphanumericalTagSet('Object').create()
objectDim = tagset.createPersistentDimension( tagset.fetchOrAddTag("Object") )
rootNode = objectDim.getRoot()

equipmentNode = objectDim.addNode( rootNode.id, tagset.fetchOrAddTag("Gear"))
objectDim.addNode( equipmentNode.id, tagset.fetchOrAddTag("Backpack"))
objectDim.addNode( equipmentNode.id, tagset.fetchOrAddTag("Hiking boots"))
objectDim.addNode( equipmentNode.id, tagset.fetchOrAddTag("Compass"))
objectDim.addNode( equipmentNode.id, tagset.fetchOrAddTag("GPS"))
objectDim.addNode( equipmentNode.id, tagset.fetchOrAddTag("Camera"))
objectDim.addNode( equipmentNode.id, tagset.fetchOrAddTag("Tent"))
objectDim.addNode( equipmentNode.id, tagset.fetchOrAddTag("Medical"))
objectDim.addNode( equipmentNode.id, tagset.fetchOrAddTag("Sign"))

entertainmentNode = objectDim.addNode( rootNode.id, tagset.fetchOrAddTag("Entertainment"))
objectDim.addNode( entertainmentNode.id, tagset.fetchOrAddTag("Dinosaur"))
objectDim.addNode( entertainmentNode.id, tagset.fetchOrAddTag("Ball"))
objectDim.addNode( entertainmentNode.id, tagset.fetchOrAddTag("Frisbee"))
objectDim.addNode( entertainmentNode.id, tagset.fetchOrAddTag("Candy"))
objectDim.addNode( entertainmentNode.id, tagset.fetchOrAddTag("Food"))
objectDim.addNode( entertainmentNode.id, tagset.fetchOrAddTag("Flowers"))

vehiclesNode = objectDim.addNode( rootNode.id, tagset.fetchOrAddTag("Vehicle"))
objectDim.addNode( vehiclesNode.id, tagset.fetchOrAddTag("Car"))
objectDim.addNode( vehiclesNode.id, tagset.fetchOrAddTag("Airplane"))
objectDim.addNode( vehiclesNode.id, tagset.fetchOrAddTag("Bus"))
objectDim.addNode( vehiclesNode.id, tagset.fetchOrAddTag("Luggage Truck"))
#############################################################################################


#############################################################################################
tagset = AlphanumericalTagSet('Events').create()
eventsDim = tagset.createPersistentDimension( tagset.fetchOrAddTag("Events") )
rootNode = eventsDim.getRoot()

dayOneNode = eventsDim.addNode( rootNode.id, tagset.fetchOrAddTag("Day 1"))
eventsDim.addNode( dayOneNode.id, tagset.fetchOrAddTag("Bathing"))
eventsDim.addNode( dayOneNode.id, tagset.fetchOrAddTag("First Warmup"))
eventsDim.addNode( dayOneNode.id, tagset.fetchOrAddTag("Red clay faces"))
eventsDim.addNode( dayOneNode.id, tagset.fetchOrAddTag("Rain Break"))
eventsDim.addNode( dayOneNode.id, tagset.fetchOrAddTag("Foot Path Construction"))
eventsDim.addNode( dayOneNode.id, tagset.fetchOrAddTag("Frisbee"))

dayTwoNode = eventsDim.addNode( rootNode.id, tagset.fetchOrAddTag("Day 2"))
eventsDim.addNode( dayTwoNode.id, tagset.fetchOrAddTag("White Clay Faces"))
eventsDim.addNode( dayTwoNode.id, tagset.fetchOrAddTag("Ice Cave"))
eventsDim.addNode( dayTwoNode.id, tagset.fetchOrAddTag("Alftavatn"))
eventsDim.addNode( dayTwoNode.id, tagset.fetchOrAddTag("Wading Geithalskvisl"))
eventsDim.addNode( dayTwoNode.id, tagset.fetchOrAddTag("Wading Blafjallakvisl"))

dayThreeNode = eventsDim.addNode( rootNode.id, tagset.fetchOrAddTag("Day 3"))
eventsDim.addNode( dayThreeNode.id, tagset.fetchOrAddTag("The Dressmann Contest"))
eventsDim.addNode( dayThreeNode.id, tagset.fetchOrAddTag("Dodgeball"))
eventsDim.addNode( dayThreeNode.id, tagset.fetchOrAddTag("Break - Asa's injury"))
eventsDim.addNode( dayThreeNode.id, tagset.fetchOrAddTag("Rolling in the Ash"))

dayFourNode = eventsDim.addNode( rootNode.id, tagset.fetchOrAddTag("Day 4"))
eventsDim.addNode( dayFourNode.id, tagset.fetchOrAddTag("Crossing that Bridge"))
eventsDim.addNode( dayFourNode.id, tagset.fetchOrAddTag("Wading Thronga"))
eventsDim.addNode( dayFourNode.id, tagset.fetchOrAddTag("Break in the Ash"))


dayFiveNode = eventsDim.addNode( rootNode.id, tagset.fetchOrAddTag("Day 5"))
eventsDim.addNode( dayFiveNode.id, tagset.fetchOrAddTag("The Flower Contest"))
eventsDim.addNode( dayFiveNode.id, tagset.fetchOrAddTag("Football"))
eventsDim.addNode( dayFiveNode.id, tagset.fetchOrAddTag("Climbing Snorri's Kingdom"))
eventsDim.addNode( dayFiveNode.id, tagset.fetchOrAddTag("Riding the Rapids"))
#############################################################################################


#############################################################################################
tagset = AlphanumericalTagSet('People').create()
peopleDim = tagset.createPersistentDimension( tagset.fetchOrAddTag("People") )
rootNode = peopleDim.getRoot()

adultsNode = peopleDim.addNode( rootNode.id, tagset.fetchOrAddTag("Adults"))
peopleDim.addNode( adultsNode.id, tagset.fetchOrAddTag("Magnus Senior"))
peopleDim.addNode( adultsNode.id, tagset.fetchOrAddTag("Margret Senior"))
peopleDim.addNode( adultsNode.id, tagset.fetchOrAddTag("Duddi"))
peopleDim.addNode( adultsNode.id, tagset.fetchOrAddTag("Frida"))
peopleDim.addNode( adultsNode.id, tagset.fetchOrAddTag("Kristinn"))
peopleDim.addNode( adultsNode.id, tagset.fetchOrAddTag("Hrefna"))
peopleDim.addNode( adultsNode.id, tagset.fetchOrAddTag("Asa"))
peopleDim.addNode( adultsNode.id, tagset.fetchOrAddTag("Bjorn"))
peopleDim.addNode( adultsNode.id, tagset.fetchOrAddTag("Dori Truss"))

kidsNode = peopleDim.addNode( rootNode.id, tagset.fetchOrAddTag("Kids"))
peopleDim.addNode( kidsNode.id, tagset.fetchOrAddTag("Magnus Junior"))
peopleDim.addNode( kidsNode.id, tagset.fetchOrAddTag("Margret Junior"))
peopleDim.addNode( kidsNode.id, tagset.fetchOrAddTag("Magnus Dudda"))
peopleDim.addNode( kidsNode.id, tagset.fetchOrAddTag("Katrin"))
peopleDim.addNode( kidsNode.id, tagset.fetchOrAddTag("Jokull"))
peopleDim.addNode( kidsNode.id, tagset.fetchOrAddTag("Johannes"))
peopleDim.addNode( kidsNode.id, tagset.fetchOrAddTag("Solveig"))
peopleDim.addNode( kidsNode.id, tagset.fetchOrAddTag("Asthor"))
peopleDim.addNode( kidsNode.id, tagset.fetchOrAddTag("Kria"))

familyDim = tagset.createPersistentDimension( tagset.fetchOrAddTag("Family") )
rootNode = familyDim.getRoot()
familyDim.addNode( rootNode.id, tagset.fetchOrAddTag("Asa"))
familyDim.addNode( rootNode.id, tagset.fetchOrAddTag("Bjorn"))
familyDim.addNode( rootNode.id, tagset.fetchOrAddTag("Solveig"))
familyDim.addNode( rootNode.id, tagset.fetchOrAddTag("Asthor"))
#############################################################################################+

#############################################################################################
tagset = AlphanumericalTagSet('Animals').create()
animaleDimension = tagset.createPersistentDimension( tagset.fetchOrAddTag("Animals") )
animalsNode = animaleDimension.getRoot()
node = animaleDimension.addNode( animalsNode.id, tagset.fetchOrAddTag("Sheep") )
node = animaleDimension.addNode( animalsNode.id, tagset.fetchOrAddTag("Bird") )
node = animaleDimension.addNode( animalsNode.id, tagset.fetchOrAddTag("Dog") )
node = animaleDimension.addNode( animalsNode.id, tagset.fetchOrAddTag("Fish") )
#############################################################################################


#############################################################################################
tagset = AlphanumericalTagSet('Impression').create()
impressionHir = tagset.createPersistentDimension( tagset.fetchOrAddTag("Impression") )
imperssionNode = impressionHir.getRoot()
node = impressionHir.addNode( imperssionNode.id, tagset.fetchOrAddTag("Beautiful") )
#############################################################################################
