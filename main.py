from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    data = extract_data()
    
    if not data:
        print("No data extracted")
        return

    clean_data = transform_data(data)
    load_data(clean_data)

    print("Pipeline executed successfully")

if __name__ == "__main__":
    run_pipeline()