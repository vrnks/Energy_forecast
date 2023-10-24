# Energy_forecast
Forecasting electricity production. Solving a number of practical tasks: preparing input data on electricity generation, developing software modules, visualizing and interpreting the forecast results for 2023. Historical data by month for 2019-2022, saved in a text file, are used as input data.

This code performs a forecast of electricity production for 2023 based on historical data and uses the SARIMA (Seasonal AutoRegressive Integrated Moving Average) model. The algorithm of the code:

Import the necessary libraries, such as pandas, matplotlib, statsmodels.tsa.seasonal, and statsmodels.tsa.statespace.sarimax.

The EnergyForecast class is created, which contains methods for loading data, splitting data, training the model, creating a forecast, and plotting.

The __init__ method of the EnergyForecast class initializes an object with the parameters data_file (the name of the file with historical data) and output_file (the name of the file to save the forecast).

The load_data method loads data from the data_file, creates a DataFrame, and converts the date to the correct format.

The decompose_data method splits the data into trend, seasonality, and noise using the seasonal_decompose function from the statsmodels.tsa.seasonal library.

The train_model method trains a SARIMA model with the optimal parameters specified in the SARIMAX method from the statsmodels.tsa.statespace.sarimax library.

The make_forecast method predicts electricity generation for 2023 using the trained model. The forecast is stored in the self.forecast variable and written to the output_file you specify.
The plot_data method plots historical data (2019-2022) and a forecast for 2023. The matplotlib library is used for this purpose.

The main function specifies the file names for the input data (data_file) and the output forecast (output_file).

A forecast_model object of the EnergyForecast class is created, and methods are called to load data, split data, train the model, create a forecast, and plot.

The last line specifies that the code is executed only when the file is directly run and calls the main function.

This code loads and analyzes historical data on electricity production, trains the SARIMA model, and makes a forecast for the next year. The result of the forecast is displayed on a graph and is also saved in the file.

Цей код виконує прогноз виробництва електроенергії на 2023 рік на основі історичних даних та використовує модель SARIMA (Seasonal AutoRegressive Integrated Moving Average). Алгоритм роботи коду:

Імпортується необхідні бібліотеки, такі як pandas, matplotlib, statsmodels.tsa.seasonal та statsmodels.tsa.statespace.sarimax.

Створюється клас EnergyForecast, який містить методи для завантаження даних, розбиття даних, навчання моделі, створення прогнозу та побудови графіку.

У методі __init__ класу EnergyForecast ініціалізується об'єкт з параметрами data_file (ім'я файлу з історичними даними) та output_file (ім'я файлу для збереження прогнозу).

Метод load_data завантажує дані з файлу data_file, створює DataFrame та перетворює дату у правильний формат.

Метод decompose_data розбиває дані на тренд, сезонність та шум за допомогою функції seasonal_decompose з бібліотеки statsmodels.tsa.seasonal.

Метод train_model навчає модель SARIMA з оптимальними параметрами, вказаними у методі SARIMAX з бібліотеки statsmodels.tsa.statespace.sarimax.

Метод make_forecast прогнозує виробництво електроенергії на 2023 рік за допомогою навченої моделі. Прогноз зберігається у змінній self.forecast, а також записується у вказаний вами файл output_file.
Метод plot_data побудовує графік історичних даних (2019-2022 рр.) та прогнозу на 2023 рік. Для цього використовується бібліотека matplotlib.

У функції main вказуються імена файлів для вхідних даних (data_file) та вихідного прогнозу (output_file).

Створюється об'єкт forecast_model класу EnergyForecast, і викликаються методи для завантаження даних, розбиття даних, навчання моделі, створення прогнозу та побудови графіку.

Останній рядок визначає, що код виконується лише при безпосередньому запуску файла, і викликає функцію main.

Цей код завантажує і аналізує історичні дані щодо виробництва електроенергії, навчає модель SARIMA та робить прогноз на наступний рік. Результат прогнозу виводиться на графіку, і також зберігається в файлі.
