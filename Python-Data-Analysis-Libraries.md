# Python-Data-Analysis-Libraries

- Numpy
- Pandas
- Vaex
- [Modin](https://modin.readthedocs.io/en/stable/)
- Ray
- Fugue
- Spark
- [Datatable](https://github.com/h2oai/datatable)
- [Polars](https://github.com/pola-rs/polars)
- Dask



|Library | Multiprocessing | Distributed | Workload Capacity | Documentation|
|---|----|------|-----|-----|
| Pandas | No | No | < 50 GB | [Docs](https://github.com/pandas-dev/pandas) | 
| Numpy | No | No | < 200 GB | [Docs](https://github.com/numpy/numpy) | 
| Modin | Yes | Yes | < 5000 GB | [Docs](https://modin.readthedocs.io/en/stable/) | 
| Dask | Yes | Yes | < 50000 GB | [Docs](https://github.com/dask/dask) | 
| Ray | Yes | Yes | < 2000 GB | [Docs](https://github.com/ray-project/ray) | 
| PySpark | Yes | Yes | < 500000 GB | [Docs](https://github.com/apache/spark) | 
| Vaex | Yes | No | < 2000 GB | [Docs](https://github.com/vaexio/vaex) | 
| Datatable | Yes | No | < 200 GB | [Docs](https://github.com/h2oai/datatable) | 
| Polars | Yes | No | < 200 GB | [Docs](https://github.com/pola-rs/polars) | 
| cuDF | Yes | Yes | < 200 GB | [Docs](https://github.com/rapidsai/cudf) | 
| Fugue | Yes | Yes | < 200 GB | [Docs](https://github.com/rapidsai/cudf) | 



| Col1  | col2  | col3  | col4  | col5  |
|---|---|---|---|---|
| a  | d  | g  | j  |   |
| b  | e  | h  | k  |   |
| c  | f  | i  | l  |   |

### Benchmarks
As always, take these with a grain of sand. They are specific test cases that may not generalize well.
- https://h2oai.github.io/db-benchmark/

