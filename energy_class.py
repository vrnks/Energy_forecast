import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX


class EnergyForecast:
    def __init__(self, data_file, output_file):
        self.data_file = data_file
        self.output_file = output_file
        self.data = None
        self.model = None

    def load_data(self):
        # Зчитуємо дані з файлу та створюємо DataFrame
        self.data = pd.read_csv(
            self.data_file, delimiter="-", header=None, names=["date", "production"]
        )
        self.data["date"] = pd.to_datetime(self.data["date"], format="%d.%m.%Y")
        self.data = self.data.set_index("date")
        self.data["month"] = self.data.index.month
        self.data["year"] = self.data.index.year

    def decompose_data(self):
        # Розбиваємо дані на тренд, сезонність та шум
        decomp = seasonal_decompose(self.data["production"], period=12)

    def train_model(self):
        # Створюємо SARIMA модель з оптимальними параметрами
        self.model = SARIMAX(
            self.data["production"], order=(2, 1, 2), seasonal_order=(2, 1, 0, 12)
        ).fit()

    def make_forecast(self):
        # Прогнозуємо виробництво електроенергії на 2023 рік
        self.forecast = self.model.forecast(steps=12)

        # Зберігаємо прогнозовані дані у файл
        with open(self.output_file, "w") as file:
            for i, value in enumerate(self.forecast):
                date = pd.to_datetime("2023-{}-01".format(i + 1)).strftime("%d.%m.%Y")
                file.write("{}-{}\n".format(date, value))

    def plot_data(self):
        # Робимо графік
        plt.title(
            "Виробництво електроенерії в Україні за 2019-2022 рр. та прогноз на 2023 р."
        )
        plt.xlabel("Роки")
        plt.ylabel("Вироблено електроенергії, млн кВат")
        plt.grid()
        plt.plot(self.data["production"][:12], label="2019")
        plt.plot(self.data["production"][12:24], label="2020")
        plt.plot(self.data["production"][24:36], label="2021")
        plt.plot(self.data["production"][36:48], label="2022")
        plt.plot(self.forecast, label="2023", linestyle="dashed")
        plt.legend()
        plt.show()


def main():
    data_file = "data.txt"
    output_file = "forecast.txt"

    forecast_model = EnergyForecast(data_file, output_file)
    forecast_model.load_data()
    forecast_model.decompose_data()
    forecast_model.train_model()
    forecast_model.make_forecast()
    forecast_model.plot_data()


if __name__ == "__main__":
    main()
