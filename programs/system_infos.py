import os, pprint

def get_env_var(var):
    env_var = os.environ.get(var)
    return env_var

def cpu_infos():
    print('ALL CPU INFORMATIONS:')
    print('CPU Architecture:', get_env_var('PROCESSOR_ARCHITECTURE'))
    print('CPU Identifier:', get_env_var('PROCESSOR_IDENTIFIER'))
    print('CPU Level:', get_env_var('OS'))
    print('CPU Revision:', get_env_var('OS'))
    #mettre aussi l'utilisation actuelle du cpu
    
def os_infos():
    print("ALL OS INFORMATIONS:")
    print('OS:', get_env_var('OS'))
    #finir le reste des informations sur l'os
    
def all_env_var():
    env_var = os.environ
    pprint.pprint(dict(env_var))
all_env_var()
       
    
def get_all_infos():
    return
