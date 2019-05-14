"""
Scenario 2: List of route costs to check

You have a carrier route list with 100,000 (100K) entries (in arbitrary order) 
and a list of 1000 phone numbers. How can you operationalize the route cost lookup problem?
"""
import os
class CallRouting(object):

    def __init__(self, route_costs, phone_numbers):
        self.route_costs = route_costs
        self.phone_numbers = phone_numbers
    
    def dict_of_routes(self):
        """
        Returns a dictionary of routes >> key: route, value: cost

        Time Complexity:
        Best >> O(n*l) >> n = number of lines, l = length of the line
        Worst >> N/A
        Space Complexity:
        O(n) >> the bigger the dict, the more space
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
               

    def list_of_numbers(self):
        """
        Returns list of phone numbers, 1000
        """
        list_of_numbers = []
        with open(self.phone_numbers) as file:
            for line in file:
                number = line[:-1]
                list_of_numbers.append(number)
        return list_of_numbers

    def cost_of_calling(self, phone_number, routes):
        """
        Goes through dict_of_routes to find the input number cost
        Time Complexity:
        Best >> O(1) >> 1st number match
        Worst >> O(n) >> go throught the dict
        Space Complexity: 
        O(1) >> not creating anything
        """

        while len(phone_number) > 1:
            try:
                if routes[phone_number] is not None:
                    cost = routes[phone_number]
                    cheapest = min(cost)
                    return cheapest
            except:
                phone_number = phone_number[:-1]
        return None

        
    def input_number_costs(self):
        """
        Returns a dictionary of input number and cost of calling
        Time Complexity:
        Best >>
        Worst >>
        Space Complexity:
        """
        input_numbers = self.list_of_numbers()
        route = self.dict_of_routes()
        input_number_costs = {}

        for number in input_numbers:
            cost = self.cost_of_calling(number, route)
            input_number_costs[number] = cost

        return input_number_costs



    
def test_call_routing():
    pass


if __name__ == '__main__':
    # route_costs = os.path.dirname("/data/route-costs-106000.txt")
    # phone_numbers = os.path.dirname("/data/phone-numbers-1000.txt")
    call_routing = CallRouting("route-costs-106000.txt", "phone-numbers-1000.txt")
    print(call_routing.input_number_costs())