

print("""
    List kata pertama   : 'padre', 'madre', 'nonno', 'nonna'
    List kata kedua     : 'raccolto', 'mangiare', 'pianta'
    List kata ketiga    : 'mela', 'mais', 'grano'
""")
sentence = input("Input sebuah kalimat (sesuai gammar dan kamus): ")
tokens = sentence.lower().split()
tokens.append('EOS')
# symbols definition
non_terminals = ['S', '<SB>', '<VB>', '<OB>']
terminals = ['padre', 'madre', 'nonno', 'nonna', 'raccolto',
             'mangiare', 'pianta', 'mela', 'mais', 'grano']
# parse table definition
parse_table = {}
parse_table[('S', 'padre')] = ['<SB>', '<VB>', '<OB>']
parse_table[('S', 'madre')] = ['<SB>', '<VB>', '<OB>']
parse_table[('S', 'nonno')] = ['<SB>', '<VB>', '<OB>']
parse_table[('S', 'nonna')] = ['<SB>', '<VB>', '<OB>']
parse_table[('S', 'raccolto')] = ['error']
parse_table[('S', 'mangiare')] = ['error']
parse_table[('S', 'pianta')] = ['error']
parse_table[('S', 'mela')] = ['error']
parse_table[('S', 'mais')] = ['error']
parse_table[('S', 'grano')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('<SB>', 'padre')] = ['padre']
parse_table[('<SB>', 'madre')] = ['madre']
parse_table[('<SB>', 'nonno')] = ['nonno']
parse_table[('<SB>', 'nonna')] = ['nonna']
parse_table[('<SB>', 'raccolto')] = ['error']
parse_table[('<SB>', 'mangiare')] = ['error']
parse_table[('<SB>', 'pianta')] = ['error']
parse_table[('<SB>', 'mela')] = ['error']
parse_table[('<SB>', 'mais')] = ['error']
parse_table[('<SB>', 'grano')] = ['error']
parse_table[('<SB>', 'EOS')] = ['error']

parse_table[('<VB>', 'padre')] = ['error']
parse_table[('<VB>', 'madre')] = ['error']
parse_table[('<VB>', 'nonno')] = ['error']
parse_table[('<VB>', 'nonna')] = ['error']
parse_table[('<VB>', 'raccolto')] = ['raccolto']
parse_table[('<VB>', 'mangiare')] = ['mangiare']
parse_table[('<VB>', 'pianta')] = ['pianta']
parse_table[('<VB>', 'mela')] = ['error']
parse_table[('<VB>', 'mais')] = ['error']
parse_table[('<VB>', 'grano')] = ['error']
parse_table[('<VB>', 'EOS')] = ['error']

parse_table[('<OB>', 'padre')] = ['error']
parse_table[('<OB>', 'madre')] = ['error']
parse_table[('<OB>', 'nonno')] = ['error']
parse_table[('<OB>', 'nonna')] = ['error']
parse_table[('<OB>', 'raccolto')] = ['error']
parse_table[('<OB>', 'mangiare')] = ['error']
parse_table[('<OB>', 'pianta')] = ['error']
parse_table[('<OB>', 'mela')] = ['mela']
parse_table[('<OB>', 'mais')] = ['mais']
parse_table[('<OB>', 'grano')] = ['grano']
parse_table[('<OB>', 'EOS')] = ['error']

# stack initialization
stack = []
stack.append('#')
stack.append('S')

# input reading initialization
idx_token = 0
symbol = tokens[idx_token]
# parsing process
while (len(stack) > 0):
    top = stack[len(stack) - 1]
    print('top = ', top)
    print('symbol = ', symbol)
    if top in terminals:
        print('top adalah simbol terminal')
        if top == symbol:
            stack.pop()
            idx_token = idx_token + 1
            symbol = tokens[idx_token]
            if symbol == 'EOS':
                print('isi stack:', stack)
                stack.pop()
        else:
            print('error')
            break
    elif top in non_terminals:
        print('top adalah simbol non-terminal')
        if parse_table[(top, symbol)][0] != 'error':
            stack.pop()
            symbols_to_be_pushed = parse_table[(top, symbol)]
            for i in range(len(symbols_to_be_pushed)-1, -1, -1):
                stack.append(symbols_to_be_pushed[i])
        else:
            print('error')
            break
    else:
        print('error')
        break
    print('isi stack:', stack)
    print()

# conclusion
print()
if symbol == 'EOS' and len(stack) == 0:
    print('ACCEPT: Input string ', sentence, ' diterima, sesuai Grammar')
else:
    print('ERROR: input string:', sentence,
          ', tidak diterima, tidak sesuai Grammar')
