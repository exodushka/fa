class Map:
    def __init__(self, map=None):
        if map is None:
            self.map = {
                "A1": "R",
                "A2": "P",
                "A3": ".",
                "A4": ".",
                "A5": ".",
                "A6": ".",
                "A7": "p",
                "A8": "r",
                "B1": "N",
                "B2": "P",
                "B3": ".",
                "B4": ".",
                "B5": ".",
                "B6": ".",
                "B7": "p",
                "B8": "n",
                "C1": "B",
                "C2": "P",
                "C3": ".",
                "C4": ".",
                "C5": ".",
                "C6": ".",
                "C7": "p",
                "C8": "b",
                "D1": "Q",
                "D2": "P",
                "D3": ".",
                "D4": ".",
                "D5": ".",
                "D6": ".",
                "D7": "p",
                "D8": "q",
                "E1": "K",
                "E2": "P",
                "E3": ".",
                "E4": ".",
                "E5": ".",
                "E6": ".",
                "E7": "p",
                "E8": "k",
                "F1": "B",
                "F2": "P",
                "F3": ".",
                "F4": ".",
                "F5": ".",
                "F6": ".",
                "F7": "p",
                "F8": "b",
                "G1": "N",
                "G2": "P",
                "G3": ".",
                "G4": ".",
                "G5": ".",
                "G6": ".",
                "G7": "p",
                "G8": "n",
                "H1": "R",
                "H2": "P",
                "H3": ".",
                "H4": ".",
                "H5": ".",
                "H6": ".",
                "H7": "p",
                "H8": "r",
            }
        else:
            self.map = map
    
    def map_print(self):
        print("\n" * 50)
        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        print("  A B C D E F G H")
        for i in range(8):
            print(f"{8 - i} ", end="")
            for j in letters:
                print(f"{self.map[j + str(8 - i)]} ", end="")
            print(f"{8 - i}")
        print("  A B C D E F G H")

class Game:
    def __init__(self, map=None):
        self.map = Map(map)
    
    def check_move(self, move):
        ...

def main():
    ...
if __name__ == "__main__":
    main()