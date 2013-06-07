'''
game parameters

'''

import random as rnd

### numbers to names

terrain = { 0: 'grass',
            1: 'forest',
            2: 'rock' }
            3: 'water' } # water is an obstacle

# healer is good in forest, archer is good on rock, footman is good in fields
# archer is worst in forest, footman is worst on rock, healer is worst in fields
units = { 0: 'healer',
          1: 'archer',
          2: 'soldier' }

# I don't really need to use resources
resources = { 0: 'sunflower',
              1: 'treewood',
              2: 'stonemetal' }

# each resource building (0-2) gradually depletes the underlying resource
buildings = { 0: 'sungarden',
              1: 'lumbery', 
              2: 'quarryforge',
              3: 'tower',
              4: 'trap', 
              5: 'wallfort' } 
# Tower:
#  built on grass by archer with lumber, consumes an archer and requires another to man
#  manned by archer, provides ranged support
#  most vulnerable to soldier, slightly vulnerable to archers, not vulnerable to healers
# Wallfort:
#  built on rocks with stonemetal by soldiers, convertable from quarryforge
#  manned by anybody, but archers can actually defend it
#  not really destroyable except by converting to quarryforge
# Trap:
#  built in forest by healers from nothing much
#  when manned by nobody, disappears enemy units with some probability
#  when manned by a healer, scouts countryside and is completely undetectable
#  when manned by others, can be an ambush thingy?
#  detectable only by healers walking over it when another healer isn't in it

# unit : hitpoints, attack strength, attack range
unitInfo = { 0: {'hitpoints': 1, 'attackPower': -1, 'attackRange': 1},
             1: {'hitpoints': 2, 'attackPower': 2, 'attackRange': 2},
             2: {'hitpoints': 3, 'attackPower': 2, 'attackRange': 1} }

# terrain effect by (unit type, terrain type)
#  I could write this as a function instead
terrainEffect = { (0,0): 0, (0,1): 2, (0,2): 1,
                  (1,0): 1, (1,1): 0, (1,2): 2,
                  (2,0): 2, (2,1): 1, (2,2): 0 }
                  
terrainInfo = { 0: {'allowedBuildings': [0, 3], 'sightRadius': 2 },
                1: {'allowedBuildings': [1, 4], 'sightRadius': 1},
                2: {'allowedBuildings': [2, 5], 'sightRadius': 3},}

# building: attributes
buildingInfo = { 0: {'hitpoints': 2, 'attackPower': 0, 'attackRange': 0},
                 1: {'hitpoints': 3, 'attackPower': 0, 'attackRange': 0},
                 2: {'hitpoints': 4, 'attackPower': 0, 'attackRange': 0},
                 3: {'hitpoints': 4, 'attackPower': 0, 'attackRange': 3}, #
                 4: {'hitpoints': 0, 'attackPower': 0, 'attackRange': 0}, #
                 5: {'hitpoints': 6, 'attackPower': 0, 'attackRange': 2} }#


### Terrain generator
# First, randomize equally all terrain types
# Then implement Schelling model with some parameter
# Also need to ensure that water isn't blocking anything
#  Or just ensure that players are on a connected piece of land
def generateTerrain(cellList, uniformity=0.5):
    
    numCells = len(cellList)
    happyDict = {}
    terrainTypesWithSpace = [-1, 0, 1, 2, 3] # -1 being none for now
    terrainTypes = [0, 1, 2, 3]
    for cell in cellList: # randomize terrain with some space
        cell.terrain = rnd.choice(terrainTypesWithSpace)

    def getHappiness(cell):
        if cell.terrain == -1
            return None
        neighborTerrains = [neighbor.terrain for neighbor in cell.neighbors.values()]
        numTerrainedNeighbors = len(neighborTerrains) - neighborTerrains.count(-1)
        
        if neighborTerrains.count(cell.terrain) / numTerrainedNeighbors >= uniformity:
            return 1 # happy
        else:
            return -1 # unhappy
    
    for cell in cellList: # set happiness for everybody
        happyDict[cell] = getHappiness(cell)

    maxAveTimeChecked = 1000
    for i in xrange(numCells * maxAveTimeChecked):

        rnd.shuffle(cellList) # not sure if necessary

        unhappyCells = [cell for cell in cellList if happyDict[cell] == -1]
        if len(unhappyCells) == 0: # leave loop if all satisfied
            continue

        for cell in unhappyCells: # swap terrain in unhapy cells for blank cells
            for i in xrange(10000): # didn't want "while True"
                targetCell = rnd.choice(cellList)
                if targetCell.terrain == -1:
                    targetCell.terrain = cell.terrain
                    cell.terrain = -1
                    # update happiness
                    happyDict[targetCell] = getHappy(targetCell)
                    happyDict[cell] = None
                    break # continue onto next unhappy cell

    # Now I need to fill in the blanks with majority of neighbor terrains
    for i in xrange(numCells * maxAveTimeChecked):
        emptyCells = [cell for cell in cellList if cell.terrain == -1]
        if len(emptyCells) == 0: # leave loop if no empty cells
            continue
        for cell in emptyCells:
            neighborTerrains = [neighbor.terrain for neighbor in cell.neighbors.values()]
            terrainCounts = [neighborTerrains.count(i) for i in terrainTypes]
            if sum(terrainCounts[1:]) == 0: # No terrained neighbors
                continue # till next time!
            maxTerrains = []
            maxValue = max(terrainCounts)
            for terrain, countie in enumerate(terrainCounts):
                if countie == maxValue:
                    maxTerrains.append(terrain)
            cell.terrain = rnd.choice(maxTerrains)
    else:
        raise Exception("Can't get rid of empties")
