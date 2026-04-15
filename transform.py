def transform_data(data):
    clean_data = []

    for record in data:
        rating = record.get('rating', {})

        new_record = {
            'product_id': record.get('id'),
            'title': record.get('title'),
            'price': record.get('price'),
            'category': record.get('category'),
            'rating': rating.get('rate'),
            'rating_count': rating.get('count')
        }

        clean_data.append(new_record)
    
    return clean_data