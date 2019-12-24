# python3

class Database:
    def __init__(self, tablesLen):
        self.tablesLen = tablesLen
        self.maxLen = max(tablesLen)
        n_tables = len(tablesLen)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, dst, src):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)
#        print("dis parent {} <== src parent {}".format(dst_parent, src_parent))
        if src_parent == dst_parent:
            return False
        #exchange source with destination according to the rank of each
        if (self.ranks[dst_parent] <= self.ranks[src_parent]):
            dst_parent, src_parent = src_parent, dst_parent
            if self.ranks[dst_parent] == self.ranks[src_parent]:
                self.ranks[dst_parent] += self.ranks[src_parent]
        #Change tables sizes
        self.tablesLen[dst_parent] += self.tablesLen[src_parent]
        self.tablesLen[src_parent] = 0
        #Check which is maximum in size
        if self.tablesLen[dst_parent] > self.maxLen:
            self.maxLen = self.tablesLen[dst_parent]
        #Add a symbolic link to the source table
        self.parents[src_parent] = dst_parent
        return True

    def get_parent(self, table):
        # find parent and compress path
        if table != self.parents[table]:
            self.parents[table] = self.get_parent(self.parents[table])
        return self.parents[table]
    
#    iterative impelmentation of get_parent
#    def get_parent(self, table):
#        tempTable = table
#        #get parent for the table
#        while table != self.parents[table]:
#            table = self.parents[table]
#            
#        parentTable = table
#        table = tempTable
#        
#        #update all parents in the branch
#        while table != self.parents[table]:
#            table = self.parents[table]
#            self.parents[table] = parentTable
#    
#        return parentTable


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
#    print("Parents :", db.parents)
#    print("tables size:", db.tablesLen)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
#        print("Parents :", db.parents)
#        print("tables size:", db.tablesLen)
        print(db.maxLen)


if __name__ == "__main__":
    main()
