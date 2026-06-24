import networkx as nx
import matplotlib.pyplot as plt

class LawDegreeNavigator:
    def __init__(self):
        self.graph = nx.DiGraph()
        self._load_kenyan_llb_curriculum()

    def _load_kenyan_llb_curriculum(self):
        """Standard CLE (Council of Legal Education) aligned curriculum mapping."""
        # Nodes: (Course Code, Name, Year)
        courses = [
            ("L101", "Legal Systems and Methods", 1),
            ("L102", "Law of Torts I", 1),
            ("L103", "Law of Contract I", 1),
            ("L104", "Constitutional Law I", 1),
            ("L105", "Criminal Law I", 1),
            ("L201", "Evidence I", 2),
            ("L202", "Administrative Law", 2),
            ("L203", "Criminal Procedure", 2),
            ("L204", "Civil Procedure I", 2),
            ("L301", "Jurisprudence", 3),
            ("L302", "Commercial Law", 3),
            ("L303", "Family Law", 3),
            ("L401", "Legal Research/Dissertation", 4),
            ("L402", "International Law", 4),
            ("ATP", "Advocates Training Program (KSL)", 5)
        ]
        
        for code, name, year in courses:
            self.graph.add_node(code, name=name, year=year)

        # Prerequisite Edges
        edges = [
            ("L101", "L201"), # Legal Systems -> Evidence
            ("L101", "L301"), # Legal Systems -> Jurisprudence
            ("L105", "L203"), # Criminal Law -> Criminal Procedure
            ("L104", "L202"), # Constitutional -> Administrative
            ("L102", "L204"), # Torts -> Civil Procedure
            ("L103", "L302"), # Contract -> Commercial
            ("L204", "ATP"),  # Civil Proc -> KSL
            ("L203", "ATP"),  # Crim Proc -> KSL
            ("L301", "L401"), # Jurisprudence -> Dissertation
        ]
        self.graph.add_edges_from(edges)

    def visualize(self, output_file="llb_pathway_2025.png"):
        plt.figure(figsize=(14, 10))
        
        # Positioning nodes by year (horizontal layers)
        pos = {}
        year_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        
        for node, data in self.graph.nodes(data=True):
            year = data['year']
            pos[node] = (year * 2, -year_counts[year])
            year_counts[year] += 1

        labels = {node: f"{node}\n{data['name']}" for node, data in self.graph.nodes(data=True)}
        
        nx.draw_networkx_nodes(self.graph, pos, node_size=3000, node_color="skyblue", alpha=0.9)
        nx.draw_networkx_edges(self.graph, pos, arrowstyle="->", arrowsize=20, edge_color="gray")
        nx.draw_networkx_labels(self.graph, pos, labels, font_size=8, font_weight="bold")

        plt.title("Kenyan Law Degree (LLB) Prerequisite Navigator 2025", fontsize=15)
        plt.axis("off")
        print(f"Saving visualization to {output_file}...")
        plt.savefig(output_file)
        plt.show()

    def get_path_to_ksl(self):
        """Finds critical path to Kenya School of Law."""
        print("\nCritical Path to Advocates Training Program (KSL):")
        try:
            paths = nx.all_simple_paths(self.graph, source="L101", target="ATP")
            for i, path in enumerate(paths):
                print(f"Option {i+1}: {' -> '.join(path)}")
        except nx.NetworkXNoPath:
            print("No specific core path defined.")

if __name__ == "__main__":
    navigator = LawDegreeNavigator()
    navigator.get_path_to_ksl()
    navigator.visualize()