import requests
import json


def get_eov_packet():
    with open('eov_packet.json', 'rb') as f:
        eov_packet = json.loads(f.read())
        
    return eov_packet


def worms_info_from_names(name_list):
    response_package = {
        "worms_responses": list(),
        "valid_aphiaids": list()
    }

    for taxon_name in name_list:
        this_record = {
            "list_name": taxon_name,
            "worms_search_url": f"http://www.marinespecies.org/rest/AphiaRecordsByName/{taxon_name}?like=true&marine_only=false&offset=1"
        }
        try:
            this_record["worms_response"] = requests.get(this_record["worms_search_url"]).json()
            response_package["valid_aphiaids"].append(next((i["valid_AphiaID"] for i in this_record["worms_response"]), None))
        except:
            this_record["worms_response"] = None
        response_package["worms_responses"].append(this_record)
        response_package["valid_aphiaids"] = [x for x in response_package["valid_aphiaids"] if x is not None]
        response_package["valid_aphiaids"] = list(set(response_package["valid_aphiaids"]))
        
    return response_package


def get_worms_info(eov_group):
    with open(f"{eov_group}.json", "rb") as f:
        data = json.loads(f.read())

    return data


def summary_stats_by_aphiaids(aphia_ids, summary_type="statistics", area_id=None):
    valid_summary_types = [
        "statistics",
        "statistics/years",
        "statistics/all",
        "statistics/env",
        "institute",
        "dataset"
    ]
    if summary_type not in valid_summary_types:
        return None
    
    if len(aphia_ids) > 1:
        query_string = '&taxonid='.join([str(i) for i in aphia_ids])
    else:
        query_string = aphia_ids[0]

    url = f"https://api.obis.org/{summary_type}?taxonid={query_string}"
    
    if summary_type == "statistics/years":
        url = f"{url}&startdate=1900-01-01"
        
    if area_id is not None:
        url = f"{url}&areaid={area_id}"
        
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

