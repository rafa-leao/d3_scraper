from scraper.robot import Robot

if __name__ == '__main__':

	print("Scraping...")

	paths = Robot().paths_catcher()
	
	print("-*-------------*-------------*-------------*-------------*-------------*-")
	print("ALL ALLOWED PATHS ==> ", paths)
	print("-*-------------*-------------*-------------*-------------*-------------*-")

	print(Robot().path_assets_catcher(paths))

	print("-*-------------*-------------*-------------*-------------*-------------*-")
	print("-*   Copy this huge return and paste on: http://jsonviewer.stack.hu/   *-")
	print("-*-------------*-------------*-------------*-------------*-------------*-")