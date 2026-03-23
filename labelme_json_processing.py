import json

class LabelMeJSONProcessor:
    def __init__(self, json_file):
        self.json_file = json_file
        self.data = self.load_json()

    def load_json(self):
        with open(self.json_file, 'r') as file:
            return json.load(file)

    def get_shapes(self):
        return self.data.get('shapes', [])

    def get_image_data(self):
        return self.data.get('imageData', None)

    def get_labels(self):
        shapes = self.get_shapes()
        return [shape['label'] for shape in shapes]

    def get_bounding_boxes(self):
        shapes = self.get_shapes()
        bounding_boxes = []
        for shape in shapes:
            if shape['shape_type'] == 'rectangle':
                points = shape['points']
                x_min = min(points[0][0], points[1][0])
                y_min = min(points[0][1], points[1][1])
                x_max = max(points[0][0], points[1][0])
                y_max = max(points[0][1], points[1][1])
                bounding_boxes.append((x_min, y_min, x_max, y_max))
        return bounding_boxes

    def save_to_file(self, output_file):
        with open(output_file, 'w') as file:
            json.dump(self.data, file, indent=4)