import time
import pyspark
import dxpy
import hail as hl

hl.init()

hl.set_global_seed(1)

times = []
for _ in range(5):
    bn_ds = hl.balding_nichols_model(3, 100000, 1000000)
    t1 = time.time()
    dataset = hl.sample_qc(bn_ds, name='sample_qc')
    dataset.show()
    times.append(time.time()-t1)
print("benchmark 1", sum(times)/5)

times = []
for _ in range(5):
    t1 = time.time()
    bn_ds = hl.balding_nichols_model(3, 1000, 1000)
    grm = hl.genetic_relatedness_matrix(bn_ds.GT)
    times.append(time.time()-t1)

print("benchmark 2", sum(times)/5)
