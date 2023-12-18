import json
import requests
import csv

url = 'https://shopee.ph/api/v2/item/get_ratings?exclude_filter=1&filter=0&filter_size=0&flag=1&fold_filter=0&itemid=11286470426&limit=50&offset=6&relevant_reviews=false&request_source=2&shopid=54469408&tag_filter=&type=0&variation_filters='

data = requests.get(url)
html_text = data.text
json_data = json.loads(html_text)
comments_data = json_data['data']['ratings']

for item in comments_data:
	if len(item['comment']) > 50:
		with open(r'data.csv', 'a', newline='', encoding='utf-8') as csv_file:
			column_names = ['itemid', 'comment', 'rating_star']
			writer = csv.DictWriter(csv_file, fieldnames=column_names)
			writer.writerow({
				'itemid': item['itemid'],
				'comment': item['comment'],
				'rating_star': item['rating_star']
			})

print('Appended to CSV')