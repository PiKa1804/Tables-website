from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch()

def Download(name, name1):            #get the data from elasticsearch indices and types
    result_list=[]
    size=[]
    doc = {'query': {'match_all' : {}}}
    res = es.search(index=name,doc_type=name1,body=doc)
    size=res['hits']['total']
    res = es.search(index=name,doc_type=name1,body=doc,size=size)
    ala=[]
    ind=[]
    for i in range(0,size):
        ala.append(res['hits']['hits'][i]['_source'])
        ind.append(res['hits']['hits'][i]['_id'])

    res2 = ala.copy()
    result_list=[]
    for i in range(0,size):
        result_list.append([v for k,v in res2[i].items()])
        result_list[i].append(ind[i])
    size=len(result_list)+1

    return result_list, size

def Change(name, name1, firm, ident, ind):    #search and change specific document in the types
    result_list2=[]
    size2=[]
    actions = [
              {
                '_op_type': 'update',
                '_index': name,
                '_type': name1,
                '_id': ind,
                'doc': {'nsk': firm,
                        'id':ident
                        }
              }

            ]
    helpers.bulk(es, actions)
    doc2 = {'query': {'match_all' : {}}}
    res2 = es.search(index=name,doc_type=name1,body=doc2)
    size2=res2['hits']['total']
    res2 = es.search(index=name,doc_type=name1,body=doc2,size=size2)
    ala2=[]
    ind2=[]
    for i in range(0,size2):
        ala2.append(res2['hits']['hits'][i]['_source'])
        ind2.append(res2['hits']['hits'][i]['_id'])
    res3 = ala2.copy()
    result_list2=[]
    for i in range(0,size2):
        result_list2.append([v for k,v in res3[i].items()])
        result_list2[i].append(ind2[i])
    size2=len(result_list2)#get the changed data

    return result_list2, size2