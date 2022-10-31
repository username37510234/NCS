class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다 [속도 {2}]".format(self.name,location,self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self,name,hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1}방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name,location,self.damage))

    def damaged(self, damage):
        print("{0} : {1}데미지를 입었습니다.".format(self.name,damage))
        self.hp-=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(self.name,location,self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, flying_speed)
        Flyable.__init__(self,flying_speed)

    def move(self,location):
        print("[공중 유닛 이동]")
        self.fly(location)

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0)
        self.location = location
        
        
marine1 = AttackUnit("마린",40,5,2)
marine2 = AttackUnit("마린",40,5,2)
tank = AttackUnit("탱크",150,35,2)
marine3 = AttackUnit("마린",40,5,2)

wraith1 = AttackUnit("레이스",80,5,10)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))

wraith2 = AttackUnit("빼앗은 레이스",80,5,8)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name,wraith2.damage))

firebat1 = AttackUnit("파이어뱃",50,16,2)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)

valkyrie1 = FlyableAttackUnit("발키리",200,6,5)
valkyrie1.fly("3시")

vulture1 = AttackUnit("벌쳐",80,10,10)

battlecruiser1 = FlyableAttackUnit("배틀크루저",500,25,3)

vulture1.move("11시")
battlecruiser1.move("9시")

supply_depot = BuildingUnit("서플라이 디폿",500,"7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()