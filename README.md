<h1>Generating a recursive sequence via exp(z)</h1>

This is a program to calculate a sequence of arbitrary length for the sequence a_0 = z, a_n = exp(i(a_{n-1})), where z is an arbitrary complex number, a_n is the nth member of the sequence, e is euler's constant, exp(z) = e^z,and i is the square root of -1.

The dependencies of this program are the sympy library. Install it with

<code>pip install sympy</code>

The way to use this program is

<code>python [exp-generate.py or rounded-exp-generate.py] [real part of a_0] [imaginary part of a_0] [number of iterations]</code>

Using the rounded method is the preferred way of doing things. If you use exp-generate it will go through all the iterations, however if you use rounded-exp-generate it will stop when the previous number in the sequence is 0.001 away in both real and complex parts.

What's interesting about this program is that *most* numbers seem to converge to gamma + ~(i0.375), where gamma is the Euler-Mascheroni constant, I don't know what the imaginary part is, i.e. if it's a known constant.

However, when you plug in the number -2 - 2i it diverges, I'm not sure of any other numbers you can plug in to get it to diverge, and I'm not sure what's special about -2 - 2i. I got that number through testing :)

EDIT: The general form for the number z to cause the sequence to diverge is {a + bi | a = -2^(2k+1), b = -2^(2j+1), a,b > 0 and a >=b}, or at least one of them
