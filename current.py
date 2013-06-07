'''

A 4X game with time travel

'''

import params

class GameStateStorage(object):
    def __init__(self):
        self.gameStates = {}
    def saveState(self, gameState, now):
        self.gameStates[now] = gameState
    def loadState(self, time):
        return self.gameStates[time]
    def getTimesSaved(self):
        return sorted(self.gameStates.keys()) # sorting necessary?
    def saveGame(self, gameState, now, filename):
        self.saveState(gameState, now)
        ######## WRITE self.gameStates TO FILE #########
    def loadGame(self, filename):
        self.gameStates ######### GET THIS FROM FILE #########
        return loadState(max(self.gameStates.keys()))

class Simulation(object):
    def __init__(self):

        self.width
        self.slantyHeight
        self.grid = {}

    def createGrid(self):
        for i in xrange(self.width):
            for j in xrange(self.slantyHeight):
                self.grid[(i,j)] = Cell(self, (i,j))
        for cell in self.grid.values():
            cell.findNeighbors()


class Player(object):
    def __init__(self, context):
        self.simulation = context

        self.selected = None

        # locations that have been explored before
        self.canSee = {} # coords : visible or fogged
        self.units
        self.buildings

    ################ WORK ON THIS ###############

    def select(self, thingy): # should I be able to select multiple?
        self.selected = thingy

    def deselect(self):
        self.selected = None
        
    def leftClickOn(self, coords): # say these are coords for grid
        if coords in self.canSee and self.canSee[coords]=='visible':
            self.selected = 
        self.selected = self.simulation.grid[coords]
        self.selected.displaySelectionTo(self.playerUI)

    def rightClickOn(self, coords):
        if self.selected == None:
            self.simulation.grid[coords].displayInfoTo(self.playerUI)
        else:
            self.selected.interactWith(coords)




class Cell(object):
    def __init__(self, context, coords):
        self.simulation = context
        self.coords = coords

        self.terrain

        self.units = {}
        self.buildings = {}

        self.neighbors = {}
        
    def findNeighbors(self): # call after all cells instantiated
        '''
        0 = E
        1 = SE
        2 = SW
        3 = W
        4 = NW
        5 = NE        
        '''
        i,j = self.location
        w = self.simulation.width
        self.neighbors[0] = self.simulation.grid[((i+1)%w, j)]
        self.neighbors[3] = self.simulation.grid[((i-1)%w, j)]
        try: self.neighbors[1] = self.simulation.grid[(i, j+1)]
        except: pass # Could make Nones instead
        try: self.neighbors[4] = self.simulation.grid[(i, j-1)]
        except: pass
        try: self.neighbors[2] = self.simulation.grid[((i-1)%w, j-1)]
        except: pass
        try: self.neighbors[5] = self.simulation.grid[((i+1)%w, j+1)]
        except: pass
        
        
    def displaySelectionTo(self, player):
        pass

    def displayInfoTo(self, player):
        pass

class Unit(object):
    
    def __init__(self, context, unitType): # 0, 1, 2
        self.owner = context
        self.unitType = unitType
        self.typeName = params.units[unitType]
        self.HP = params.unitInfo[unitType]['hitpoints']
        self.attackPower = params.unitInfo[unitType]['attackPower']
        self.attackRange = params.unitInfo[unitType]['attackRange']
        self.terrainEffect = {}
        allTerrainEffects = params.terrainEffect
        for uType, terrain in allTerrainEffects:
            if uType == self.unitType:
                self.terrainEffect[terrain] = allTerrainEffects[(uType, terrain)]

        self.location ##### a cell with coords and terrain attributes
        self.terrain   #########
        self.visibleLocations = {} # cell: distance

    def attack(self, defendingUnit):
        SOMETHING = defendingUnit.defend

    def defend(self, attackingUnit):
        pass

    def moveTo(self, coords):
        pass

    def moveDirection(self, direction):
        # update location and terrain and sightCoords and total player sight

        # after moving,
        self.updateSight()

    def updateSight(self): # call when moving
        baseRadius = params.terrainInfo[self.terrain]['sightRadius']

        # tell old visible locations not to show to the player
        for location in self.visibleLocations:
            

        # replace old visible locations with new visible locations

        # tell new visible locations to show to player
        
        for i in xrange(baseRadius):
            for location in self.visibleLocations:
                self.visibleLocations.update
        
        

