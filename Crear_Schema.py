from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

# Definir el schema con los cambios solicitados
mi_schema = StructType([
    StructField("Company_id", IntegerType(), True),  # Tipo entero
    StructField("Company_name", StringType(), True),  # Tipo cadena
    StructField("Sales_amount", FloatType(), True),  # Tipo flotante
    StructField("Import_amount", StringType(), True),  # Tipo cadena
    StructField("Export_amount", StringType(), True)  # Tipo cadena
])

# Leer el archivo CSV
df = spark.read.format("csv") \
    .option("delimiter", ";") \
    .option("header", "true") \
    .schema(mi_schema) \
    .load("data.csv")

# Mostrar el DataFrame
df.show()
