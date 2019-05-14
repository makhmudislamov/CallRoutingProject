"""
Scenario 2: List of route costs to check

You have a carrier route list with 100,000 (100K) entries (in arbitrary order) 
and a list of 1000 phone numbers. How can you operationalize the route cost lookup problem?
"""

class CallRouting(object):

    def __init__(self, route_costs, phone_numbers):
        self.route_costs = route_costs
        self.phone_numbers = phone_numbers
    
    def dict_of_routes(self):
        """
        Returns a dictionary of routes >> key: route, value: cost
        """
        dict_of_routes = {}

        with open(self.route_costs) as file:
            for line in file:
                list_from_lines = line.split(",")
                route = list_from_lines[0]
                cost = list_from_lines[1]
                if list_from_lines[0] in dict_of_routes:
                    dict_of_routes[route].append(cost[:1])
                else:
                    dict_of_routes[route] = [cost[:-1]]
        return dict_of_routes 
        # return input_numbers        

    def route_cost_to_hashtable():
        """
        Returns converted txt file of route costs as hashtable
        key, value = route, cost
        """
        pass
        # return route_cost

    def look_up_cost():
        """
        Returns union of two sets: route costs and input 1000 phone numbers
        """
        pass

    
def test_call_routing():
    pass


if __name__ == '__main__':
    pass