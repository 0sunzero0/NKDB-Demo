from elasticsearch import Elasticsearch

URL = "http://localhost:9200"
INDEX = "nkdb200531"

es = Elasticsearch(URL)


def getResult(temp_query):
    query_doc = {}
    query_doc['query'] = {
        "multi_match": {
            "query": temp_query,
            "fields": ["post_title", "post_body", "file_name", "file_extracted_content"],
            "tie_breaker": 0.2,
            "type": "best_fields"
        }
    }
    print(query_doc)
    result = es.search(index=INDEX, body=query_doc)
    #print(result)
    rawData = result["hits"]["hits"]

    length = len(rawData)
    print("###### es 보내준 문서의 갯수 : ", length)

    final_result = []

    for doc in rawData:
        print(doc)
        if  doc['_source'].get('file_name'):
            final_result.append(
                {
                    "_id": doc["_id"],
                    "post_title":doc["_source"]["post_title"],
                    "content": doc["_source"]["file_extracted_content"],
                    "file_name": doc["_source"]["file_name"],
                    "file_url": doc["_source"]["file_download_url"],
                    "post_date": doc["_source"]["post_date"],
                    "post_writer": doc["_source"]["post_writer"],
                    "published_institution_url": doc["_source"]["published_institution_url"],
                    "top_category": doc["_source"]["top_category"]
                }
            )
        else:
            final_result.append(
                {
                    "_id": doc["_id"],
                    "post_title": doc["_source"]["post_title"],
                    "content": doc["_source"]["post_body"],
                    "post_date": doc["_source"]["post_date"],
                    "post_writer": doc["_source"]["post_writer"],
                    "published_institution_url": doc["_source"]["published_institution_url"],
                    "top_category": doc["_source"]["top_category"]
                }
            )
    print(final_result)

    return final_result

temp_query = "북한 농업"
result_list = getResult(temp_query)
