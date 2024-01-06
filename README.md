# bitin

bitin is a comprehensive Python library designed to facilitate a wide range of digital electronics operations, from fundamental logic gate implementations to complex circuit simulations, this library provides a user-friendly interface to handle digital logic effortlessly. With bitin, users can perform operations such as Boolean algebra, circuit analysis and simulation, enabling the creation and manipulation of digital circuits with ease. 

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
```

<hr>

### Output 

```python
# Universal Gates
u = Universal()
a = u.logical_nand(1,1) # 0
b = u.logical_nor(1,1)  # 0
```

Note: 

For Basic Gates, if the type of gate, `gate_type` is not declared it is set as `nand` by default. To select the type of gate, `logical_<GATE>(input1, input2, 'nor')` or `logical_<GATE>(input1, input2, 'nand')`.

```python
# Basic Gates
u = Basic()
a = u.logical_and(1,1) # 1
b = u.logical_or(1,1)  # 1
c = u.logical_not(1)  # 0
d = u.logical_xor(1,1)  # 0
e = u.logical_xnor(1,1)  # 1
```
