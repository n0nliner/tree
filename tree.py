"""
written by Alexander Chudaykin December 19, 2018.
"""


class tree:
    """tree object"""
    def __init__(self):
        self.tree = {"0":{'childrens':[], 'parrent_id':None, "name":'root', "content":None}}

    def __repr__(self):
        res = ''
        for node in self.tree:
            res += '{} : {} \n'.format(node , self.tree.get(node))
        return res

    def __iter__(self):
        for node in self.tree:
            yield {node:self.tree.get(node)}

    def add_node(self, parrent_id="0",**kwargs):
        '''
        add node to tree
        '''
        if parrent_id not in self.tree:
            exit('Node with this id does not exist in this tree')
        # adding important values
        stock_params = {'parrent_id': parrent_id , "childrens":[]}
        add_stock = lambda param , key : kwargs.update({param:key}) if param not in kwargs else None
        for param in stock_params:
            add_stock(param , stock_params.get(param))
        #
        my_parrent = self.tree.get(parrent_id)
        nodeName = parrent_id  + '.' + str(len(my_parrent.get("childrens"))+1)
        self.tree.update({nodeName : kwargs})
        my_parrent.get('childrens').append(nodeName)
        return self.tree

    def get_nodes_by_params(self ,**kwargs):
        '''
        This code search nodes in tree by any params or update them.
        '''
        res = []
        for _node_ in self.tree:
            node = self.tree.get(_node_)
            for agrname in kwargs:
                if node.get(agrname) == kwargs.get(agrname):
                    res.append(node)
        return res

    class random_tree(self, depth=None, leafs=None):
        def __init__(self):
            for i in depth:
                pass





"""
catalog = tree()
catalog.add_node(parrent_id="0" , data='some text')
catalog.add_node(parrent_id="0" , data='some text 1' , gg='1')
catalog.add_node(parrent_id="0" , data='some text 1' , gg='1')
catalog.add_node(parrent_id="0.3" , data='some text 1' , gg='1')
print(catalog.get_nodes_by_params(parrent_id="0"))
print(catalog, '\n')
"""
