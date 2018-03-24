class Vertex:
    def __init__(self, node):
        self.id = node
        self.edges_leaving = []

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_edge(self, edge):
        self.edges_leaving.append(edge)

    def get_connections(self):
        return self.edges_leaving

    def get_id(self):
        return self.id

class Edge:

    def __init__(self, from, to, usd_value, to_amount, from_amount):
        self.tail = tail
        self.head = to
        self.usd_value = usd_value
        self.from_amount = from_amount
        self.to_amount = to_amount
        self.trade_ratio = float(to_amount) / float(from_amount)

    def getFrom(self):
        return self.tail

    def getTo(self):
        return self.head

    def getFromAmount(self):
        return self.from_amount

    def getToAmount(self):
        return self.to_amount

    def getTradeRatio(self):
        return self.trade_ratio

    def getUSDValue(self):
        return self.usd_value

    def __str__(self):
        return "Trade Order : " + str(self.tail) " -> " + str(self.head) + " @ " str(self.give_currency_amount) + ' to ' + str(self.want_currency_amount)


class Graph:
    def __init__(self):
        # Vertex Set
        self.graph = {}
        self.num_vertices = 0
        self.num_edges = 0

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.graph[node] = []

    def get_vertex(self, n):
        if n in self.graph:
            return self.graph[n]
        else:
            return None

    def add_edge(self, frm, to, from_amount, to_amount, usd_value):
        new_edge = Edge(frm, to, usd_value, to_amount, from_amount)

        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        # Update graph and the actual vertex to keep track of what edges are available
        self.graph[frm].append(new_edge)
        # Below isn't *necessary* but might be helpful for something later
        self.graph[frm].add_edge(new_edge)

    def get_vertices(self):
        return self.graph.keys()



########################################################################
########################################################################
#######     CYCLE FINDING IMPLEMENTATION BELOW IN PROGRESS       #######
########################################################################
########################################################################


# Start of finding all cycles
def dfs(graph, start, end):
    fringe = [(start, [], 1, 1000000)]
    while fringe:
        node, path, trade_ratio, min_usd = fringe.pop()
        if path and node == end:
            yield (path, trade_ratio, min_usd)
            continue
        for edge in graph[node]:
            #getting head and tail vertices  of this edge
            from_vertex = edge.getFrom()
            to_vertex = edge.getTo()
            if to_vertex in path:
                continue
            trade_ratio = trade_ratio * edge.getTradeRatio()
            min_usd = min(min_usd, edge.getUSDValue())
            fringe.append((to_vertex, path+[to_vertex], trade_ratio, min_usd))

# Returns all cycles with min usd pushed along that cycle (bottle neck flow)
# Along with the trade ratio

cycles = [ [ [node]+path[0],path[1],path[2]]   for node in graph for path in dfs(graph, node, node)]
# End to finding all cycles

if __name__ == '__main__':
