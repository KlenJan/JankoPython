class Mother:
    def __init__(self) -> None:
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"



class Father:
    def __init__(self) -> None:
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"


class Child(Mother, Father):
    pass