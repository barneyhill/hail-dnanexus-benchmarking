# Benchmarking
## Spark Jupyter w/ 2x mem3_hdd2_v2_x4

```
bn_ds = hl.balding_nichols_model(3, 100000, 1000000)
dataset = hl.sample_qc(bn_ds, name='sample_qc')
dataset.show()
```
Over 5 runs average: 10.64s

```
bn_ds = hl.balding_nichols_model(3, 1000, 1000)
grm = hl.genetic_relatedness_matrix(bn_ds.GT)
```
Over 5 runs average: 8.93s

## hail-minimal w/ mem3_hdd2_v2_x8

```
bn_ds = hl.balding_nichols_model(3, 100000, 1000000)
dataset = hl.sample_qc(bn_ds, name='sample_qc')
dataset.show()
```
Over 5 runs average: 4.74s
```
bn_ds = hl.balding_nichols_model(3, 1000, 1000)
grm = hl.genetic_relatedness_matrix(bn_ds.GT)
```
Over 5 runs average: 0.91s
