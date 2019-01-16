class MinStack:
    def __init__(self):
        self.mainStack = []
        self.minStack = []

    # @param x, an integer
    def push(self, x):
        if not self.minStack or x<=self.minStack[-1]:
            self.minStack.append(x)
        self.mainStack.append(x)

    # @return nothing
    def pop(self):
        if self.mainStack:
            x = self.mainStack.pop()
            if self.minStack and x == self.minStack[-1]:
                self.minStack.pop()
    

    # @return an integer
    def top(self):
        if self.mainStack:
            return self.mainStack[-1]
        else:
            return -1        

    # @return an integer
    def getMin(self):
        if self.minStack:
            return self.minStack[-1]
        else:
            return -1