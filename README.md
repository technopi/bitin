# bitin

bitin is a comprehensive Python library designed to facilitate a wide range of digital electronics operations, from fundamental logic gate implementations to complex circuit simulations, this library provides a user-friendly syntax to handle digital logic effortlessly. With bitin, users can perform operations such as Boolean algebra, circuit analysis and simulation, enabling the creation and manipulation of digital circuits with ease. 

## Usage:
This package comes with inbuit Universal Gates and Basic Gates.
```python
# Initialisation
import subprocess
subprocess.run(["pip", "install", "bitin"])
import bitin

# Call Universal Gates
from bitin.universal import Universal 


# Call Basic Gates
from bitin.basic import Basic

# Call Numerical base Conversion
from bitin.basesystem import Base_Translation, BaseReversal
```

<hr>

### Output 

##### 1. Universal Gates
```python

u = Universal()
a = u.logical_nand(1,1) # 0
b = u.logical_nor(1,1)  # 0
```

##### 2. Basic Gates
Note: 
For Basic Gates, if the type of gate, `gate_type` is not declared it is set as `nand` by default. To select the type of gate, `logical_<GATE>(input1, input2, 'nor')` or `logical_<GATE>(input1, input2, 'nand')`.

```python
b = Basic()
a = b.logical_and(1,1) # 1
b = b.logical_or(1,1)  # 1
c = b.logical_not(1)  # 0
d = b.logical_xor(1,1)  # 0
e = b.logical_xnor(1,1)  # 1
```

##### 3. Numerical base Conversion

```python
BaseReversal('1100').from_base(2)
```

Note: 
`precision` referes to the number of places after decimal, the output value will be calculated. This only has it's significance when the `input` number is in decimal and it's conversion is needed.
```python
Base_Translation(input, precision=10, d_type = 'decimal').to_base(base)
```

For addition of bits, convert them to `int(decimal)` add them, then convert them to desired output.
