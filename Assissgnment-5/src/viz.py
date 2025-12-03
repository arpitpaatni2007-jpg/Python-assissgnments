import matplotlib.pyplot as plt

def plot_usage(df, save_path="../outputs/energy_usage.png"):
    """
    Plots total energy consumption over time.
    """
    try:
        daily = df.groupby("Date")["Energy_kWh"].sum()

        plt.figure(figsize=(12,6))
        plt.plot(daily.index, daily.values, marker='o')

        plt.xlabel("Date")
        plt.ylabel("Energy (kWh)")
        plt.title("Daily Energy Usage")
        plt.grid(True)

        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

        print(f"Plot saved: {save_path}")
    except Exception as e:
        print("Plotting error:", e)
