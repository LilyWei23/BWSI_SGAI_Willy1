class DataCollector:    

    hospital = False
    zombies_killed = 0
    zombies_cured = 0
    zombies_cured_in_hospital = 0
    human_vaccinated = 0
    humans_remaining = 0
    humans_infected = 0
    turns_taken = 0
    
    @staticmethod
    def reset_data():
        DataCollector.zombies_killed = 0
        DataCollector.zombies_cured = 0
        DataCollector.zombies_cured_in_hospital = 0
        DataCollector.humans_vaccinated = 0
        DataCollector.humans_remaining = 0
        DataCollector.humans_infected = 0
        DataCollector.turns_taken = 0

    @staticmethod
    def save_player_data():
        with open("previous_game_data.txt", "w") as f:
            lines = [
                "Has hospital: " + str(DataCollector.hospital) + "\n",
                "Zombies killed: " + str(DataCollector.zombies_killed) + "\n",
                "Zombies cured: " + str(DataCollector.zombies_cured) + "\n",
                "Zombies cured in hospital: " + str(DataCollector.zombies_cured_in_hospital) + "\n",
                "Humans vaccinated: " + str(DataCollector.humans_vaccinated) + "\n",
                "Humans remaining: " + str(DataCollector.humans_remaining) + "\n",
                "Humans infected: " + str(DataCollector.humans_infected) + "\n",
                "Number of turns taken: " + str(DataCollector.turns_taken) + "\n"
            ]
            f.writelines(lines)

    @staticmethod
    def save_ai_data():
        pass
