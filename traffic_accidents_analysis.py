import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    # Remove duplicates
    data = data.drop_duplicates()

    # Ensure all column names are trimmed and consistent
    data.columns = data.columns.str.strip()

    # Standardize string values in categorical columns
    if 'Accident Type' in data.columns:
        data['Accident Type'] = data['Accident Type'].str.strip()
    if 'Road Safety Measures' in data.columns:
        data['Road Safety Measures'] = data['Road Safety Measures'].str.strip()

    return data

def transform_data(data):
    # Severity score: weighted sum of fatalities and injuries
    data['Severity Score'] = data['Fatalities'] * 3 + data['Injuries']

    # Add rate features for fatality and injury
    data['Fatality Rate'] = (data['Fatalities'] / data['Accidents Reported']).fillna(0) * 100
    data['Injury Rate'] = (data['Injuries'] / data['Accidents Reported']).fillna(0) * 100
    return data

def aggregate_data(data):
    aggregated = data.groupby(['Country', 'Year']).agg({
        'Accidents Reported': 'sum',
        'Fatalities': 'sum',
        'Injuries': 'sum',
        'Severity Score': 'mean'
    }).reset_index()
    return aggregated

# Exploratory Data Analysis (EDA)
def perform_eda(data):
    # Accidents reported by year
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x='Year', y='Accidents Reported', hue='Country', marker='o')
    plt.title('Accidents Reported by Year')
    plt.ylabel('Accidents Reported')
    plt.xlabel('Year')
    plt.legend(title='Country')
    plt.tight_layout()
    plt.savefig('eda_accidents_reported.png')
    plt.close()

def visualize_data(data):
    # Generate visualizations for the dataset

    # Total accidents reported by country
    plt.figure(figsize=(10, 6))
    data.groupby('Country')['Accidents Reported'].sum().sort_values().plot(kind='barh')
    plt.title('Total Accidents Reported by Country')
    plt.xlabel('Total Accidents')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.savefig('total_accidents_reported.png')
    plt.close()

    # Average Fatality Rate by Accident Type
    plt.figure(figsize=(10, 6))
    data.groupby('Accident Type')['Fatality Rate'].mean().sort_values().plot(kind='bar', color='orange')
    plt.title('Average Fatality Rate by Accident Type')
    plt.xlabel('Accident Type')
    plt.ylabel('Average Fatality Rate (%)')
    plt.tight_layout()
    plt.savefig('average_fatality_rate.png')
    plt.close()

    # Impact of Road Safety Measures on Fatality Rate
    plt.figure(figsize=(10, 6))
    data.groupby('Road Safety Measures')['Fatality Rate'].mean().sort_values().plot(kind='bar', color='green')
    plt.title('Impact of Road Safety Measures on Fatality Rate')
    plt.xlabel('Road Safety Measures')
    plt.ylabel('Average Fatality Rate (%)')
    plt.tight_layout()
    plt.savefig('impact_road_safety_measures.png')
    plt.close()

def save_data(data, output_path):
    data.to_csv(output_path, index=False)

def run_pipeline(file_path, output_path):
    try:
        print("Loading data...")
        data = load_data(file_path)

        print("Cleaning data...")
        data = clean_data(data)

        print("Transforming data...")
        transformed_data = transform_data(data)

        print("Aggregating data...")
        aggregated = aggregate_data(transformed_data)

        print("Performing EDA...")
        perform_eda(aggregated)

        print("Visualizing data...")
        visualize_data(transformed_data)

        print("Saving processed data...")
        save_data(aggregated, output_path)

        print("Pipeline execution complete.")
    except Exception as e:
        print(f"Error during pipeline execution: {e}")

if __name__ == "__main__":
    input_file = 'traffic_accidents.csv'
    output_file = 'processed_traffic_data.csv'

    run_pipeline(input_file, output_file)