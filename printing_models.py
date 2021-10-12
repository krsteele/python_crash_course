from printing_functions import print_models as pm 
from printing_functions import show_completed_models as scm

unprinted_designs = ['baby yoda', 'phone case', 'robot', 'flip-flop pendant']
completed_models = []

pm(unprinted_designs, completed_models)
scm(completed_models)