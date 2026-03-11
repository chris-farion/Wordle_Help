from Wordle import *

def test_empty_list():
    assert is_list_sorted([]) == True

def test_singelton_list():
    assert is_list_sorted(['order']) == True

def test_unordered_list():
    assert is_list_sorted(['order','above']) == False

def test_ordered_list():
    assert is_list_sorted(['above','order']) == True

def test_split_list():
    list = ['above','order']
    first,second = split_list(list)
    assert first == ['above']
    assert second == ['order']

#Blue/Gold Binary Search Tree Tests
def test_add_node_to_empty_tree():
    test_tree = Blue_Gold_Tree()
    root_node = Rank_Node("Root",0)
    test_tree += root_node
    assert test_tree.root == root_node

def test_root_node_is_blue():
    test_tree = Blue_Gold_Tree()
    root_node = Rank_Node("Root",0)
    test_tree += root_node
    assert root_node.blue == True

def test_add_greater_than_node():
    test_tree = Blue_Gold_Tree()
    root_node = Rank_Node("Root",0)
    more_node = Rank_Node("More",1)
    test_tree += root_node
    test_tree += more_node
    assert root_node.right == more_node

def test_add_less_than_node():
    test_tree = Blue_Gold_Tree()
    root_node = Rank_Node("Root",0)
    less_node = Rank_Node("Less",-1)
    test_tree += root_node
    test_tree += less_node
    assert root_node.left == less_node

def test_gold_uncle():
    test_tree = Blue_Gold_Tree()
    node_010 = Rank_Node("None",10)
    node_005 = Rank_Node("None",5)
    node_015 = Rank_Node("None",15)
    node_001 = Rank_Node("None",1)
    test_tree += node_010
    test_tree += node_005
    test_tree += node_015
    test_tree += node_001
    assert test_tree.root == node_010
    assert node_010.blue == True
    assert node_005.blue == True
    assert node_015.blue == True
    assert node_001.blue == False

def test_blue_uncle_angle():
    test_tree = Blue_Gold_Tree()
    node_010 = Rank_Node("None",10)
    node_005 = Rank_Node("None",5)
    node_015 = Rank_Node("None",15)
    node_012 = Rank_Node("None",12)
    test_tree += node_010
    test_tree += node_005
    test_tree += node_015
    test_tree += node_012
    assert test_tree.root == node_010
    assert node_010.blue == True
    assert node_005.blue == True
    assert node_015.blue == True
    assert node_012.blue == False

def test_blue_uncle_line():
    test_tree = Blue_Gold_Tree()
    node_010 = Rank_Node("None",10)
    node_005 = Rank_Node("None",5)
    node_015 = Rank_Node("None",15)
    node_003 = Rank_Node("None",3)
    node_001 = Rank_Node("None",1)
    test_tree += node_010
    test_tree += node_005
    test_tree += node_015
    test_tree += node_003
    test_tree += node_001
    assert test_tree.root.left == node_003
    assert node_010.blue == True
    assert node_005.blue == True
    assert node_015.blue == True
    assert node_001.blue == False

def test_right_rotation():
    test_tree = Blue_Gold_Tree()
    node_001 = Rank_Node("None",1)
    node_002 = Rank_Node("None",2)
    node_003 = Rank_Node("None",3)
    test_tree += node_001
    test_tree += node_002
    test_tree += node_003
    assert test_tree.root == node_002

def test_left_rotation():
    test_tree = Blue_Gold_Tree()
    node_003 = Rank_Node("None",3)
    node_002 = Rank_Node("None",2)
    node_001 = Rank_Node("None",1)
    test_tree += node_003
    test_tree += node_002
    test_tree += node_001
    assert test_tree.root == node_002
