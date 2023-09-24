def avarage(values):
    if values:
        return sum(values)/len(values)
    else:
        return None
    
if __name__ == '__main__':
    print("__name__ ->",__name__)
    print("test 1 should be None", avarage([]))
    print("test 2 should be 1", avarage([1]))
    print("test 3 should be 2", avarage([1,2,3]))