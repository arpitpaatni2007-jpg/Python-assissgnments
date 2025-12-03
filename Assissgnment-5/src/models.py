class BuildingManager:
    def __init__(self, df, energy_column="kwh", building_column="building"):
        self.df = df
        self.energy_column = energy_column
        self.building_column = building_column

        # Verify the required columns exist
        if self.energy_column not in df.columns:
            raise KeyError(f"Column '{self.energy_column}' not found. Available: {df.columns}")

        if self.building_column not in df.columns:
            raise KeyError(f"Column '{self.building_column}' not found. Available: {df.columns}")

    def total_energy(self):
        return self.df[self.energy_column].sum()

    def top_building(self):
        usage = self.df.groupby(self.building_column)[self.energy_column].sum()
        return usage.idxmax(), usage.max()

    def lowest_building(self):
        usage = self.df.groupby(self.building_column)[self.energy_column].sum()
        return usage.idxmin(), usage.min()
