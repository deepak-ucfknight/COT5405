# import the necessary headers
import random  # to use random variable generation
import matplotlib.pyplot as plt # for plotting the graphs

# this class contains all the necessary methods for graph insertion and deletion
class Programming_Assignment2:

    def __init__(self):
        # constant strings for dictionary labels
        self.c_timestamp = "time"
        self.c_node_count = "nodes"
        self.c_edge_count = "edges"
        self.c_threshold = "threshold"
        self.c_degree_list = "degree list"
        self.c_probability_list = "probability list"
        self.c_predicted_node_count = "predicted node count"
        self.c_predicted_edge_count = "predicted edge count"
        self.c_predicted_distribution = "predicted distribution"

    # generation of discrete random variable between 0.1 to 0.99
    def generate_random_variable(self):
        return random.uniform(0.1, 0.99)

    # generation of discrete random variable between 0.1 to 0.99
    def get_degree_of_nodes(self,Graph):  # computing the degree of nodes in the graph, returns list of degrees
        degree_list = []
        for eachnode in Graph:
            degree = len(Graph[eachnode])
            degree_list.append(degree)
        return degree_list

    # computing the histogram of same degree counts in the graph
    # returns degree dictionary of structure : key : degree, value : no of occurences of the degree in Graph
    def get_Kth_order_of_degree(self,degree_list):
        degree_dict = {}
        for eachdegree in degree_list:
            if len(degree_dict) == 0:
                degree_dict[eachdegree] = [1]
            elif eachdegree not in degree_dict:
                degree_dict[eachdegree] = [1]
            elif eachdegree in degree_dict:
                degree_dict[eachdegree][0] = degree_dict[eachdegree][0] + 1
        return degree_dict

    # Computes no of edges in the graph, returns integer
    def get_number_of_edges_in_Graph(self,Graph):
        edges = 0
        for eachnode in Graph:
            edges = edges + len(Graph[eachnode])
        if edges / 2 == 0:
            return 1
        else:
            return edges / 2

    # API to perform addition of new node in the graph
    # incident node is found based on the birth probability of the node : degree of node / 2 X edges in graph
    def perform_birth_process(self, new_node, Graph):

        edges = self.get_number_of_edges_in_Graph(Graph)
        threshold = self.generate_random_variable()
        birth_probability = 0

        for incidentnode in Graph:
            degree_of_node = len(Graph[incidentnode])
            birth_probability = birth_probability + (degree_of_node / (2 * edges))  # d(u) / 2m

            if birth_probability > threshold:
                Graph[new_node] = [incidentnode]

                if len(Graph[incidentnode]) != 0:
                    Graph[incidentnode].append(new_node)
                else :
                    Graph[incidentnode] = [new_node]
                break

    # API to perform deletion of existing node in the graph
    # deletion is done based on death probability : nodes  - degree of node / nodes^2 - 2 X edges
    def perform_death_process(self, Graph):
        edges = self.get_number_of_edges_in_Graph(Graph)
        threshold = self.generate_random_variable()

        death_probability = 0
        nodes = len(Graph)

        for removal_node in Graph:

            degree_of_node = len(Graph[removal_node])
            death_probability = death_probability + ((nodes - degree_of_node) / ((nodes * nodes) - (edges * 2)))

            if death_probability >= threshold:
                for removal_edges in Graph[removal_node]:
                    if removal_edges != removal_node:
                        Graph[removal_edges].remove(removal_node)
                del Graph[removal_node]
                break

    # API to compute cummulative probabilities of the degrees in the graph
    # returns degree list containing degrees in the graph and cummulative probability of each degree
    def Compute_Probabilities(self,Graph,degree_dict):
        death_prob = []
        initial_death_prob = 0
        nodes = len(Graph)
        edges = self.get_number_of_edges_in_Graph(Graph)

        # reverse_unique_degree_list = sorted(unique_degree_list, key=int, reverse=True)
        keylist = sorted(list(degree_dict.keys()), key=int, reverse=True)

        for key in keylist:
            k_th_order = degree_dict[key][0]
            initial_death_prob = initial_death_prob + (k_th_order / nodes)
            degree_dict[key].append(initial_death_prob)

        a_keylist = sorted(keylist, key=int, reverse=False)

        for key in a_keylist:
            death_prob.append(degree_dict[key][1])
        return a_keylist, death_prob

    # API to predict the degree distribution in the graoh
    # k^(−1−(2p/2p−1)) where K is the degrees of the graph
    def predict_degree_distribution(self, degree_dict, Threshold):
        keylist = sorted(list(degree_dict.keys()), key=int, reverse=True)
        predicted_dist_list = []
        predicted_prob = 0
        power = - 1 - (2 * Threshold / (2 * Threshold - 1))
        for key in keylist:
            if key == 0:
                predicted_prob = predicted_prob
            else:
                predicted_prob = predicted_prob + int(key)**power
            degree_dict[key].append(predicted_prob)

        a_keylist = sorted(keylist, key=int, reverse=False)

        for key in a_keylist:
            predicted_dist_list.append(degree_dict[key][2])
        return a_keylist, predicted_dist_list

    #  API to run simulation and prediction for three different graph with 3 different probabilities
    def Compute_degree_distribution(self, Graph,Threshold):
        distributions = {}
        distributions[self.c_threshold] = []
        distributions[self.c_degree_list] = []
        distributions[self.c_probability_list] = []
        distributions[self.c_predicted_distribution] = []

        degree_dict = self.get_Kth_order_of_degree(self.get_degree_of_nodes(Graph))
        # degree_list = self.get_degree_of_nodes(Graph)
        degree_list, probability_list = self.Compute_Probabilities(Graph,degree_dict)
        degree_list, predicted_dist_list = self.predict_degree_distribution(degree_dict, Threshold)

        distributions[self.c_degree_list].append(degree_list)
        distributions[self.c_probability_list].append(probability_list)
        distributions[self.c_threshold].append(Threshold)
        distributions[self.c_predicted_distribution].append(predicted_dist_list)
        return distributions

    # API to perform simulation and prediction of birth and death process in the graph
    def perform_simulation(self,Graph,threshold,iteration_count):
        results = {}
        results[self.c_timestamp] = []
        results[self.c_node_count] = []
        results[self.c_edge_count] = []
        results[self.c_predicted_node_count] = []
        results[self.c_predicted_edge_count] = []

        for time_step in range(2, iteration_count):
            proces_threshold = self.generate_random_variable()
            if proces_threshold <= threshold:
                self.perform_birth_process(time_step,Graph)
            elif len(Graph) > 1:
                self.perform_death_process(Graph)

            if time_step % 1000 == 0:
                birth_threshold = threshold
                death_threshold = 1 - threshold
                results[self.c_timestamp].append(time_step)
                results[self.c_node_count].append(len(Graph))
                results[self.c_edge_count].append(self.get_number_of_edges_in_Graph(Graph))
                results[self.c_predicted_node_count].append((birth_threshold - death_threshold) * time_step)
                results[self.c_predicted_edge_count].append(birth_threshold * (birth_threshold - death_threshold) * time_step)
        return results

    # Main API for one click run of the entire graph
    # we need to just call this one function to get simulation and prediction results of the model
    def Run_Simulation(self, Graph,Thresholds,iteration_count):
        final_results = []
        distribution_results = []
        for each_simulation in range(0, len(Graph)):
            simulation_results = self.perform_simulation(Graph[each_simulation], Thresholds[each_simulation],iteration_count)
            final_results.append(simulation_results)
            distributions = self.Compute_degree_distribution(Graph[each_simulation], Thresholds[each_simulation])
            distribution_results.append(distributions)

        self.plot_node_growth(final_results,Thresholds)
        self.plot_edge_growth(final_results,Thresholds)

        self.plot_predicted_node_growth(final_results, Thresholds)
        self.plot_predicted_edge_growth(final_results, Thresholds)

        self.plot_degree_distribution(distribution_results)
        self.plot_predicted_distribution(distribution_results)


    # API's for plotting graphs

    def plot_node_growth(self, final_results,thresholds):
        plot = plt.plot(final_results[0][self.c_timestamp],final_results[0][self.c_node_count],
                        final_results[1][self.c_timestamp],final_results[1][self.c_node_count],
                        final_results[2][self.c_timestamp],final_results[2][self.c_node_count])

        plt.gca().legend((str(thresholds[0]), str(thresholds[1]), str(thresholds[2])))
        plt.xlabel("Time steps")
        plt.ylabel("Number of Nodes")
        plt.title("Growth rate of nodes in Graph G for three different thresholds")
        plt.show(plot)

    def plot_edge_growth(self, final_results,thresholds):
        plot = plt.plot(final_results[0][self.c_timestamp], final_results[0][self.c_edge_count],
                        final_results[1][self.c_timestamp], final_results[1][self.c_edge_count],
                        final_results[2][self.c_timestamp], final_results[2][self.c_edge_count])
        plt.gca().legend((str(thresholds[0]), str(thresholds[1]), str(thresholds[2])))
        plt.xlabel("Time steps")
        plt.ylabel("Number of Edges")
        plt.title("Growth rate of edges in Graph G for three different thresholds")
        plt.show(plot)

    def plot_predicted_node_growth(self, final_results, thresholds):
        plot = plt.plot(final_results[0][self.c_timestamp], final_results[0][self.c_predicted_node_count],
                        final_results[1][self.c_timestamp], final_results[1][self.c_predicted_node_count],
                        final_results[2][self.c_timestamp], final_results[2][self.c_predicted_node_count])
        plt.gca().legend((str(thresholds[0]), str(thresholds[1]), str(thresholds[2])))
        plt.xlabel("Time steps")
        plt.ylabel("Number of Nodes")
        plt.title("Predicted Growth rate of nodes in Graph G for three different thresholds")
        plt.show(plot)

    def plot_predicted_edge_growth(self, final_results, thresholds):
        plot = plt.plot(final_results[0][self.c_timestamp], final_results[0][self.c_predicted_edge_count],
                        final_results[1][self.c_timestamp], final_results[1][self.c_predicted_node_count],
                        final_results[2][self.c_timestamp], final_results[2][self.c_predicted_node_count])

        plt.gca().legend((str(thresholds[0]),
                          str(thresholds[1]),
                          str(thresholds[2])))

        plt.xlabel("Time steps")
        plt.ylabel("Number of Edges")
        plt.title("Predicted Growth rate of edges in Graph G for three different thresholds")
        plt.show(plot)

    def plot_degree_distribution(self, distribution_result):
        plot = plt.plot(distribution_result[0][self.c_degree_list][0], distribution_result[0][self.c_probability_list][0],
                        distribution_result[1][self.c_degree_list][0], distribution_result[1][self.c_probability_list][0],
                        distribution_result[2][self.c_degree_list][0], distribution_result[2][self.c_probability_list][0])

        plt.gca().legend((str(distribution_result[0][self.c_threshold][0]),
                          str(distribution_result[1][self.c_threshold][0]),
                          str(distribution_result[2][self.c_threshold][0])))

        plt.xlabel("Range of Degree in the Graph")
        plt.ylabel("Cummulative Probabilitiy of degree")
        plt.title("Degree distribution of final Graph")
        plt.xscale("log")
        plt.yscale("log")
        plt.show(plot)

    def plot_predicted_distribution(self, distribution_result):
        plot = plt.plot(distribution_result[0][self.c_degree_list][0], distribution_result[0][self.c_predicted_distribution][0],
                        distribution_result[1][self.c_degree_list][0], distribution_result[1][self.c_predicted_distribution][0],
                        distribution_result[2][self.c_degree_list][0], distribution_result[2][self.c_predicted_distribution][0])

        plt.gca().legend((str(distribution_result[0][self.c_threshold][0]),
                          str(distribution_result[1][self.c_threshold][0]),
                          str(distribution_result[2][self.c_threshold][0])))

        plt.xlabel("Range of Degree in the Graph")
        plt.ylabel("Cummulative Probabilitiy of degree")
        plt.title("Predicted Degree distribution of final Graph")
        plt.xscale("log")
        plt.yscale("log")
        plt.show(plot)




Graph_1 = { 1:[1] }
Graph_2 = { 1:[1] }
Graph_3 = { 1:[1] }

simulation_thresholds = [0.7,0.85,0.95]
Graphs = [Graph_1,Graph_2,Graph_3]

object_Programming_Assignment2 = Programming_Assignment2()
object_Programming_Assignment2.Run_Simulation(Graphs,simulation_thresholds, 10000)











