## Tree problems:

This module contains solutions for most of the tree and BST related problems found
across the WWW ranging from sites such as hackerrank, geekforgeeks and other random sites.
Pep8 standard naming convention is followed.
The properties are accessed or mutated via getters and setters.

FUNCTIONS
    all_paths(root)
        Return all the paths of a binary tree from root node to leaf nodes.
        
        Input:
                   3
             6           7
          4     5     8     9
        1   7    2             10
        Output:
        [[3,6,4,1], [3,6,4,7], [3,6,5,2], [3,7,8], [3,7,9,10]]
        
        :param root: root node of a binary tree.
        :return: A list of the paths from root node to leaf node.
    
    bst_search(root, value)
        Search for the value in a BST.
        
        :param root: root of a binary tree.
        :param value: value to be searched for.
        :return: a boolean value that indicates whether the value is present or not.
    
    common_ancestor(root, value1, value2)
        Lowest Common Ancestor of a pair of values.
        
        :param root: root of the binary tree
        :param value1: The first value
        :param value2: The second value
        :return: the lowest common ancestor node's value
    
    get_height(root)
        Given a root of the tree, find it's max height.
        The height of the tree is the max height of either one of its subtrees.
        
        Input:
        1
        
        Output:
        0
        
        Input:
             2
           1   3
        
        Output:
        1
        
        Input:
              2
            1
         4    3
        
        Output:
        2
        
        :param root: root of the binary tree
        :return: the height of the binary tree
    
    is_identical(root1, root2)
        Given root nodes of two trees, check whether they're identical.
        
        :param root1: root node of a tree
        :param root2: root node of another tree
        :return: a boolean to indicate whether they're identical.
    
    mirror_tree(root)
        Mirror a given tree.
        
        Input:
              3
           1     2
         4   5     6
        Output:
                3
            2       1
          6      5     4
        :param root: root node of the binary tree.
        :return: the root of the mirrored tree.
    
    recursive_paths(root, path, results)


