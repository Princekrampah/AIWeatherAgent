from langchain.utilities.dataforseo_api_search import DataForSeoAPIWrapper
from decouple import config
import os

os.environ["DATAFORSEO_LOGIN"] = config("DATAFORSEO_LOGIN")
os.environ["DATAFORSEO_PASSWORD"] = config("DATAFORSEO_PASSWORD")

wrapper = DataForSeoAPIWrapper()

response = wrapper.run("What is the currently trending movie")

print(response)

response = wrapper.results("What is the currently trending movie")

print(response)

# difference between run and result methods
# https://python.langchain.com/docs/integrations/tools/dataforseo#the-difference-between-run-and-results