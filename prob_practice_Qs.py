import random
questions_ch1 = [
    'How do we develop integration for integrable functions? What is the definition of integrable and why is it important?',
    'What are random variables, distribution functions, and probablity measures of random variables?',
    'What is a sigma-algebra? What are the Borels?',
    'What is a (probability) measure? What are some properties?',
    'What are some convergence theorems for integration? When do they hold?',
    'What is E[X]? What are some nice expressions for E[X]? E|X|? EX^k?',
    'What is Var(X)? How does it relate to E[X]?',
    'What is Chebyshev\' Inequality? Give a general and common form.',
    'What is Jensen\' Inequality? Holder\'s Inequality?',
    'State Fubini\' Theorem. Use it to derive a formula for E|X|.',
    'What is the pi-lambda theorem? Why is it useful? Give an example.',
    'What is convergence in P? convergence a.s.? in L^p? How do they relate? What is an example of something that converges in P but not a.s.? in P but not Lp?'
]

questions_ch2 = [
    'When do expectations add? What about variance?',
    'What is the definition of independence?',
    'State the weak law of large numbers (i.i.d.). Sketch a proof.',
    'State the strong law of large numbers. Sketch a proof (you may assume EX^4<infty). What if E|X_i| = infty?',
    'What is the Borel-Cantelli Lemma? Prove it. Does the converse hold, if not, what condition(s) need to be added? How do you prove it?',
    'What are some equivalent characterizations of convergence in P?',
    'Consider a sequence of i.i.d. variables Xi, how can we express X_n -> 0 a.s. in terms of a convergence in probability?',
    'What is Kolmogorov\'s 0-1 Law? Give some examples of tail sigma-fields. What is a key idea in the proof?',
    'State Kolmogorov\'s Maximal Inequality. How does it compare to Chebyshev\'s Inequality?'
]

questions_ch3 = [
    'State and prove the Central Limit Theorem (i.i.d. is fine).',
    'What are characteristic functions? What are some properties? Can you state an inversion formula?',
    'The central limit theorem uses weak convergence, why can\'t it be convergence in probability?',
    'What is weak convergence? Give at least 3 characterizations of weak convergence.',
    'How do weak convergence and convergence in probability relate?',
    'Suppose you have random variables X1,X2,... with characteristic functions phi_1, phi_2, ... with phi_n -> Phi. What can you say about this? When can you say more and why?',
    'What is the Lindeberg-Feller Central Limit Theorem? Do you know any other generalizations of the IID CLT?'
]

questions_ch4 = [
    'What is a regular conditional probability?',
    'What is the definition of uniformly integrable? What can you say about a martingale that is uniformly integrable?',
    'What is optional stopping? What are some conditions under which it holds? Give an example where optional stopping fails.',
    'What is the definition of a martingale? Give some examples.',
    'Can you apply optional stopping to get a formula for the probability that the simple symmetric random walk on Z, started at 0, hits some -a before b?',
    'Give a convergence theorem for martingales. How do you prove a.s. convergence? Why do we handle Lp and L1 convergence differently?',
    'What is the connection between martingales and betting (specifically the classic martingale strategy)?',
    'Let X_n be martingale and T be a stopping time. What is true of X_N^n? What if X_n is UI?',
    'Let X_n be submartingale and let H_n be predictable and N be a stopping time. Show that (H * X)_n and X_N^n are submartingale (you may assume H>=0 where needed).'
]

questions_ch5 = [
    'Can you have a process which is Markov and Martingale? What if the state space is finite?',
    'Define the following terms: recurrent, null reccurent, and positive recurrent.',
    'What are class properties for a markov chain? Give an example with proof.',
    'What is the period for a Markov chain? What does this have to do with convergence? Give an example of a periodic chain and explain why it cannot converge.',
    'State a markov convergence theorem. Prove it.',
    'Let p have a stationary distrubtion pi. What can we conclude about recurrence?',
    'What is the definition of a stationary measure? Do you know any generalizations?',
    'What is the Markov property? The strong Markov property?',
]


def pick_prob_questions(n, ch1=True, ch2=True, ch3=True, ch4=True, ch5=True):
    print("")
    questions = []
    if(ch1):
        questions += questions_ch1 
    if(ch2):
        questions += questions_ch2
    if(ch3):
        questions += questions_ch3 
    if(ch4):
        questions += questions_ch4 
    if(ch5):
        questions += questions_ch5         
    selected_qs = random.sample(questions,n)
    for i, q in enumerate(selected_qs):
        print(str(i+1)+". "+q+"\n")

pick_prob_questions(7, ch4=True, ch5=False, ch1=False, ch2=False, ch3=False)