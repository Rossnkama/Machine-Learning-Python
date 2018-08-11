# Searching problem


class SearchProblem(object):
	""" Representing the search problem
	-------------------------------

	The search problem consists of:
		- A start node.
		- A neigbors function that returns enumerations of 
		  arcs from a given node.
		- A goal specification that takes a node and returns true
		  if that node is a goal.
		- A heuristic function (given a node, returns a non-negative real number. 
		  The heuristic function defaults to zero)

	In the following code raise NotImplementedError() is a 
	way to specify that this is an abstract method that needs 
	to be overridden to define an actual search problem.
	"""
	
	def start_node(self):
		"""returns the start node"""
		raise NotImplementedError("start_node")  # Abstract method

	def is_goal(self, node):
		"""is true if node is a goal"""
		raise NotImplementedError("is_goal")

	def neighbors(self, node):
		"""returns a list of arcs for the neighbors of the node"""
		raise NotImplementedError("neighbors")

	def heuristic(self, n):
		"""Gives the heuristic value of node n, returns 0 if not overridden"""
		return 0


class Arc(object):
	"""Consists of a (from_node, to_node) pair and a non-negative cost"""
	def __init__(self, from_node, to_node, cost=1, action=None):

		# Making sure that cost arguments are positive
		assert cost >= 0, ("Cost cannot be negative for", str(from_node), 
			"->", str(to_node), "Cost:", str(cost))

		self.from_node = from_node
		self.to_node = to_node
		self.cost = cost
		self.action = action

	def __repr__(self):
		"""String representation of an arc"""
		if self.action:
			return str(self.from_node) + "--" + str(self.action) + "-->" + str(self.to_node)
		else:
			return str(self.from_node) + "-->" + str(self.to_node)


class SearchProblemFromExplicitGraph(SearchProblem):
	""" Representing the search problem for an explicit graph
	---------------------------------------------------------

	The search problem consists of:
		- A list or set of nodes.
		- A list or set of arcs.
		- A start node. 
		- A list or set of goal nodes.
		- A dictionary that maps each node to it's heuristic value.

	The first representation of a search problem is from an explicit 
	graph (as opposed to one that is generated as needed).
	"""

	def __init__(self, nodes, arcs, start=None, goals=set(), hmap={}):
		self.neighbors = {}  # {from_node: [arc_1, arc_2... arc_n]}
		self.nodes = nodes

		for node in nodes:
			# Initialising empty array of neighbors for a particular node...
			# to fill in later
			self.neighbors[node] = []

		self.arcs = arcs

		for arc in arcs:
			# Appending arcs to from_nodes creating a network of neighbors
			self.neighbors[arc.from_node].append(arc)

		self.start = start
		self.goals = goals
		self.hmap = hmap

	def start_node(self):
		"""Returns start node"""
		return self.start

	
