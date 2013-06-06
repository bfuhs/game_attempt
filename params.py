'''
game parameters

'''

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



