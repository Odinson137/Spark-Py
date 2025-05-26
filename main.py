from pyspark.sql import SparkSession

def get_product_category_pairs(products, categories, product_categories):
    product_with_categories = products.join(
        product_categories,
        products.product_id == product_categories.product_id,
        "left_outer"
    )
    result = product_with_categories.join(
        categories,
        product_with_categories.category_id == categories.category_id,
        "left_outer"
    )
    result = result.select(products.product_name, categories.category_name)
    return result

if __name__ == "__main__":
    spark = SparkSession.builder.appName("ProductCategoryPairs").getOrCreate()
    products_data = [(1, "Product A"), (2, "Product B"), (3, "Product C")]
    categories_data = [(1, "Category X"), (2, "Category Y")]
    product_categories_data = [(1, 1), (1, 2), (2, 1)]
    products = spark.createDataFrame(products_data, ["product_id", "product_name"])
    categories = spark.createDataFrame(categories_data, ["category_id", "category_name"])
    product_categories = spark.createDataFrame(product_categories_data, ["product_id", "category_id"])
    result_df = get_product_category_pairs(products, categories, product_categories)
    result_df.show()