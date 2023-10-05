# More on working with json and getting json results

from langchain.utilities.dataforseo_api_search import DataForSeoAPIWrapper
from decouple import config
import os

os.environ["DATAFORSEO_LOGIN"] = config("DATAFORSEO_LOGIN")
os.environ["DATAFORSEO_PASSWORD"] = config("DATAFORSEO_PASSWORD")

json_wrapper = DataForSeoAPIWrapper(
    json_result_types=["organic", "knowledge_graph", "answer_box"],
    json_result_fields=["type", "title", "description", "text"],
    top_count=3,
)

response = json_wrapper.results("What is the currently trending movie")

print(response)
