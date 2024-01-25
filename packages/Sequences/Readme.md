# Sequences.jl

Sequences.jl is a Julia module designed to generate mathematical sequences, including the Fibonacci sequence and Catalan numbers, through various computational approaches.

## Features

- Calculate the entire Fibonacci sequence up to the `n`th number.
- Compute Catalan numbers using either direct computation or dynamic programming.
- Generate a list of the first `k` Catalan numbers. 

## Usage


To generate the Fibonacci sequence up to the `n`th number:

```julia
using Sequences
sequence = fibonacci(n)
```