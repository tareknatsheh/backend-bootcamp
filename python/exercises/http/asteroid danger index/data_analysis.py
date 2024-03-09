class DataHandler:
    def __init__(self, raw_data: dict) -> None:
        self.raw_data = raw_data
        self.clean_data = self.__clean_asteroid_data()
        self.asteroid_names_list, self.min_diameter_list, self.relative_velocity_list, self.miss_distance_list, self.max_diameter_list = self.__get_x_y_lists()
        # self.danger_indices = self.get_danger_indices(1, 1, 1)
        pass
    
    def __clean_asteroid_data(self) -> list:
        """Takes a dict with all original kvps from the source API
        returns a clean list of dicts for each asteroid.
        """
        clean_asteroid_list = []
        for day in self.raw_data:
            asteroids_list = self.raw_data[day]
            for asteroid in asteroids_list:
                # id name ["estimated_diameter"]["kilometers"]["estimated_diameter_min"]/["estimated_diameter_max"]
                clean_asteroid_list.append({
                    "id": asteroid["id"],
                    "name": asteroid["name"],
                    "estimated_diameter_min": asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_min"],
                    "estimated_diameter_max": asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
                    "miss_distance": asteroid["close_approach_data"][0]["miss_distance"]["kilometers"],
                    "relative_velocity": asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"]
                })
        return clean_asteroid_list

    def __get_x_y_lists(self) -> tuple[list, list, list, list, list]:
        """Get all asteroid needed paramters as lists to be used in the plots"""
        ast_name = []
        est_dia_min = []
        rel_vel = []
        miss_dist = []
        est_dia_max = []

        # Will generate all x and y axes at once to avoid calling a for loop
        # too often
        for asteroid in self.clean_data:
            ast_name.append(asteroid["name"])
            est_dia_min.append(float(asteroid["estimated_diameter_min"]))
            rel_vel.append(float(asteroid["relative_velocity"]))
            miss_dist.append(float(asteroid["miss_distance"]))
            est_dia_max.append(float(asteroid["estimated_diameter_max"]))
        return ast_name, est_dia_min, rel_vel, miss_dist, est_dia_max

    def get_danger_indices(self, A: float, B: float, C: float) -> list:
        """Calculate the danger index of each asteroid
        Note: There is no average diameter in the data, so I'll just use the max"""
        if len(self.max_diameter_list) == len(self.relative_velocity_list) == len(self.miss_distance_list):
            danger_ind_list = [A*diameter + B*speed + (1/C)*dist for diameter, speed, dist in zip(self.max_diameter_list, self.relative_velocity_list, self.miss_distance_list)]
            # print(f"dia: {self.max_diameter_list[0]}")
            # print(f"spd: {self.relative_velocity_list[0]}")
            # print(f"miss: {self.miss_distance_list[0]}")
            # print(f"calc: {danger_ind_list[0]} should: {A*self.max_diameter_list[0] + B*self.relative_velocity_list[0] + (1/C)*self.miss_distance_list[0]}")
            return danger_ind_list
        else:
            raise Exception("Error: all lists should have the same size")
