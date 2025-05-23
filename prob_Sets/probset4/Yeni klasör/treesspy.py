'''
    Provided implementation. Do not modify any of the functions below
    You should acquaint yourself with how to initialize and access data from
    Node objects but you do not need to fully understand how this class works internally
'''

class Node:
    def __init__(self, value, left_child=None, right_child=None):
        '''
        Constructs an instance of Node
        Inputs:
            value: An object, the value held by this node
            left_child: A Node object if this node has a left child, None otherwise
            right_child: A Node object if this node has a right child, None otherwise
        '''
        if isinstance(left_child, Node):
            self.left = left_child
        elif left_child == None:
            self.left = None
        else:
            raise TypeError("Left child not an instance of Node")

        if isinstance(right_child, Node):
            self.right = right_child
        elif right_child == None:
            self.right = None
        else:
            raise TypeError("Right child not an instance of Node")

        self.value = value

    def get_left_child(self):
        '''
        Returns this node's left child if present. None otherwise
        '''
        return self.left

    def get_right_child(self):
        '''
        Returns this node's right child if present. None otherwise
        '''
        return self.right

    def get_value(self):
        '''
        Returns the object held by this node
        '''
        return self.value

    def __eq__(self, tree):
        '''
        Overloads the == operator
        Example usage: Node(6, Node(1)) == Node(6, Node(1)) evaluates to True
        Output:
            True or False if the tree is equal or not
        '''
        if not isinstance(tree, Node):
            return False
        return (self.value == tree.value and
                self.left == tree.left and
                self.right == tree.right)

    def __str__(self):
        '''
         Output:
            A well formated string representing the tree (assumes a node can have at most one parent)
         '''
         
        """
         MYYY
         Goal: Traverse the entire tree, grouping nodes by their depth (level).
            
         Parameters:
             tree: The current node.
             current_tier: The current node’s depth level (root is 0, children are 1, etc.).
             tier_map: A dictionary where keys = tier (depth), and values = list of nodes at that tier.
        
        Logic:
            If current_tier is not already a key in tier_map, create a new list with the current node.
            Otherwise, append the current node to the existing list.
            Recursively call itself on left and right children (increasing current_tier + 1).
        """
        
        def set_tier_map(tree,current_tier,tier_map):
            if current_tier not in tier_map:
                tier_map[current_tier] = [tree]
            else:
                tier_map[current_tier].append(tree)
            if tree.get_left_child() is not None:
                set_tier_map(tree.get_left_child(),current_tier+1,tier_map)
            if tree.get_right_child() is not None:
                set_tier_map(tree.get_right_child(),current_tier+1,tier_map)
        
        tiers = {}
        set_tier_map(self,0,tiers)
        """  
        tiers[0]: [1]
        tiers[1]: [2,5]
        tiers[2]: [7,8]
        MYYY
        ###Printing tiers dictioanry
        tiers = {}
        set_tier_map(self,0,tiers)
        for k in tiers.keys():
            print(f"\n{k}:")
            for i in tiers[k]:
                print(f"{i.get_value()}")
        return ""
        """
        nextTier = [True]
        for key in sorted(tiers,reverse=False):
            #key is 0,1,2
            """copy next_tier to current_tier, and create new tier with depth 2**(key+1)"""
            current_tier = nextTier[:]
            nextTier = [' ' for i in range(2**(key+1))]
            #for key=0,  current_tier=[True], nextTier = ['','']
            #for key=1,  current_tier=[True, True], nextTier = ['','','','']
            #for key=2, current_tier = ['','', True,True], nextTier = ['','','','','','','','']
            
            """"find first True indexed element in current_tier,which mean first node object 
                in current_tier and get its node value
                i is first node objects index number in current tier"""
            for tree in tiers[key]:
                i = current_tier.index(True)
                #for key=0, tree is node(1), i =0
                #for key=1,
                    #tree is node(2), i= 0
                    #tree is node(5), i=1
               
                current_tier[i] = str(tree.get_value())
                #for key=0, current_tier= [1]
                #for key=1,
                   # for tree = node(2), current_tier = [2, True]
                   # for tree = node(5), currentTier = [2,5]
                
                """ for creating next tier check every current_tier node object 
                whether it has either left or right child , if it has make next tier's 
                (2*current objects index number in current_tier) index True
                   [ 0      ,    1 ]
                   /  \         / \
                [(2*0), (2*0+1), (2*1) ,(2*1+1)]
                """
                if tree.get_left_child():
                    nextTier[2*i] = True
                    #for key = 0 nextTier= [True,'']
                    #for key = 1  nextTier= ['','', True,''] ,bcs node(2) hasn't left child but node(5) has 
                if tree.get_right_child():
                    nextTier[2*i+1] = True 
                    #for key = 0 nextTier= [True,True]
                    #for key = 1  nextTier= ['','', True,True] ,bcs node(2) hasn't right child but node(5) has 
            
            tiers[key] = current_tier
            #for key=0 ,tiers[0]=  [1]
            #for key=1 ,tiers[1]=  [2,5]
            #for key=2 ,tiers[2]=  ['','', 7,8]
            
        max_tier = max(tiers)
        lowest_tier = []
        for i,val in enumerate(tiers[max_tier]):
            lowest_tier.append(val)
            if i < len(tiers[max_tier])-1:
                lowest_tier.append(' ')
        all_tier_strs = [lowest_tier]
        skip,hop = 1,4
        for key in sorted(tiers,reverse=True):
            if key != max_tier:
                new_tier = [' ' for i in lowest_tier]
                arrow_tier = new_tier[:]
                tier_index,new_tier_index = 0,skip
                offset = hop//4
                if key != max_tier-1:
                    offset //= 2
                while new_tier_index < len(new_tier):
                    new_tier[new_tier_index] = tiers[key][tier_index]
                    if tiers[key+1][2*tier_index] != ' ':
                        arrow_tier[new_tier_index-offset] = '/'
                    if tiers[key+1][2*tier_index+1] != ' ':
                        arrow_tier[new_tier_index+offset] = '\\'
                    tier_index += 1
                    new_tier_index += hop
                skip = hop - 1
                hop = 2*hop
                all_tier_strs.append(arrow_tier)
                all_tier_strs.append(new_tier)

        out = []
        for t in all_tier_strs:
            out.append(' '.join(t))
        return '\n\n'.join(out[::-1])


example_tree = Node(1, Node(2), Node(5, Node(7), Node(8)))
print(example_tree)