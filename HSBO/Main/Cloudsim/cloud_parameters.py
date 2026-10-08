import random


def cloud_compute(n_cnr, n_apn):

    def resource_allocate(nc, na, lb, ub):
        _array = []
        for i in range(nc):
            tem = []
            for j in range(na):
                tem.append(random.uniform(lb, ub))
            _array.append(tem)
        return _array

    ub = 10
    lb = 1
    CPU = resource_allocate(n_cnr, n_apn, lb, ub)
    Memory = resource_allocate(n_cnr, n_apn, lb, ub)
    Bandwidth = resource_allocate(n_cnr, n_apn, lb, ub)
    frequency = resource_allocate(n_cnr, n_apn, lb, ub)

    return CPU, Memory, Bandwidth, frequency
