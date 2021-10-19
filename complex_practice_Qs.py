import random
questions= [
    'What are holomorphic functions? What makes this stronger than differentiable real functions? What properties do they have? Give an example of a not holomorphic function.', 
        # complex differentiable (h->0 by *any* path in C). Properties: analytic, cauchy Riemann, infinitely differentiable 
    'What are the Cauchy Riemann Equations? Derive them.',
    'Give the definition for absolute convergence and radius of convergence. What is Hadamards Formula?',
    'Compute the path integral along the unit circle (positive) of 1/z and z^2',
    'What is a primitive? How do they relate to integrals? Show that if f\'=0 then f is constant.',
    'State and prove Cauchy\' Theorem.',
    'What is Morera\'s Theorem? How is it proved?',
    'State and prove Cauchy\'s Integral Formula. What are some consequences?',
    'Is there a generalization of Cauchy\'s integral formula? How is it proved?',
    'Give the Cauchy Inequalities and prove them.',
    'State and prove Liouville\'s Theorem. What if f^(n) is bounded? What if Im(f) is bounded?',
    'State and prove the Fundamental Theorem of Algebra.',
    'Use contour integrals to compute the integral from 0 to infinity of 1/1+x^2.',
    'What are some consequences of Cauchy\'s Integral Formula?',
    'What is the Residue Theorem? How do you prove it? Give an example of a residue computation.', 
        #example int 0 to infinity of 1/1+x^2 dx
    'Find the residue of e^z/z^3 at 0?',
    'Where in the proof of the open mapping theorem do you use the fact that f is non-constant?',
    'Suppose we have a holomorphic function f that lies within a strip of the exponential, i.e. |f(x)-e^x|<R for some R, what can we say about f?', # hint: Liouville's applied to g(x)=f(x)-e^x
    'Suppose f is holomorphic with image in R (the reals). What can you conclude about f?', 
        # hint: Cauchy Riemann equations 
    'Let Omega be some open domian with boundary C. What holomorphic functions map C to 0?', 
        # hint: open mapping theorem 
    'What is a meromorphic function? What is the definition of a pole?',
    'When does a meromorphic function have a Laurent series? Is it unique? Does it have a positive radius of convergence? Why? Can you think of a real power series with R=0?',
    'Let f be holomorphic in a closed ball around 0 with 0 removed (punctured ball). Is f meromorphic if we add 0?', 
        #no, f(z) = e^1/z has essential singularity. No such n s.t. lim z^n e^1/z exists and is finite
    'What is an essential singularity? Give an example of a function with an essential singularity.' 
        # def: f undefined and neither pole nor removable singularity, ex. f(z)=e^1/z
]


def pick_complex_questions(n):
    print("")
    selected_qs = random.sample(questions,n)
    for i, q in enumerate(selected_qs):
     print(str(i+1)+". "+q+"\n")

pick_complex_questions(7)