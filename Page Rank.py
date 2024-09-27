dic = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['A', 'B', 'C'],
    'D': ['C']
}
k = 5

def pageRank(dic, k, damping_factor=0.85):
    # Calculate inbound links
    inbound = {i: [] for i in dic}
    for i in dic:
        for j in dic:
            if i in dic[j]:
                inbound[i].append(j)
    print("Connected Nodes:", inbound)
 
   # Initialize ranks
    num_nodes = len(dic)
    rank = {i: 1 / num_nodes for i in dic.keys()}
    for iteration in range(k):
        new_rank = {i: (1 - damping_factor) / num_nodes for i in dic.keys()}
        for node in dic:
            temp = 0
            for inbound_node in inbound[node]:
                temp += damping_factor * (rank[inbound_node] / len(dic[inbound_node]))
            new_rank[node] += temp
        rank = new_rank.copy()
        print(f"Iteration {iteration + 1}:", rank)
    return rank




# Run PageRank and print the final ranks
final_ranks = pageRank(dic, k)
print("Final Ranks:", final_ranks)
