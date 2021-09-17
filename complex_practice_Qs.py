import random
questions= [
    'What are holomorphic functions? What makes this stronger than differentiable real functions? What properties do they have? Give an example of a not holomorphic function.',
    'What are the Cauchy Riemann Equations? Derive them.',
    'Give the defition for absolute convergence and radius of convergence. What is Hadamards Formula?',
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
    'Find the residue of e^z/z^3 at 0?',
    'Where in the proof of the open mapping theorem do you use the fact that f is non-constant?'
]


def pick_complex_questions(n):
    print("")
    selected_qs = random.sample(questions,n)
    for i, q in enumerate(selected_qs):
     print(str(i+1)+". "+q+"\n")

pick_complex_questions(7)