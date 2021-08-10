class BaseTransformer:
    @staticmethod
    def single_transform(value):
        return vars(value)


    @classmethod
    def transform(cls, values: list):
        data = []

        if len(values) < 1:
            return data

        for value in values:
            data.append(cls.single_transform(value))
        
        return data