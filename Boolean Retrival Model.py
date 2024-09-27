def boolean(strs=[], files=[], query=''):
    # Load file content if files are provided
    if len(files) != 0 and len(strs) == 0:
        strs = []
        for f in files:
            with open(f'{f}.txt', "r") as file:
                strs.append(file.read().strip())

    # Ensure everything is lowercase for consistency
    strs = [s.lower() for s in strs]
    query = query.lower()

    # Create a unique set of all words in all documents
    unique = set(' '.join(strs).split())

    # Create boolean values for each document indicating the presence of each word
    bool_val = [{word: word in s.split() for word in unique} for s in strs]

    query = query.split()
    var_bool = []
    ope = []
    not_switch = False

    # Process the query
    for term in query:
        if term in ('and', 'or'):
            ope.append(term)
        elif term == 'not':
            not_switch = True
        else:
            # Safely handle missing terms with a default value of False
            temp = [not doc.get(term, False) if not_switch else doc.get(term, False) for doc in bool_val]
            var_bool.append(temp)
            not_switch = False

    # Combine results based on the operators (and/or)
    while len(var_bool) > 1:
        a, b = var_bool.pop(0), var_bool.pop(0)
        op = ope.pop(0)
        var_bool.insert(0, [i and j if op == 'and' else i or j for i, j in zip(a, b)])

    # Return the document numbers that match the query
    return 'document number:' + str([index + 1 for index, value in enumerate(var_bool[0]) if value])

# For User Input
s1 = "java is elegant"
s2 = "C++ is powerful"
s3 = "Rust is safe"
s4 = "Go is efficient"
s5 = "Kotlin is modern"
strs = [s1, s2, s3, s4, s5]
query = "is and not Kotlin and not C++"
print('Input ', boolean(strs=strs, query=query))

# Input from Files
files = ['d1', 'd2', 'd3', 'd4', 'd5']
query = 'not java and not Python and is'
print('File ', boolean(files=files, query=query))
