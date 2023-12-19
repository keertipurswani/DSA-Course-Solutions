// https://leetcode.com/problems/clone-graph

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneUtil(Node* node, unordered_map<Node*, Node*>& mp) {      
        if(!node) return nullptr;
        Node* newNode = new Node(node->val);
        mp[node] = newNode;      
        for(auto itr : node->neighbors) {
            if(mp.find(itr) == mp.end()) {
                (newNode->neighbors).push_back(cloneUtil(itr, mp));
            } else {
                (newNode->neighbors).push_back(mp[itr]);        
            }
        }
        return newNode;
    }
     
    Node* cloneGraph(Node* node) {
        unordered_map<Node*, Node*> mp;
        return cloneUtil(node, mp);
    }
};