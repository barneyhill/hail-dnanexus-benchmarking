import time
import pyspark
import dxpy
import hail as hl

my_database = dxpy.find_one_data_object(
    name="my_database", 
    project=dxpy.find_one_project()["id"]
)["id"]
database_dir = f'dnax://{my_database}'
sc = pyspark.SparkContext()
spark = pyspark.sql.SparkSession(sc)
hl.init(sc=sc, tmp_dir=f'{database_dir}/tmp/')

t1 = time.time()
hl.set_global_seed(1)
bn_ds = hl.balding_nichols_model(3, 100000, 1000000)
t1 = time.time()
dataset = hl.sample_qc(bn_ds, name='sample_qc')
dataset.show()
print(time.time()-t1)
