module Sequences

    """
    fibonacci(n)

    Calculate the Fibonacci sequence up to the nth number.

    Arguments
    - `n`: The position in the Fibonacci sequence to calculate up to. Must be a positive integer.

    Returns
    - An array containing the Fibonacci sequence up to the nth number.
    """
    function fibonacci(n)
        fib_sequence = zeros(Int, n)
        fib_sequence[1] = 0
        fib_sequence[2] = 1
        for i = 3:n
            fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2]
        end
        return fib_sequence
    end

    """
        catalan_direct(n::Int)

    Compute the `n`-th Catalan number using the direct formula involving factorials.

    # Arguments
    - `n::Int`: The index of the Catalan number to compute.

    # Returns
    - `::BigInt`: The `n`-th Catalan number.

    # Examples
    ```julia
    catalan_direct(4) # returns 14
    """    
    function catalan_direct(n::Int)
        # Calculating the nth Catalan number using the direct formula
        return factorial(2n) // (factorial(n + 1) * factorial(n))
    end
    

    """
    catalan_dynamic(n::Int)

    Calculate the `n`-th Catalan number using a dynamic programming approach.

    # Arguments
    - `n::Int`: The index of the Catalan number to compute.

    # Returns
    - `::BigInt`: The `n`-th Catalan number.

    # Examples
    ```julia
    catalan_dynamic(4) # returns 14
    ```
    """
    function catalan_dynamic(n::Int)
        # Initialize an array to store intermediate results
        C = zeros(BigInt, n+1)
        C[1] = BigInt(1)
    
        # Fill the array using the dynamic programming approach
        for i in 2:n+1
            for j in 1:i-1
                C[i] += C[j] * C[i-j]
            end
        end
    
        return C[n+1]
    end

    """
    catalan(k::Int)

    Generate a list of the first `k` Catalan numbers using the `catalan_direct` function.

    # Arguments
    - `k::Int`: The number of Catalan numbers to generate.

    # Returns
    - `::Vector{BigInt}`: A vector of the first `k` Catalan numbers.
    """
    function catalan(k::Int)
        return [catalan_direct(n) for n in 0:(k-1)]
    end

    export fibonacci, catalan

end