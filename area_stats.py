import requests
import pegasus_functions as pf
from datetime import datetime
from pprint import pprint
import json

eov_packet = pf.get_eov_packet()
obis_areas = requests.get("https://api.obis.org/area").json()

area_stats_cache = list()

for i_eov,eov in enumerate(eov_packet):
    if i_eov > 0:
        break

    for i_area,area in enumerate(obis_areas["results"]):
        area_stats = pf.summary_stats_by_aphiaids(pf.get_worms_info(eov["name"])["valid_aphiaids"], summary_type="statistics/all", area_id=area["id"])

        for k, v in area.items():
            area_stats[f"area_{k}"] = v
        for k, v in eov.items():
            area_stats[f"eov_{k}"] = v

        area_stats["area_records_per_year"] = pf.summary_stats_by_aphiaids(pf.get_worms_info(eov["name"])["valid_aphiaids"], summary_type="statistics/years", area_id=area["id"])
        area_stats["date_cached"] = datetime.utcnow().isoformat()

        area_stats_cache.append(area_stats)

    with open(f'area_stats_{eov["name"]}.json', 'w') as f:
        f.write(json.dumps(area_stats_cache))
        
