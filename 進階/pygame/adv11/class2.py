# 基本玩家類別
class Player:
    def __init__(self, name, health, attack, defense):
        """初始化玩家, name: 名稱, health: 血量, attack: 攻擊, defense: 防禦"""
        # self的意思是創造一個屬於自己的變數
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        """受到傷害"""
        self.health -= damage - self.defense  # 受到傷害 = 傷害 - 防禦
        return f"{self.name} 受到了 {damage} 點傷害！"


# 法師類別
class Mage(Player):  # 繼承Player類別
    def __init__(self, name, health, attack, defense, magic_power):
        """初始化法師, name: 名稱, health: 血量, attack: 攻擊, defense: 防禦, magic_power: 魔力"""
        super().__init__(name, health, attack, defense)
        self.magic_power = magic_power

    def cast_spell(self):
        """施放魔法"""
        # 消耗魔力，施放魔法攻擊
        self.magic_power -= 10
        return self.attack + self.magic_power


# 戰士類別
class Warrior(Player):  # 繼承Player類別
    def __init__(self, name, health, attack, defense, armor):
        """初始化戰士, name: 名稱, health: 血量, attack: 攻擊, defense: 防禦, armor: 裝甲"""
        super().__init__(name, health, attack, defense)
        self.armor = armor

    def use_armor(self):
        self.health += self.armor
        return f"{self.name} 使用裝甲，增加了 {self.armor} 點體力！"


player1 = Warrior("戰士小明", 100, 15, 10, 5)  # 裡面包含了Player的物件，所以可以使用Player的方法
player2 = Mage("法師小華", 80, 10, 5, 20)

print(f"{player1.name}血量剩餘: {player1.health}")
print(player1.use_armor())
print(f"{player1.name}血量剩餘: {player1.health}")

print(f"{player2.name}目前魔力: {player2.magic_power}")
player1.take_damage(player2.cast_spell())
print(f"{player2.name}對{player1.name}施放魔法攻擊！")
print(f"{player2.name}目前魔力: {player2.magic_power}")
print(f"{player1.name}血量剩餘: {player1.health}")