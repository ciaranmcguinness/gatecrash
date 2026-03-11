class LayeredTruthTable:
    def __init__(self, inputs: int):
        self.inputs = inputs
        self.table = []
        # create a layer for each input
        self.table = [[j // (2 ** i) % 2 == 1 for j in range(2 ** inputs)] for i in range(inputs)]
        self.output_column = -1 # int once done

    def apply_transform(self, cols: list[int], transform: LayeredTruthTable):
        if len(cols) != transform.inputs:
            raise ValueError(f"Expected {transform.inputs} columns, got {len(cols)}")
        
        # add column, containing output of eval() for each row
        new_column = []
        for i in range(2 ** self.inputs):
            input_values = [self.table[col][i] for col in cols]
            new_column.append(transform.eval(input_values))
        self.table.append(new_column)
    
    def eval(self, input_values: list[bool]) -> bool:
        if len(input_values) != self.inputs:
            raise ValueError(f"Expected {self.inputs} inputs, got {len(input_values)}")
        if self.output_column == -1:
            raise ValueError("Output column not set")
        return self.table[self.output_column][sum([input_values[i] * (2 ** i) for i in range(self.inputs)])]
    
nand = LayeredTruthTable(2)
nand.table.append([True, True, True, False])
nand.output_column = 2

print(nand.eval([False, False])) # True
print(nand.eval([False, True])) # True
print(nand.eval([True, False])) # True
print(nand.eval([True, True])) # False

a = LayeredTruthTable(2)
a.apply_transform([0, 1], nand)
a.apply_transform([2,2], nand)
a.output_column = 3
print(a.eval([True, True])) # True