'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''


def compact(truthy_list):
    return [x for x in truthy_list if x]
