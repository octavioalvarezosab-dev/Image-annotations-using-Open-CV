import json
import os

class LabelMeProcessor:
    def __init__(self, json_file):
        self.json_file = json_file
        self.annotations = self.load_json()

    def load_json(self):
        """Load the LabelMe JSON file"""
        try:
            with open(self.json_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise Exception(f"File {self.json_file} not found.")
        except json.JSONDecodeError:
            raise Exception("Error decoding JSON.")

    def get_shapes(self):
        """Extract shapes from the annotations"""
        shapes = self.annotations.get('shapes', [])
        return shapes

    def get_image_info(self):
        """Get image height and width"""
        width = self.annotations.get('imageWidth', 0)
        height = self.annotations.get('imageHeight', 0)
        return width, height

    def save_processed_data(self, output_file):
        """Save extracted shapes to a new JSON file"""
        shapes = self.get_shapes()
        output_data = {'shapes': shapes}
        with open(output_file, 'w') as file:
            json.dump(output_data, file, indent=4)
        print(f"Processed data saved to {output_file}")

# Example usage:
# processor = LabelMeProcessor('path_to_labelme_file.json')
# processor.save_processed_data('processed_output.json')