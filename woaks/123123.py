class Fish:
    def __init__(self, fish_weights):
        self.fish_weights = fish_weights

    def average_weight(self):
        avg_weight = round(sum(self.fish_weights) / 5, 2)
        print(f"물고기 평균 무게: {avg_weight:.2f} kg")
    
fish = Fish([2.5, 3.1, 1.7, 2.8, 2.4])
fish.average_weight()