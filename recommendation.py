class Product:
    def __init__(self, name, category, conversion_prob):
        self.name = name
        self.category = category
        self.conversion_prob = conversion_prob

    def set_name(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category

    def set_conversion_prob(self, conversion_prob):
        self.conversion_prob = conversion_prob

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def get_conversion_prob(self):
        return self.conversion_prob

class AStarRecommendation:
    def __init__(self, products):
        self.products = products
    
    def a_star_recommendation(self, initial_product, final_product):
        """
        Implements the A* algorithm to recommend the optimal path from initial_product to final_product
        based on conversion probability as heuristic.
        """
        import heapq

        # Build adjacency list where each product connects to all other products
        # Cost can be defined, for example, as 1 for each transition (or other relevant criteria)
        graph = {}
        for product in self.products:
            neighbors = []
            for other_product in self.products:
                if other_product != product:
                    # Define transition cost as needed; here we use cost 1 as example
                    neighbors.append((other_product, 1))
            graph[product] = neighbors

        # Heuristic function: negative conversion probability (higher probability = lower cost)
        def heuristic(product):
            return -product.get_conversion_prob()

        open_set = []
        heapq.heappush(open_set, (heuristic(initial_product), 0, initial_product, [initial_product]))

        closed_set = set()
        g_scores = {initial_product: 0}

        while open_set:
            _, current_g, current, path = heapq.heappop(open_set)

            if current == final_product:
                return [p.get_name() for p in path]

            closed_set.add(current)

            for neighbor, cost in graph.get(current, []):
                if neighbor in closed_set:
                    continue
                tentative_g = current_g + cost
                if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                    g_scores[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor)
                    heapq.heappush(open_set, (f_score, tentative_g, neighbor, path + [neighbor]))

        return None  # No path found
        
        
# Products for electronics store with different conversion levels

# HIGH conversion product - Popular headphones
airpods_headphones = Product(
    name="AirPods Pro 2nd Generation",
    category="Audio",
    conversion_prob=0.85  # 85% conversion probability (high)
)

# MEDIUM conversion product - Laptop
gaming_laptop = Product(
    name="ASUS ROG Strix G15 Gaming Laptop",
    category="Computers",
    conversion_prob=0.45  # 45% conversion probability (medium)
)

# LOW conversion product - Specialized printer
printer_3d = Product(
    name="Creality Ender-3 S1 Pro 3D Printer",
    category="3D Printing",
    conversion_prob=0.15  # 15% conversion probability (low)
)

# Product list for the recommendation system
electronics_products = [airpods_headphones, gaming_laptop, printer_3d]

# Example usage of the recommendation system
if __name__ == "__main__":
    # Create recommendation system instance
    recommendation_system = AStarRecommendation(electronics_products)
    
    # Example: find path from headphones to printer
    recommended_path = recommendation_system.a_star_recommendation(
        airpods_headphones, printer_3d
    )
    
    print("Products created:")
    for product in electronics_products:
        print(f"- {product.get_name()} ({product.get_category()}) - Conversion: {product.get_conversion_prob():.0%}")
    
    if recommended_path:
        print(f"\nRecommended path from {airpods_headphones.get_name()} to {printer_3d.get_name()}:")
        print(" → ".join(recommended_path))
    else:
        print("\nNo path found.")
