from etl.loader import load_all_sources, save_all_outputs
from etl.transformer import DiceGameTransformer
from etl.insights import generate_insights

def main():
    # Load
    data = load_all_sources()

    # Transform
    transformer = DiceGameTransformer(data)
    output = transformer.transform_all()

    # Save
    save_all_outputs(output)

    # Analyze
    generate_insights(output)

if __name__ == "__main__":
    main()
