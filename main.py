from flask import Flask, render_template



def get_bits(n: int, width: int) -> list[bool]:
    if n < 0:
        raise ValueError("Only non-negative integers supported")

    bits = [bit == "1" for bit in bin(n)[2:]]

    if len(bits) > width:
        raise ValueError(f"Width {width} is too small to represent {n}")

    bits = [False] * (width - len(bits)) + bits
    return bits

def get_gate(inputs: int, n: int):
    width = 2 ** inputs
    gate = []
    x = list(reversed(get_bits(n, width)))
    for i in range(width):
        gate.append((get_bits(i, inputs), x[i]))
    return gate


app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")