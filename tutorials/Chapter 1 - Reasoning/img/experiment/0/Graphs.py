import lnn
graph = lnn.Graph()

A = graph.add_node("A")
B = graph.add_node("B")
C = graph.add_node("C")

graph.add_edge(A, B, lnn.Rule.AND)
graph.add_edge(B, C, lnn.Rule.OR)


A.add_data(lnn.Fact.TRUE)
B.add_data(lnn.Fact.FALSE)
C.add_data(lnn.Fact.TRUE)

graph.infer()

print(graph.nodes)


#2

graph = lnn.Graph()

# Add nodes to the graph
A = graph.add_node("A")
B = graph.add_node("B")
C = graph.add_node("C")

graph.add_edge(A, B, lnn.Rule.AND)
graph.add_edge(B, C, lnn.Rule.OR)

A.add_data(lnn.Fact.TRUE)
B.add_data(lnn.Fact.FALSE)
C.add_data(lnn.Fact.TRUE)

graph.infer()

for node in graph.nodes:
    print(f"{node.name}: {node.get_truth_value()}") 

import matplotlib.pyplot as plt
import networkx as nx

G1 = nx.Graph()
G1.add_node("A", value="TRUE")
G1.add_node("B", value="FALSE")
G1.add_node("C", value="TRUE")

G1.add_edge("A", "B", rule="AND")
G1.add_edge("B", "C", rule="OR")

G2 = nx.Graph()
G2.add_node("A", value="TRUE")
G2.add_node("B", value="FALSE")
G2.add_node("C", value="TRUE")

G2.add_edge("A", "B", rule="AND")
G2.add_edge("B", "C", rule="OR")

# Plotting Function
def plot_graph(G, graph_num):
    plt.figure(figsize=(5, 5))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=['green' if data['value'] == "TRUE" else 'red' for _, data in G.nodes(data=True)], node_size=2000)
    plt.title(f"Graph #{graph_num}")
    plt.show()

# Plotting both graphs
plot_graph(G1, 1)
plot_graph(G2, 2)




class Node {
    constructor(name) {
        this.name = name;
        this.data = null;
        this.edges = [];
    }

    addData(data) {
        this.data = data;
    }

    addEdge(node) {
        this.edges.push(node);
    }
}

class Graph {
    constructor() {
        this.nodes = [];
    }

    addNode(name) {
        const node = new Node(name);
        this.nodes.push(node);
        return node;
    }

    query(...nodes) {
        // Example logic for logical OR: returns true if any node is TRUE
        return nodes.some(node => node.data === true);
    }
}

// Create the graph
<script>
const graph = new Graph();

const B = graph.addNode("B");
const D = graph.addNode("D");
const E = graph.addNode("E");

B.addData(true);
D.addData(false);
E.addData(true);

// Add edges (though not used in the query here)
B.addEdge(D);
D.addEdge(E);

// Query the logical disjunction between nodes B, D, and E
const disjunction = graph.query(B, D, E);

// Print the result
console.log(disjunction);  // This will log true


    const nodes = [
        { id: "B", value: true },
        { id: "D", value: false },
        { id: "E", value: true }
    ];

    const links = [
        { source: "B", target: "D" },
        { source: "D", target: "E" }
    ];

    const svg = d3.select("svg");

    const link = svg.append("g")
      .selectAll("line")
      .data(links)
      .enter().append("line")
      .style("stroke", "black");

    const node = svg.append("g")
      .selectAll("circle")
      .data(nodes)
      .enter().append("circle")
      .attr("r", 10)
      .attr("fill", d => d.value ? "green" : "red");

    // Add labels
    const labels = svg.append("g")
      .selectAll("text")
      .data(nodes)
      .enter().append("text")
      .attr("dy", ".35em")
      .attr("x", 12)
      .text(d => d.id);

    const simulation = d3.forceSimulation(nodes)
      .force("link", d3.forceLink().id(d => d.id))
      .force("charge", d3.forceManyBody())
      .force("center", d3.forceCenter(300, 200));

    simulation
      .nodes(nodes)
      .on("tick", ticked);

    simulation.force("link")
      .links(links);

    function ticked() {
        link
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        node
            .attr("cx", d => d.x)
            .attr("cy", d => d.y);

        labels
            .attr("x", d => d.x)
            .attr("y", d => d.y);
    }




