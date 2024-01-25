using Test
using Sequences

@testset "Sequences Module Tests" begin

    @testset "Fibonacci Function Tests" begin
        @test Sequences.fibonacci(1) == [0]
        @test Sequences.fibonacci(2) == [0, 1]
        @test Sequences.fibonacci(5) == [0, 1, 1, 2, 3]
        @test Sequences.fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        @test_throws ArgumentError Sequences.fibonacci(-1)
        @test_throws ArgumentError Sequences.fibonacci(0)
    end

    @testset "Catalan Direct Function Tests" begin
        @test Sequences.catalan_direct(0) == 1
        @test Sequences.catalan_direct(1) == 1
        @test Sequences.catalan_direct(4) == 14
        @test Sequences.catalan_direct(5) == 42
        @test_throws ArgumentError Sequences.catalan_direct(-1)
    end

    @testset "Catalan Dynamic Function Tests" begin
        @test Sequences.catalan_dynamic(0) == 1
        @test Sequences.catalan_dynamic(1) == 1
        @test Sequences.catalan_dynamic(4) == 14
        @test Sequences.catalan_dynamic(5) == 42
        @test_throws ArgumentError Sequences.catalan_dynamic(-1)
    end

    @testset "Catalan List Function Tests" begin
        @test Sequences.catalan(1) == [1]
        @test Sequences.catalan(4) == [1, 1, 2, 5]
        @test Sequences.catalan(5) == [1, 1, 2, 5, 14]
        @test_throws ArgumentError Sequences.catalan(-1)
    end

end