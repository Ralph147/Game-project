import random
Damage = 2
Heal = 4
Level = 1
Health = (Level*10)+30
Name = input("Name: ")
r = 0
i = 3
x = 1
#################################################################################
print("Class Options:      1:Warrior")
print("                    2:Paladin")
print("                    3:Druid")
print("                    4:Hunter")
while True:
    classChoice = input("Class choice: ")
    if classChoice == '1':
        className = 'Warrior'
        break
    elif classChoice == '2':
        className = 'Paladin'
        break
    elif classChoice == '3':
        className = 'Druid'
        break
    elif classChoice == '4':
        className = 'Hunter'
        break
    else:
        print("Please choose option 1,2,3 or 4")
#################################################################################
print("Race Options:       1:Human")
print("                    2:Orc")
print("                    3:Naga")
print("                    4:Aviar")
raceChoice = input("Race choice: ")
if raceChoice == '1':
    raceChoice = 'Human'
    Heal + 2
elif raceChoice == '2':
    raceChoice = 'Orc'
    Damage =+ 2
elif raceChoice == '3':
    raceChoice = 'Naga'
    Health =+ 2
elif raceChoice == '4':
    raceChoice = 'Aviar'
    Level =+ 1
else:
    print("Please choose option 1,2,3 or 4")

#################################################################################    
if className == 'Warrior':
    print("One handed")
    print("Two handed")
    Damage = Damage + 1
    
elif className == 'Paladin':
    print("One handed")
    print("Two handed")
    print("Magic")
    Heal = Heal + 1
    
elif className == 'Druid':
    print("One handed")
    print("Magic")
    Health = Health + 1
    
elif className == 'Hunter':
    print("One Handed")
    print("Ranged")
    Level = Level + 1
    
while True:   
    weaponType = input("Please enter what class of weapon you would like to use: ")
    if weaponType == "One handed" or weaponType == "one handed":
        weaponType = 1
        print("Sword")
        print("Dagger")
        print("Torch")
        break
    elif weaponType == "Two handed" or weaponType == "two handed":
        weaponType = 2
        print("LongSword")
        print("BattleAxe")
        print("Spear")
        break
    elif weaponType == "Ranged" or weaponType == "ranged":
        weaponType = 3
        print("Gun")
        print("Crossbow")
        print("Long Bow")
        break
    elif weaponType == "Magic" or weaponType == "magic":
        weaponType = 4
        print("Nature")
        print("Holy")
        print("Enhancement")
        break
    elif weaponType == '0':
        weaponType = 0
        print("Scyth")
        break
    else:
        print("Please enter one of the choices above")


#################################################################################
while True:
    Weapon = input("Enter your weapon choice: ")
    if weaponType == 1 and Weapon == 'Sword':
        Damage = Damage + random.randint(3,6)
        break
    elif weaponType == 1 and Weapon == 'Dagger':
        Damage = Damage + random.randint(1,5)
        break
    elif weaponType == 1 and Weapon == 'Torch':
        Damage = Damage + random.randint(0,4)
        break
    elif weaponType == 2 and Weapon == 'LongSword':
        Damage = Damage + random.randint(6,7)
        break
    elif weaponType == 2 and Weapon == 'BattleAxe':
        Damage = Damage + random.randint(5,6)
        break
    elif weaponType == 2 and Weapon == 'Spear':
        Damage = Damage + random.randint(5,6)
        break
    elif weaponType == 3 and Weapon == 'Gun':
        Damage = Damage + random.randint(4,6)
        break
    elif weaponType == 3 and Weapon == 'Crossbow':
        Damage = Damage + random.randint(5,6)
        break
    elif weaponType == 3 and Weapon == 'Long Bow':
        Damage = Damage + random.randint(3,5)
        break
    elif weaponType == 4 and Weapon == 'Holy':
        Damage = Damage + random.randint(2,3)
        Heal = Heal + 3
        break
    elif weaponType == 4 and Weapon == 'Nature':
        Damage = Damage + random.randint(2,4)
        Heal = Heal + 2
        break
    elif weaponType == 4 and Weapon == 'Enhancement':
        Damage = Damage + random.randint(2,3)
        Health = Health + 10
        break
    elif weaponType == 0 and Weapon == 'Scyth':
        Damage = 100
        Heal = 100
        break
    else:
        print("Please enter one of the choices above")
        r = r+1
        if r >= 3:
            print("Remember that you have to enter the choice exactly as it is written above")
#################################################################################

class Character:
    def __init__(self, Name, className, raceName, Weapon, Level, Damage, Health, Heal):
        self._Name = Name
        self._Race = raceName
        self._Class = className
        self._Weapon = Weapon
        self._Level = Level
        self._Damage = int(Damage)
        self._Health = Health
        self._Heal = Heal

    def setName(self, Name):
        self._Name = Name
    def getName(self):
        return self._Name
    
    def setClass(self, className):
        self._Class = className
    def getClass(self):
        return self._Class
    
    def setRace(self, raceName):
        self._Race = raceName
    def getRace(self):
        return self._Race
    
    def setWeapon(self, Weapon):
        self._Weapon = Weapon
    def getWeapon(self):
        return self._Weapon
    
    def setLevel(self,Level):
        self._Level = Level
    def getLevel(self):
        return self._Level
    
    def setDamage(self, Damage):
        self._Damage = Damage
    def getDamage(self):
        return self._Damage
    
    def setHealth(self, Health):
        self._Health = Health   
    def getHealth(self):
        return self._Health
    
    def setHeal(self,Heal):
        self._Heal = Heal    
    def getHeal(self):
        return self._Heal

class Race:
    def __init__(self,raceChoice):
        self._Race = raceChoice
    def setRace(self,raceChoice):
        self._Race = raceChoice
    def getRace(self):
        return self._Race

class Class:
    def __init__(self,classChoice):
        self._Class = classChoice
    def setClass(self,classChoice):
        self._Class = classChoice
    def getClass(self):
        return self._Class

class Weapon:
    def __init__(self,Weapon):
        self._Weapon = Weapon
    def setWeapon(self,Weapon):
        self._Weapon = Weapon
    
class Enemy:
    def __init__(self, enemy, enLevel, enhealth, enDamage):
        self._enemy = ''
        self._enLevel = ''
        self._enHealth = ''
        self._enDamage = ''

    def setEnemy(self,enemy):
        self._enemy = enemy

    def getEnemy(self):
        return self._enemy

    def setEnhealth(self,enHealth):
        self._enHealth = enHealth

    def getEnhealth(self):
        return self._enHealth

    def setEnlevel(self,enLevel):
        self._enLevel = enLevel

    def getEnlevel(self):
        return self._enLevel

    def setEndamage(self,enDamage):
        self._enDamage = enDamage

    def getEndamage(self):
        return self._enDamage




raceInfo = Race(raceChoice)
classInfo = Class(className)
weaponInfo = Weapon(Weapon)
Player = Character(Name,raceInfo.getRace(),classInfo.getClass(),Weapon,Level,Damage,Health,Heal)
def Stats():
    print("##############################")
    print("##        STATS             ##")
    print("##############################")
    print("Name: ",Player.getName(),"The",Player.getRace(),Player.getClass())
    print("Damage: ",Player.getDamage())
    print("Health: ",Player.getHealth())
    if Player.getLevel() < 10:
        print("Level: ",Player.getLevel())
    else:
        print("Level: Max")
    print()
    print("Enemy: ", Attacker.getEnemy())
    print("Damage: ", Attacker.getEndamage())
    print("Health: ", Attacker.getEnhealth())
    print("Level: ", Attacker.getEnlevel())
    print()   



replay = True
while replay == True:
    if Player.getLevel() == 10:
        enemy = "Ragnaros, Bringer of the end"
        enLevel = 100
        enHealth = 150
        enDamage = (x//2)
    else:
        pick = random.randint(1,4)
        if pick == 1:
            enemy = "Demon"
            enLevel = random.randint(Player.getLevel(),(Player.getLevel()+2))
            enHealth = (enLevel*5)+20
            enDamage = int(enLevel*2.5)+3
            if enDamage >= 15:
                enDamage = 15
        elif pick == 2:
            enemy = "Goblin"
            enLevel = random.randint(Player.getLevel(),(Player.getLevel()+2))
            enHealth = (enLevel*2)+15
            enDamage = int(enLevel*2.5)
        elif pick == 3:
            enemy = "Corrupt"
            enLevel = random.randint(Player.getLevel(),(Player.getLevel()+2))
            enHealth = (enLevel*2)+20
            enDamage = int(enLevel*1.5)+5
        elif pick == 4:
            enemy = "Dragonkin"
            enLevel = random.randint(Player.getLevel(),(Player.getLevel()+2))
            enHealth = (enLevel*5)+30
            enDamage = int(enLevel*2)+3
            if enDamage >= 15:
                enDamage = 15
    Attacker = Enemy(enemy,enDamage,enHealth,enLevel)
    Stats()
    encounter = True
    
    while encounter == True:
        print("ROUND",x)
        print("Options:")
        print("        1:Attack")
        print("        2:Defend")
        print("        3:Heal")
        print("        4:Run")
        print("        5:Stats")
        print("        6:Quit")
        Action = input("Choose an option: ")
#################################################################################
        if Action == '1':
            print()
            remEnHealth = (Attacker.getEnhealth() - Player.getDamage())
            if remEnHealth <= 0:
                remEnHealth = 0
            Attacker.setEnhealth(remEnHealth)
            print("Enemy Health:", Attacker.getEnhealth())
            if remEnHealth <= 0:
                if Attacker.getEnemy() == 'Ragnaros, Bringer of the end':
                    print("You Defeat Ragnaros, and have brought peace to the land Congratulations!!")
                    encounter = False
                    replay = False
                    break
                else:
                    print("You won the fight and carry on")
                if Level < 10:
                    Level = Level+1
                    print("LEVEL UP")
                    print("You gain +10 Health")
                    if Player.getLevel() == i :
                        print("you gain +1 Damage")
                        Damage = Damage + 1
                        Player.setDamage(Damage)
                        i = i+3
                Player.setLevel(Level)
                Health = (Level*13)+20
                Player.setHealth(Health)
                print()
                break
            remChrHealth = (Player.getHealth() - Attacker.getEndamage())
            if remChrHealth < 0:
                remChrHealth = 0
            Player.setHealth(remChrHealth)
            print(Player.getName(),"Health:", Player.getHealth())
            if remChrHealth <= 0:
                print("Game Over")
                replay = False
                encounter = False
                break
                pause = input("")
            x = x+1
            print()

#################################################################################                
        elif Action == '2':
            print()
            remEnHealth = (Attacker.getEnhealth() - int(Player.getDamage()*0.5))
            Attacker.setEnhealth(remEnHealth)
            print("Enemy Health:", Attacker.getEnhealth())
            if remEnHealth <= 0:
                print("You won")
                print("LEVEL UP")
                if Attacker.getEnemy() == 'Ragnaros, Bringer of the end':
                    print(Player.getName()," defeated Ragnaros, and brought peace to the land. Congratulations!!")
                    encounter = False
                    replay = False
                    break
                if Level < 10:
                    Level = Level+1
                    print("LEVEL UP")
                    print("You gain +10 Health")
                    if Player.getLevel() == i :
                        print("You gain +1 Damage")
                        Damage = Damage + 1
                        Player.setDamage(Damage)
                        i = i+3
                Player.setLevel(Level)
                Health = (Level*10)+30
                Player.setHealth(Health)
                print()
                break
            remChrHealth = (Player.getHealth() - int(Attacker.getEndamage()*0.5))
            if remChrHealth < 0:
                remChrHealth = 0
            Player.setHealth(remChrHealth)
            print(Player.getName(),"Health:", Player.getHealth())
            if remChrHealth <= 0:
                print("Game Over")
                replay = False
                encounter = False
                break
            x = x+1
            print()
#################################################################################        


        elif Action == '3':
            print()
            print("Enemy Health:", Attacker.getEnhealth())
            Chance = random.randint(1,6)
            if Chance <= 2:
                print("While healing",Player.getName(),"was struck by the",Attacker.getEnemy())
                remChrHealth = (Player.getHealth() - Attacker.getEndamage())
                if remChrHealth <= 0:
                    print("Game Over")
                    encounter = False
                    replay = False
                    break
            else:
                print("The",Attacker.getEnemy(),"tried to attack you, but missed")
                strHeal = random.randint(1,Player.getHeal())
                remChrHealth = (Player.getHealth() + strHeal)
            Player.setHealth(remChrHealth)
            print(Player.getName(),"was healed by:", strHeal)
            print(Player.getName(),"Health:", Player.getHealth())
            x = x+1
            print()

            
#################################################################################        
        elif Action == '4':
            Chance = random.randint(1,6)
            if Chance >= 5:
                print("You got away")
                encounter = False
            else:
                print("You attempted to escape, but failed and are hit by the enemy")
                remChrHealth = (Player.getHealth() - Attacker.getEndamage())
                if remChrHealth <= 0:
                    print("Game Over")
                    replay = False
                    encounter = False
                    break
                Player.setHealth(remChrHealth)
                print("Enemy Health:", Attacker.getEnhealth())
                print(Player.getName(),"Health:", Player.getHealth())
                
            print()
        elif Action == '5':
            print()
            Stats()
        elif Action == '6':
            print("Game Over")
            replay = False
            encounter = False
            break
        
#################################################################################        
        else:
            print("Please choose option 1, 2, 3, 4, 5 or 6")
#################################################################################

