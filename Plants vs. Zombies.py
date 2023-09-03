import random

class Plant:
    def __init__(self, name, cost, damage):
        self.name = name
        self.cost = cost
        self.damage = damage

class Zombie:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

plants = [
    Plant("向日葵", 20, 0),
    Plant("豌豆射手", 50, 10),
    Plant("坚果墙", 30, 0)
]

zombies = [
    Zombie("普通僵尸", 50, 5),
    Zombie("铁桶僵尸", 100, 10),
    Zombie("飞行僵尸", 40, 8)
]

sun = 100  # 初始阳光
level = 1  # 初始关卡

while sun > 0:
    print(f"关卡: {level}  阳光: {sun}")
    print("可用植物:")
    for i, plant in enumerate(plants):
        print(f"{i + 1}. {plant.name} ({plant.cost}阳光)")

    choice = input("请选择要种植的植物 (1/2/3, 或输入q结束游戏): ")

    if choice == "q":
        break

    try:
        choice = int(choice) - 1
        selected_plant = plants[choice]
        if sun >= selected_plant.cost:
            sun -= selected_plant.cost
            print(f"种植{selected_plant.name}成功！")
        else:
            print("阳光不足，无法种植该植物。")
    except (ValueError, IndexError):
        print("无效的选择，请重新选择。")

    # 模拟僵尸进攻
    if random.random() < 0.3:  # 30%的概率出现僵尸
        selected_zombie = random.choice(zombies)
        print(f"{selected_zombie.name}出现！")
        while selected_zombie.health > 0:
            selected_zombie.health -= selected_plant.damage
            if selected_zombie.health <= 0:
                print(f"{selected_zombie.name}被击败！")
                break
            sun += 10  # 每次攻击获得10阳光
            print(f"{selected_plant.name}对{selected_zombie.name}造成{selected_plant.damage}伤害")
    else:
        print("没有僵尸出现。")

    if sun >= 200:  # 过关条件，可根据需要调整
        level += 1
        sun -= 200
        print(f"恭喜！你通过了第{level - 1}关，进入了第{level}关。")

print("游戏结束！")
