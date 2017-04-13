def verify(post):
    error_msg = []
    low = post.get('low', False)
    high = post.get('high', False)
    ziplen = len(post.get('zip', False))

    if ziplen and ziplen != 5:
        error_msg.append('Zip code has less than 5 digits.')
    if high and low and (int(low) > int(high)):
        error_msg.append('The low price range is greater than the high price range')
    return error_msg

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
        if not (obj.low >= low and obj.high <= high):
            print('removed')
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

def search(queryset, post, q_type):
    results = {
        'feedback': []
    }
    exception = post.get('exception', False)
    low = post.get('low', False)
    high = post.get('high', False)

    if exception:
        queryset = queryset.filter(low=0).filter(high=0)
        results['feedback'].append('Price range exception: Yes')
    else:
        if high and low:
            results['feedback'].append('Price range: $' + low + ' - $' + high)
            low = int(post.get('low', False))
            high = int(post.get('high', False))
            queryset = prices(queryset, low, high)

    zipcode = post.get('zip', False)
    name = post.get('name', False)
    res = res_format(post.getlist('res', False))
    area = post.get('area', False)

    if zipcode:
        results['feedback'].append('Zipcode: ' + zipcode)
        queryset = queryset.filter(zipcode=zipcode)
    if res:
        res_true = {k:v for k, v in res.items() if v==True}
        keys = [k.replace('one_br', '1BR').replace('two_br', '2BR').replace('three_br', '3BR') for k in list(res_true.keys())]
        results['feedback'].append('Residence: ' + ', '.join(keys))
        if post.get('strict', False):
            results['feedback'].append('Residence parameter strict')
            # Strict combo search, only matches if fields are exactly True/False matching
            queryset = queryset.filter(one_br=res['one_br'])\
                             .filter(two_br=res['two_br'])\
                             .filter(three_br=res['three_br'])\
                             .filter(rooms=res['rooms'])\
                             .filter(studio=res['studio'])
        else:
            results['feedback'].append('Residence parameter non-strict')
            # "At least" Algorithm, less strict, does not search if field is false
            queryset = filter_res(queryset, res)
    if q_type == 'apt' and area != 'none':
        queryset = queryset.filter(area=area)
        results['feedback'].append('Area: ' + area)
    if name:
        queryset = name_search(queryset, name)
        results['feedback'].append('Name: ' + name)
    results['queryset'] = queryset

    return results
