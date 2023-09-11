global_var=10

def my_fun():
    local_var=30
    print('local variable',local_var)
    print('global variable',global_var)

my_fun()   
print('outside fun',global_var)