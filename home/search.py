def res_format(res):
    keys = ['one_br', 'two_br', 'three_br', 'studio', 'rooms']
    ref = dict()
    if res:
        for key in keys:
            ref[key] = key in res
        return ref
    return res

def name_search(query, name):
    for obj in query:
        if not name.lower() in obj.entity.lower():
            query = query.exclude(entity=obj.entity)
    return query

def prices(query, low, high):
    for obj in query:
        if not obj.low >= low and obj.high <= high:
            query = query.exclude(entity=obj.entity)
    return query

def filter_res(query, res):
    res = {k:v for k, v in res.items() if v==True}

    #KEYS are [one_br, two_br, three_br, rooms, studio]
    for obj in query:
        switch = True
        for key in res:
            if switch:
                if key == 'rooms':
                    switch = obj.rooms
                elif key == 'one_br':
                    switch = obj.one_br
                elif key == 'two_br':
                    switch = obj.two_br
                elif key == 'three_br':
                    switch = obj.three_br
                elif key == 'studio':
                    switch = obj.studio
        if not switch:
            query = query.exclude(entity=obj.entity)
    return query

def search(queryset, fields, q_type):
    results = queryset

    low = fields.get('low', False)
    high = fields.get('high', False)

    if high and low:
        low = int(fields.get('low', False))
        high = int(fields.get('high', False))
        if high < low:
            return None
        results = prices(results, low, high)

    zipcode = fields.get('zip', False)
    name = fields.get('name', False)
    res = res_format(fields.getlist('res', False))
    area = fields.get('area', False)

    if zipcode and len(zipcode) == 5:
        results = results.filter(zipcode=zipcode)
    if res:
        if fields.get('strict', False):
            # Strict combo search, only matches if fields are exactly True/False matching
            results = results.filter(one_br=res['one_br'])\
                             .filter(two_br=res['two_br'])\
                             .filter(three_br=res['three_br'])\
                             .filter(rooms=res['rooms'])\
                             .filter(studio=res['studio'])
        else:
            # "At least" Algorithm, less strict, does not search if field is false
            results = filter_res(results, res)
    if q_type == 'apt' and area != 'none':
        results = results.filter(area=area)
    if name:
        results = name_search(results, name)
    return results
