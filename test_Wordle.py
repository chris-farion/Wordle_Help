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
    assert test_tree.root.isBlue == True

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

def test_gold_uncle_left():
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
    assert node_010.isBlue == True
    assert node_005.isBlue == True
    assert node_015.isBlue == True
    assert node_001.isBlue == False

def test_gold_uncle_right():
    test_tree = Blue_Gold_Tree()
    node_010 = Rank_Node("None",10)
    node_005 = Rank_Node("None",5)
    node_015 = Rank_Node("None",15)
    node_020 = Rank_Node("None",20)
    test_tree += node_010
    test_tree += node_005
    test_tree += node_015
    test_tree += node_020
    assert test_tree.root == node_010
    assert node_010.isBlue == True
    assert node_005.isBlue == True
    assert node_015.isBlue == True
    assert node_020.isBlue == False

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
    assert node_010.isBlue == True
    assert node_005.isBlue == True
    assert node_015.isBlue == True
    assert node_012.isBlue == False

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
    assert test_tree.root == node_010
    assert test_tree.root.left == node_003
    assert node_010.isBlue == True
    assert node_005.isBlue == False
    assert node_015.isBlue == True
    assert node_003.isBlue == True
    assert node_001.isBlue == False

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

def test_duplicate():
    test_tree = Blue_Gold_Tree()
    node_003 = Rank_Node("None",3)
    test_tree += node_003
    test_tree += node_003
    assert test_tree.root.right == node_003

def test_perfect_tree():
    test_tree = Blue_Gold_Tree()
    node_050 = Rank_Node("None",50)
    node_025 = Rank_Node("None",25)
    node_075 = Rank_Node("None",75)
    node_012 = Rank_Node("None",12)
    node_038 = Rank_Node("None",38)
    node_063 = Rank_Node("None",63)
    node_088 = Rank_Node("None",88)
    node_007 = Rank_Node("None",7)
    node_019 = Rank_Node("None",19)
    node_032 = Rank_Node("None",32)
    node_044 = Rank_Node("None",44)
    node_057 = Rank_Node("None",57)
    node_069 = Rank_Node("None",69)
    node_082 = Rank_Node("None",82)
    node_094 = Rank_Node("None",94)
    test_tree += node_050
    test_tree += node_025
    test_tree += node_075
    test_tree += node_012
    test_tree += node_038
    test_tree += node_063
    test_tree += node_088
    test_tree += node_007
    test_tree += node_019
    test_tree += node_032
    test_tree += node_044
    test_tree += node_057
    test_tree += node_069
    test_tree += node_082
    test_tree += node_094
    assert test_tree.root == node_050

def test_delete_leaf_node():
    test_tree = Blue_Gold_Tree()
    node_050 = Rank_Node("None",50)
    node_025 = Rank_Node("None",25)
    node_075 = Rank_Node("None",75)
    node_012 = Rank_Node("None",12)
    node_038 = Rank_Node("None",38)
    node_063 = Rank_Node("None",63)
    node_088 = Rank_Node("None",88)
    node_007 = Rank_Node("None",7)
    node_019 = Rank_Node("None",19)
    node_032 = Rank_Node("None",32)
    node_044 = Rank_Node("None",44)
    node_057 = Rank_Node("None",57)
    node_069 = Rank_Node("None",69)
    node_082 = Rank_Node("None",82)
    node_094 = Rank_Node("None",94)
    test_tree += node_050
    test_tree += node_025
    test_tree += node_075
    test_tree += node_012
    test_tree -= node_012
    assert node_025.left.score == float("-inf")
    assert test_tree.nodes == 3

def test_delete_node_1_child():
    test_tree = Blue_Gold_Tree()
    node_050 = Rank_Node("None",50)
    node_025 = Rank_Node("None",25)
    node_075 = Rank_Node("None",75)
    node_012 = Rank_Node("None",12)
    node_038 = Rank_Node("None",38)
    node_063 = Rank_Node("None",63)
    node_088 = Rank_Node("None",88)
    node_007 = Rank_Node("None",7)
    node_019 = Rank_Node("None",19)
    node_032 = Rank_Node("None",32)
    node_044 = Rank_Node("None",44)
    node_057 = Rank_Node("None",57)
    node_069 = Rank_Node("None",69)
    node_082 = Rank_Node("None",82)
    node_094 = Rank_Node("None",94)
    test_tree += node_050
    test_tree += node_025
    test_tree += node_075
    test_tree += node_012
    test_tree -= node_025
    assert node_050.left == node_012
    assert test_tree.nodes == 3

def test_delete_node_2_children():
    test_tree = Blue_Gold_Tree()
    node_050 = Rank_Node("None",50)
    node_025 = Rank_Node("None",25)
    node_075 = Rank_Node("None",75)
    node_012 = Rank_Node("None",12)
    node_038 = Rank_Node("None",38)
    node_063 = Rank_Node("None",63)
    node_088 = Rank_Node("None",88)
    node_007 = Rank_Node("None",7)
    node_019 = Rank_Node("None",19)
    node_032 = Rank_Node("None",32)
    node_044 = Rank_Node("None",44)
    node_057 = Rank_Node("None",57)
    node_069 = Rank_Node("None",69)
    node_082 = Rank_Node("None",82)
    node_094 = Rank_Node("None",94)
    test_tree += node_050
    test_tree += node_025
    test_tree += node_075
    test_tree += node_012
    test_tree += node_038
    test_tree -= node_025
    assert test_tree.nodes == 4
    assert test_tree.root.left == node_038

def test_delete_node_not_found():
    test_tree = Blue_Gold_Tree()
    node_050 = Rank_Node("None",50)
    node_025 = Rank_Node("None",25)
    node_075 = Rank_Node("None",75)
    node_012 = Rank_Node("None",12)
    node_038 = Rank_Node("None",38)
    node_063 = Rank_Node("None",63)
    node_088 = Rank_Node("None",88)
    node_007 = Rank_Node("None",7)
    node_019 = Rank_Node("None",19)
    node_032 = Rank_Node("None",32)
    node_044 = Rank_Node("None",44)
    node_057 = Rank_Node("None",57)
    node_069 = Rank_Node("None",69)
    node_082 = Rank_Node("None",82)
    node_094 = Rank_Node("None",94)
    test_tree += node_050
    test_tree += node_025
    test_tree += node_075
    test_tree -= node_038
    assert test_tree.nodes == 3

def test_delete_case_01():
    test_tree = Blue_Gold_Tree()
    node_050 = Rank_Node("None",50)
    node_025 = Rank_Node("None",25)
    node_075 = Rank_Node("None",75)
    node_012 = Rank_Node("None",12)
    node_038 = Rank_Node("None",38)
    node_063 = Rank_Node("None",63)
    node_088 = Rank_Node("None",88)
    node_007 = Rank_Node("None",7)
    node_019 = Rank_Node("None",19)
    node_032 = Rank_Node("None",32)
    node_044 = Rank_Node("None",44)
    node_057 = Rank_Node("None",57)
    node_069 = Rank_Node("None",69)
    node_082 = Rank_Node("None",82)
    node_094 = Rank_Node("None",94)
    test_tree += node_050
    test_tree += node_025
    test_tree += node_075
    test_tree += node_012
    test_tree += node_038
    test_tree += node_063
    test_tree += node_088
    test_tree += node_019
    test_tree += node_082
    test_tree += node_094
    test_tree -= node_019
    assert test_tree.nodes == 9
    assert node_012.right.score == float("-inf")

def test_delete_case_02():
    test_tree = Blue_Gold_Tree()
    node_050 = Rank_Node("None",50)
    node_025 = Rank_Node("None",25)
    node_075 = Rank_Node("None",75)
    node_012 = Rank_Node("None",12)
    node_038 = Rank_Node("None",38)
    node_063 = Rank_Node("None",63)
    node_088 = Rank_Node("None",88)
    node_007 = Rank_Node("None",7)
    node_019 = Rank_Node("None",19)
    node_032 = Rank_Node("None",32)
    node_044 = Rank_Node("None",44)
    node_057 = Rank_Node("None",57)
    node_069 = Rank_Node("None",69)
    node_082 = Rank_Node("None",82)
    node_094 = Rank_Node("None",94)
    test_tree += node_050
    test_tree += node_025
    test_tree += node_075
    test_tree += node_012
    test_tree += node_038
    test_tree += node_063
    test_tree += node_088
    test_tree += node_019
    test_tree += node_082
    test_tree += node_094
    test_tree -= node_012
    assert test_tree.nodes == 9
    assert node_025.left == node_019

def test_delete_case_03():
    test_tree = Blue_Gold_Tree()
    node_050 = Rank_Node("None",50)
    node_025 = Rank_Node("None",25)
    node_075 = Rank_Node("None",75)
    node_012 = Rank_Node("None",12)
    node_038 = Rank_Node("None",38)
    node_063 = Rank_Node("None",63)
    node_088 = Rank_Node("None",88)
    node_007 = Rank_Node("None",7)
    node_019 = Rank_Node("None",19)
    node_032 = Rank_Node("None",32)
    node_044 = Rank_Node("None",44)
    node_057 = Rank_Node("None",57)
    node_069 = Rank_Node("None",69)
    node_082 = Rank_Node("None",82)
    node_094 = Rank_Node("None",94)
    test_tree += node_050
    test_tree += node_025
    test_tree += node_075
    test_tree += node_012
    test_tree += node_038
    test_tree += node_063
    test_tree += node_088
    test_tree += node_019
    test_tree += node_082
    test_tree += node_094
    test_tree -= node_075
    assert test_tree.nodes == 9
    assert test_tree.root.right == node_082
    assert node_088.left.score == float("-inf")

def test_delete_case_04():
    test_tree = Blue_Gold_Tree()
    node_050 = Rank_Node("None",50)
    node_025 = Rank_Node("None",25)
    node_075 = Rank_Node("None",75)
    node_012 = Rank_Node("None",12)
    node_038 = Rank_Node("None",38)
    node_063 = Rank_Node("None",63)
    node_088 = Rank_Node("None",88)
    node_007 = Rank_Node("None",7)
    node_019 = Rank_Node("None",19)
    node_032 = Rank_Node("None",32)
    node_044 = Rank_Node("None",44)
    node_057 = Rank_Node("None",57)
    node_069 = Rank_Node("None",69)
    node_082 = Rank_Node("None",82)
    node_094 = Rank_Node("None",94)
    test_tree += node_050
    test_tree += node_025
    test_tree += node_075
    test_tree += node_012
    test_tree += node_038
    test_tree += node_063
    test_tree += node_088
    test_tree += node_019
    test_tree += node_082
    test_tree += node_094
    test_tree -= node_088
    assert test_tree.nodes == 9
    assert node_075.right == node_094
    assert node_094.isBlue == True

def test_delete_case_05():
    test_tree = Blue_Gold_Tree()
    node_050 = Rank_Node("None",50)
    node_025 = Rank_Node("None",25)
    node_075 = Rank_Node("None",75)
    node_012 = Rank_Node("None",12)
    node_038 = Rank_Node("None",38)
    node_063 = Rank_Node("None",63)
    node_088 = Rank_Node("None",88)
    node_007 = Rank_Node("None",7)
    node_019 = Rank_Node("None",19)
    node_032 = Rank_Node("None",32)
    node_044 = Rank_Node("None",44)
    node_057 = Rank_Node("None",57)
    node_069 = Rank_Node("None",69)
    node_082 = Rank_Node("None",82)
    node_094 = Rank_Node("None",94)
    test_tree += node_050
    test_tree += node_025
    test_tree += node_075
    test_tree += node_063
    test_tree += node_088
    test_tree += node_057
    test_tree += node_069
    test_tree += node_094
    test_tree -= node_075
    assert test_tree.nodes == 7
    assert test_tree.root.right == node_088
    assert node_088.isBlue == False
    assert node_094.isBlue == True

def test_delete_case_06():
    test_tree = Blue_Gold_Tree()
    node_050 = Rank_Node("None",50)
    node_025 = Rank_Node("None",25)
    node_075 = Rank_Node("None",75)
    node_012 = Rank_Node("None",12)
    node_038 = Rank_Node("None",38)
    node_063 = Rank_Node("None",63)
    node_088 = Rank_Node("None",88)
    node_007 = Rank_Node("None",7)
    node_019 = Rank_Node("None",19)
    node_032 = Rank_Node("None",32)
    node_044 = Rank_Node("None",44)
    node_057 = Rank_Node("None",57)
    node_069 = Rank_Node("None",69)
    node_082 = Rank_Node("None",82)
    node_094 = Rank_Node("None",94)
    test_tree += node_050
    test_tree += node_025
    test_tree += node_075
    test_tree += node_012
    test_tree += node_038
    test_tree += node_063
    test_tree += node_088
    test_tree += node_007
    test_tree -= node_007
    assert test_tree.nodes == 7
    assert node_025.isBlue == False
    assert node_012.isBlue == True
    assert node_038.isBlue == True
    test_tree -= node_025
    assert test_tree.nodes == 6
    assert test_tree.root.left == node_038
    assert node_038.isBlue == True
    assert node_007.isBlue == False

def test_delete_case_07():
    test_tree = Blue_Gold_Tree()
    node_050 = Rank_Node("None",50)
    node_025 = Rank_Node("None",25)
    node_075 = Rank_Node("None",75)
    node_012 = Rank_Node("None",12)
    node_038 = Rank_Node("None",38)
    node_063 = Rank_Node("None",63)
    node_088 = Rank_Node("None",88)
    node_007 = Rank_Node("None",7)
    node_019 = Rank_Node("None",19)
    node_032 = Rank_Node("None",32)
    node_044 = Rank_Node("None",44)
    node_057 = Rank_Node("None",57)
    node_069 = Rank_Node("None",69)
    node_082 = Rank_Node("None",82)
    node_094 = Rank_Node("None",94)
    test_tree += node_050
    test_tree += node_025
    test_tree += node_075
    test_tree += node_012
    test_tree += node_038
    test_tree += node_063
    test_tree += node_088
    test_tree += node_019
    test_tree += node_082
    test_tree += node_094
    test_tree -= node_050
    assert test_tree.nodes == 9
    assert test_tree.root == node_063
    assert test_tree.root.right == node_088
    assert node_088.isBlue == False
    assert node_088.left == node_075
    assert node_088.right == node_094
    assert node_075.right == node_082
    assert node_075.isBlue == True
    assert node_094.isBlue == True

def test_delete_case_08():
    test_tree = Blue_Gold_Tree()
    node_050 = Rank_Node("None",50)
    node_025 = Rank_Node("None",25)
    node_075 = Rank_Node("None",75)
    node_012 = Rank_Node("None",12)
    node_038 = Rank_Node("None",38)
    node_063 = Rank_Node("None",63)
    node_088 = Rank_Node("None",88)
    node_007 = Rank_Node("None",7)
    node_019 = Rank_Node("None",19)
    node_032 = Rank_Node("None",32)
    node_044 = Rank_Node("None",44)
    node_057 = Rank_Node("None",57)
    node_069 = Rank_Node("None",69)
    node_082 = Rank_Node("None",82)
    node_094 = Rank_Node("None",94)
    test_tree += node_050
    test_tree += node_025
    test_tree += node_075
    test_tree += node_012
    test_tree += node_038
    test_tree += node_063
    test_tree += node_088
    test_tree += node_019
    test_tree += node_082
    test_tree += node_094
    test_tree -= node_025
    assert test_tree.nodes == 9
    assert test_tree.root.left == node_019

def test_delete_case_09():
    test_tree = Blue_Gold_Tree()
    node_050 = Rank_Node("None",50)
    node_025 = Rank_Node("None",25)
    node_075 = Rank_Node("None",75)
    node_012 = Rank_Node("None",12)
    node_038 = Rank_Node("None",38)
    node_063 = Rank_Node("None",63)
    node_088 = Rank_Node("None",88)
    node_007 = Rank_Node("None",7)
    node_019 = Rank_Node("None",19)
    node_032 = Rank_Node("None",32)
    node_044 = Rank_Node("None",44)
    node_057 = Rank_Node("None",57)
    node_069 = Rank_Node("None",69)
    node_082 = Rank_Node("None",82)
    node_094 = Rank_Node("None",94)
    test_tree += node_050
    test_tree += node_025
    test_tree += node_075
    test_tree += node_063
    test_tree += node_088
    test_tree += node_057
    test_tree += node_069
    test_tree += node_094
    test_tree -= node_025
    assert test_tree.nodes == 7
    assert test_tree.root == node_075
    assert node_075.isBlue == True
    assert node_075.left == node_063
    assert node_063.isBlue == False
    assert node_063.left == node_050
    assert node_050.isBlue == True
    assert node_050.right == node_057
    assert node_057.isBlue == False
    assert node_063.right == node_069
    assert node_069.isBlue == True
    assert node_075.right == node_088
    assert node_088.isBlue == True
    assert node_088.right == node_094
    assert node_094.isBlue == False

def test_delete_case_10():
    test_tree = Blue_Gold_Tree()
    node_050 = Rank_Node("None",50)
    node_025 = Rank_Node("None",25)
    node_075 = Rank_Node("None",75)
    node_012 = Rank_Node("None",12)
    node_038 = Rank_Node("None",38)
    node_063 = Rank_Node("None",63)
    node_088 = Rank_Node("None",88)
    node_007 = Rank_Node("None",7)
    node_019 = Rank_Node("None",19)
    node_032 = Rank_Node("None",32)
    node_044 = Rank_Node("None",44)
    node_057 = Rank_Node("None",57)
    node_069 = Rank_Node("None",69)
    node_082 = Rank_Node("None",82)
    node_094 = Rank_Node("None",94)
    test_tree += node_050
    test_tree += node_025
    test_tree += node_075
    test_tree += node_012
    test_tree += node_038
    test_tree += node_063
    test_tree += node_088
    test_tree += node_019
    test_tree += node_082
    test_tree += node_094
    test_tree -= node_038
    assert test_tree.nodes == 9
    assert test_tree.root.left == node_019
    assert node_019.right == node_025
    assert node_025.isBlue == True

def test_delete_case_11():
    test_tree = Blue_Gold_Tree()
    node_050 = Rank_Node("None",50)
    node_025 = Rank_Node("None",25)
    node_075 = Rank_Node("None",75)
    node_012 = Rank_Node("None",12)
    node_038 = Rank_Node("None",38)
    node_063 = Rank_Node("None",63)
    node_088 = Rank_Node("None",88)
    node_007 = Rank_Node("None",7)
    node_019 = Rank_Node("None",19)
    node_032 = Rank_Node("None",32)
    node_044 = Rank_Node("None",44)
    node_057 = Rank_Node("None",57)
    node_069 = Rank_Node("None",69)
    node_082 = Rank_Node("None",82)
    node_094 = Rank_Node("None",94)
    test_tree += node_050
    test_tree += node_025
    test_tree += node_075
    test_tree += node_012
    test_tree -= node_012
    test_tree -= node_025
    assert test_tree.nodes == 2
    assert node_075.isBlue == False
