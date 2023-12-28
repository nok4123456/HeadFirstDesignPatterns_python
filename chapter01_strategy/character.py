class Character:
    def __init__(self) -> None:
        self._weapon_behavior = None

    @property
    def weapon_behavior(self):
        return self._weapon_behavior

    @weapon_behavior.setter
    def weapon_behavior(self, weapon_behavior):
        self._weapon_behavior = weapon_behavior

    def fight(self):
        self.weapon_behavior.use_weapon()


class WeaponBehavior:
    def use_weapon():
        raise NotImplementedError


class SwordBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Sword Attack")


class AxeBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Axe Attack")


class King(Character):
    def __init__(self) -> None:
        self.weapon_behavior = SwordBehavior()


def main():
    king = King()
    king.fight()
    king.weapon_behavior = AxeBehavior()
    king.fight()


if __name__ == "__main__":
    main()
