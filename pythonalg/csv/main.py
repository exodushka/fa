import pandas as pd
import numpy as np

# --- Конфигурация ---
# Укажите имя вашего исходного CSV-файла
INPUT_FILE_NAME = 'stock_data.csv'
# Имя файла, в который будут сохранены результаты статистики
OUTPUT_FILE_NAME = 'analysis_results.csv'
# Столбец для анализа цены
PRICE_COLUMN = 'Close'
# Столбец для анализа объема
VOLUME_COLUMN = 'Volume'
# --------------------


def analyze_and_save_data(input_path: str, output_path: str, price_col: str, volume_col: str):
    """
    Читает финансовые данные, вычисляет статистику и сохраняет результаты в CSV-файл.
    """
    print(f"Начинается обработка файла: {input_path}")
    
    try:
        # 1. Чтение данных
        df = pd.read_csv(
            input_path, 
            index_col='Date', 
            parse_dates=True
        )
        print("Данные успешно загружены.")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_path}' не найден.")
        return
    except KeyError as e:
        print(f"Ошибка: Не найден необходимый столбец {e} в файле.")
        return
    except Exception as e:
        print(f"Произошла непредвиденная ошибка при загрузке: {e}")
        return

    # 2. Вычисление статистики
    print("📈 Вычисление статистики...")
    
    # Расчет ежедневной доходности (Return) в процентах
    df['Daily Return (%)'] = df[price_col].pct_change() * 100

    # Создание словаря для сбора всех результатов
    results = {
        'Metric': [],
        'Value': []
    }

    # Статистика цены
    results['Metric'].extend([
        f'Mean {price_col} Price', 
        f'Std Dev {price_col} Price', 
        f'Max {price_col} Price', 
        f'Min {price_col} Price'
    ])
    results['Value'].extend([
        df[price_col].mean(), 
        df[price_col].std(), 
        df[price_col].max(), 
        df[price_col].min()
    ])

    # Статистика объема
    results['Metric'].extend([
        f'Mean {volume_col}', 
        f'Total {volume_col}'
    ])
    results['Value'].extend([
        df[volume_col].mean(), 
        df[volume_col].sum()
    ])

    # Статистика доходности
    results['Metric'].extend([
        'Mean Daily Return (%)', 
        'Std Dev Daily Return (%) (Volatility)',
        'Max Daily Return (%)',
        'Min Daily Return (%)'
    ])
    results['Value'].extend([
        df['Daily Return (%)'].mean(), 
        df['Daily Return (%)'].std(), 
        df['Daily Return (%)'].max(),
        df['Daily Return (%)'].min()
    ])
    
    # 3. Сохранение результатов в CSV-файл
    results_df = pd.DataFrame(results)
    
    try:
        results_df.to_csv(output_path, index=False, float_format='%.4f')
        print(f"Статистика успешно сохранена в файл: {output_path}")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")

if __name__ == "__main__":
    # Запуск функции
    analyze_and_save_data(INPUT_FILE_NAME, OUTPUT_FILE_NAME, PRICE_COLUMN, VOLUME_COLUMN)