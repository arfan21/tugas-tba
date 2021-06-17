import string

# Daftar Kata
# Subject (SB):
# madre (ibu)
# nonna (nenek)
# nonno (kakek)
# padre (ayah)

# Verb (VB):
# mangiare (memakan)
# pianta (menanam)
# raccolto (memanen)

# Object (OB):
# grano (gandum)
# mais (jagung) 
# mela (apel)

# CFG
# <S> ::= <SB> <VB> <OB>
# <SB> ::= padre | madre | nonno | nonna
# <VB> ::= raccolto | mangiare | pianta
# <OB> ::= mela | mais | grano

print('''
List Verb :
# <SB> ::= padre | madre | nonno | nonna
# <VB> ::= raccolto | mangiare | pianta
# <OB> ::= mela | mais | grano

# example : padre reccolto mela
''')

# input example
sentence = input("Please enter something (only those in the list of verbs): ")
print("=====================================================================\n")
inputString = sentence.lower() + "#"

# initialization

alphabet_list = list(string.ascii_lowercase)
state_list = ['q0', 'q1', 'q2',  'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'b1', 'b2', 'b3', 'b4', 'c1', 'c2',
              'c3', 'c4', 'd1', 'd2', 'd3', 'd4', 'd5', 'e1', 'e2', 'f1', 'f2', 'f3', 'f4', 'f5', 'g1', 'g2', 'g3']

transition_table = {}

for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state, alphabet)] = 'error'
    transition_table[(state, '#')] = 'error'
    transition_table[(state, ' ')] = 'error'

# update the transition_table for the following token : padre
transition_table[('q0', 'p')] = 'd1'
transition_table[('d1', 'a')] = 'g1'
transition_table[('g1', 'd')] = 'g2'
transition_table[('g2', 'r')] = 'g3'
transition_table[('g3', 'e')] = 'q1'
transition_table[('q1', ' ')] = 'q2'
transition_table[('q1', '#')] = 'accept'
transition_table[('q2', ' ')] = 'q2'
transition_table[('q2', '#')] = 'accept'

# update the transition_table for the following token : madre
transition_table[('q0', 'm')] = 'e1'
transition_table[('e1', 'a')] = 'f1'
transition_table[('f1', 'd')] = 'g2'
transition_table[('g2', 'r')] = 'g3'
transition_table[('g3', 'e')] = 'q1'
transition_table[('q1', ' ')] = 'q2'
transition_table[('q1', '#')] = 'accept'
transition_table[('q2', ' ')] = 'q2'
transition_table[('q2', '#')] = 'accept'

# update the transition_table for the following token : nonno
transition_table[('q0', 'n')] = 'c1'
transition_table[('c1', 'o')] = 'c2'
transition_table[('c2', 'n')] = 'c3'
transition_table[('c3', 'n')] = 'c4'
transition_table[('c4', 'o')] = 'q1'
transition_table[('q1', ' ')] = 'q2'
transition_table[('q1', '#')] = 'accept'
transition_table[('q2', ' ')] = 'q2'
transition_table[('q2', '#')] = 'accept'

# update the transition_table for the following token : nonna
transition_table[('q0', 'n')] = 'c1'
transition_table[('c1', 'o')] = 'c2'
transition_table[('c2', 'n')] = 'c3'
transition_table[('c3', 'n')] = 'c4'
transition_table[('c4', 'a')] = 'q1'
transition_table[('q1', ' ')] = 'q2'
transition_table[('q1', '#')] = 'accept'
transition_table[('q2', ' ')] = 'q2'
transition_table[('q2', '#')] = 'accept'

# update the transition_table for the following token : raccolto
transition_table[('q0', 'r')] = 'a1'
transition_table[('a1', 'a')] = 'a2'
transition_table[('a2', 'c')] = 'a3'
transition_table[('a3', 'c')] = 'a4'
transition_table[('a4', 'o')] = 'a5'
transition_table[('a5', 'l')] = 'a6'
transition_table[('a6', 't')] = 'b4'
transition_table[('b4', 'o')] = 'q1'
transition_table[('q1', ' ')] = 'q2'
transition_table[('q1', '#')] = 'accept'
transition_table[('q2', ' ')] = 'q2'
transition_table[('q2', '#')] = 'accept'

# update the transition_table for the following token : mangiare
transition_table[('q0', 'm')] = 'e1'
transition_table[('e1', 'a')] = 'f1'
transition_table[('f1', 'n')] = 'f2'
transition_table[('f2', 'g')] = 'f3'
transition_table[('f3', 'i')] = 'f4'
transition_table[('f4', 'a')] = 'g2'
transition_table[('g2', 'r')] = 'g3'
transition_table[('g3', 'e')] = 'q1'
transition_table[('q1', ' ')] = 'q2'
transition_table[('q1', '#')] = 'accept'
transition_table[('q2', ' ')] = 'q2'
transition_table[('q2', '#')] = 'accept'

# update the transition_table for the following token : pianta
transition_table[('q0', 'p')] = 'd1'
transition_table[('d1', 'i')] = 'd2'
transition_table[('d2', 'a')] = 'd3'
transition_table[('d3', 'n')] = 'd4'
transition_table[('d4', 't')] = 'd5'
transition_table[('d5', 'a')] = 'q1'
transition_table[('q1', ' ')] = 'q2'
transition_table[('q1', '#')] = 'accept'
transition_table[('q2', ' ')] = 'q2'
transition_table[('q2', '#')] = 'accept'

# update the transition_table for the following token : mela
transition_table[('q0', 'm')] = 'e1'
transition_table[('e1', 'e')] = 'e2'
transition_table[('e2', 'l')] = 'd5'
transition_table[('d5', 'a')] = 'q1'
transition_table[('q1', ' ')] = 'q2'
transition_table[('q1', '#')] = 'accept'
transition_table[('q2', ' ')] = 'q2'
transition_table[('q2', '#')] = 'accept'

# update the transition_table for the following token : mais
transition_table[('q0', 'm')] = 'e1'
transition_table[('e1', 'a')] = 'f1'
transition_table[('f1', 'i')] = 'f5'
transition_table[('f5', 's')] = 'q1'
transition_table[('q1', ' ')] = 'q2'
transition_table[('q1', '#')] = 'accept'
transition_table[('q2', ' ')] = 'q2'
transition_table[('q2', '#')] = 'accept'

# update the transition_table for the following token : grano
transition_table[('q0', 'g')] = 'b1'
transition_table[('b1', 'r')] = 'b2'
transition_table[('b2', 'a')] = 'b3'
transition_table[('b3', 'n')] = 'b4'
transition_table[('q1', ' ')] = 'q2'
transition_table[('q1', '#')] = 'accept'
transition_table[('q2', ' ')] = 'q2'
transition_table[('q2', '#')] = 'accept'
transition_table[('b4', 'o')] = 'q1'
transition_table[('q1', ' ')] = 'q2'
transition_table[('q1', '#')] = 'accept'
transition_table[('q2', ' ')] = 'q2'
transition_table[('q2', '#')] = 'accept'

# transition for new token
transition_table[('q2', 'g')] = 'b1'
transition_table[('q2', 'r')] = 'a1'
transition_table[('q2', 'p')] = 'd1'
transition_table[('q2', 'm')] = 'e1'
transition_table[('q2', 'n')] = 'c1'

# lexical analyzer
indexCharInput = 0
state = 'q0'
currentToken = ""

while state != 'accept':
    currentCharInput = inputString[indexCharInput]
    currentToken += currentCharInput
    state = transition_table[(state, currentCharInput)]
    if state == 'q1':
        print(f'ACCEPTED : current token: "{currentToken}" valid')
        currentToken = ''
    if state == 'error':
        print(f'ERROR : current token: "{currentToken}"" is not valid')
        break
    indexCharInput += 1

if state == 'accept':
    print(f'ACCEPTED : semua token input: "{sentence}" is valid')
