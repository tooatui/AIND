# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("goal", problem.goal)
    # print ("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print ("Start's successors:", problem.getSuccessors(problem.getStartState()))

    # initialize
    explored_states = []
    frontiers = util.Stack()

    start_node = (problem.getStartState(), [], 0)
    frontiers.push(start_node)

    while not frontiers.isEmpty():
        current_node = frontiers.pop()

        current_state = current_node[0]
        current_actions = current_node[1]

        # print("current_state:", current_state)
        # print("current_actions:", current_actions)
        # print("current_cost:", current_node[2])

        # test if it is goal
        if problem.isGoalState(current_state):
            return current_actions

        successors = problem.getSuccessors(current_state)

        for successor in successors:
            if successor[0] not in explored_states: 
                actions = list(current_actions)
                actions.append(successor[1])
                cost = current_node[2] + successor[2]
                updated_successor = (successor[0], actions, cost)

                frontiers.push(updated_successor)

        explored_states.append(current_state)

    # solution not found
    raise Exception('No path found!') 

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # initialize
    explored_states = []
    frontiers = util.Queue()

    start_node = (problem.getStartState(), [], 0)
    frontiers.push(start_node)

    while not frontiers.isEmpty():
        current_node = frontiers.pop()

        current_state = current_node[0]
        current_actions = current_node[1]

        # print("current_state:", current_state)
        # print("current_actions:", current_actions)
        # print("current_cost:", current_node[2])

        # test if it is goal
        if problem.isGoalState(current_state):
            return current_actions

        frontiers_states = list(node[0] for node in frontiers.list)
        for successor in problem.getSuccessors(current_state):
            successor_state = successor[0]
            if successor_state not in explored_states and successor_state not in frontiers_states: 
                actions = list(current_actions)
                actions.append(successor[1])
                cost = current_node[2] + successor[2]
                updated_successor = (successor_state, actions, cost)

                frontiers.push(updated_successor)

        explored_states.append(current_state)

    # solution not found
    raise Exception('No path found!') 

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # initialize
    explored_states = []
    frontiers = util.PriorityQueue()

    start_node = (problem.getStartState(), [], 0)
    frontiers.update(start_node, 0)

    while not frontiers.isEmpty():
        current_node = frontiers.pop()
        current_state = current_node[0]
        current_actions = current_node[1]

        # print("current_state:", current_state)
        # print("current_actions:", current_actions)
        # print("current_cost:", current_node[2])

        # you can add it to the frontier multiple times, but you shouldn't expand it more than once.
        if current_state not in explored_states:
            # test if it is goal
            if problem.isGoalState(current_state):
                return current_actions

            # is there any better way to find if the node is already in frontiers (hard to do in PriorityQueue)?
            # yes, check if the current node has alreay been explored (i.e. expanded)
            # see the condition above: if current_state not in explored_states:
            for successor in problem.getSuccessors(current_state):
                successor_state = successor[0]
                if successor_state not in explored_states:
                    actions = list(current_actions)
                    actions.append(successor[1])
                    cost = current_node[2] + successor[2]
                    updated_successor = (successor_state, actions, cost)

                    frontiers.update(updated_successor, cost)
            
            explored_states.append(current_state)

    # solution not found
    raise Exception('No path found!') 

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # initialize
    explored_states = []
    frontiers = util.PriorityQueue()
    
    start_node = (problem.getStartState(), [], 0)
    priority = start_node[2] + heuristic(problem.getStartState(), problem)
    frontiers.update(start_node, priority)

    while not frontiers.isEmpty():
        current_node = frontiers.pop()
        current_state = current_node[0]
        current_actions = current_node[1]

        # print("current_state:", current_state)
        # print("current_actions:", current_actions)
        # print("current_cost:", current_node[2])

        # you can add it to the frontier multiple times, but you shouldn't expand it more than once.
        if current_state not in explored_states:
            # test if it is goal
            if problem.isGoalState(current_state):
                return current_actions

            # is there any better way to find if the node is already in frontiers (hard to do in PriorityQueue)?
            # yes, check if the current node has alreay been explored (i.e. expanded)
            # see the condition above: if current_state not in explored_states:
            for successor in problem.getSuccessors(current_state):
                successor_state = successor[0]
                if successor_state not in explored_states:
                    actions = list(current_actions)
                    actions.append(successor[1])
                    cost = (current_node[2] + successor[2]) 
                    priority = cost + heuristic(successor_state, problem)
                    updated_successor = (successor_state, actions, cost)

                    frontiers.update(updated_successor, priority)
            
            explored_states.append(current_state)

    # solution not found
    raise Exception('No path found!') 


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
