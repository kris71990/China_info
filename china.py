# This program stores information related to regions and cities in China in dicts and lists
# Through user interaction, it then presents the desired information 

import webbrowser, requests, bs4
from num2words import num2words
import chinadicts

def start():
	print(u'\n\u4f60\u597d, let\'s learn about China!')
	start_again()
			
def start_again():
	print("\nType 'province' or 'capital' for more information.")
	print("Type 'q' to quit.")
	prompt = input("> ").lower()
	while True:
		if prompt == 'province':
			province_info()
			more_info()
			break
		elif prompt == 'capital':
			capital_info()
			more_info()
			break
		elif prompt == 'q' or prompt == 'quit':
			print(u'\nHope you enjoyed learning about China, \u518d\u89c1!')
			exit(0)
		else:
			print("Type one of the keywords: ",)
			prompt = input()
	
def province_info():
	print("\nHere is a list of the " + num2words(len(provdicts.province)) + " provinces" \
			" in China and their abbreviations: \n")
	for prov, abbrev in sorted(provdicts.province.items()):
		if prov == "Taiwan":
			print("* %s --> %s" % (prov, abbrev))
		else:
			print("%s --> %s" % (prov, abbrev))
	
	print("\nAdditionally, here are the " + num2words(len(mundicts.municipality)) + \
			" municipalities and their abbreviations: \n")
	for mun, abbrev in sorted(mundicts.municipality.items()):
		print("%s --> %s" % (mun, abbrev))
	
	print("\nHere are the " + num2words(len(autregdicts.autregion)) + " autonomous regions" \
			" and their abbreviations: \n")
	for autreg, abbrev in sorted(autregdicts.autregion.items()):
		print("%s --> %s" % (autreg, abbrev))
	
	print("\nThese are the " + num2words(len(admregdicts.admregion)) + " Special Adminstrative" \
			" Regions and their abbreviations: \n")
	for admreg, abbrev in sorted(admregdicts.admregion.items()):
		print("%s --> %s" % (admreg, abbrev))

def capital_info():
	print("\nHere is a list of each province's capital: \n")
	for province, capital in sorted(provdicts.prov_capitals.items()):
		if province == "Taiwan":
			print("* %s --> %s" % (province, capital))
		else:
			print("%s --> %s" % (province, capital))
	
	print("\nHere is each municipality's capital: \n")
	for mun, capital in sorted(mundicts.mun_capitals.items()):
		print("%s --> %s" % (mun, capital))
		
	print("\nCapitals of Autonomous Regions: \n")
	for autregion, capital in sorted(autregdicts.autregion_capitals.items()):
		print("%s --> %s" % (autregion, capital))
		
	print("\nCapitals of Special Administrative Regions: \n")
	for admregion, capital in sorted(admregdicts.admregion_capitals.items()):
		print("%s --> %s" % (admregion, capital))
	
def more_info():
	provinces = []
	province_abbrev = []
	prov_capital = []
	municipalities = []
	mun_abbrev = []
	mun_capital = []
	autregions = []
	aut_abbrev = []
	autregion_cap = []
	admregions = []
	adm_abbrev = []
	admregion_capital = []
	
	for key, value in sorted(provdicts.province.items()):
		provinces.append(key)
		province_abbrev.append(value)
	for key, value in sorted(provdicts.prov_capitals.items()):
		prov_capital.append(value)
	for key, value in sorted(mundicts.municipality.items()):
		municipalities.append(key)
		mun_abbrev.append(value)
	for key, value in sorted(mundicts.mun_capitals.items()):
		mun_capital.append(value)
	for key, value in sorted(autregdicts.autregion.items()):
		autregions.append(key)
		aut_abbrev.append(value)
	for key, value in sorted(autregdicts.autregion_capitals.items()):
		autregion_cap.append(value)
	for key, value in admregdicts.admregion.items():
		admregions.append(key)
		adm_abbrev.append(value)
	for key, value in admregdicts.admregion_capitals.items():
		admregion_capital.append(value)
		
	while True:
		print("\nType a province's abbreviation for more information about each territory. ")
		print("For a list of province abbreviations, type 'province'.")
		print("Type 'q' to quit.")
		x = input("> ").lower()
		if x == 'q':
			print(u'\nHope you enjoyed learning about China, \u518d\u89c1!')
			exit(0)
		elif x == 'capital':
			capital_info()
			continue
		elif x == 'province':
			province_info()
			continue
		elif x == "ah":
			print_more_info_prov(provinces[0], province_abbrev[0], province_pop[0],
								 prov_pop_rank[0], prov_area[0], prov_area_rank[0], 
								 prov_capital[0], prov_cap_pop[0])
			continue
		elif x == "bj":
			print_more_info_muni(municipalities[0], mun_abbrev[0], muni_pop[0], muni_pop_rank[0],
								 muni_area[0], muni_area_rank[0], mun_capital[0], 
								 muni_cap_pop[0])
			continue
		elif x == "cq":
			print_more_info_muni(municipalities[1], mun_abbrev[1], muni_pop[1], muni_pop_rank[1],
								 muni_area[1], muni_area_rank[1], mun_capital[1], 
								 muni_cap_pop[1])
			continue
		elif x == "fj":
			print_more_info_prov(provinces[1], province_abbrev[1], province_pop[1],
								 prov_pop_rank[1], prov_area[1], prov_area_rank[1], 
								 prov_capital[1], prov_cap_pop[1])
			continue
		elif x == "gs":
			print_more_info_prov(provinces[2], province_abbrev[2], province_pop[2],
								 prov_pop_rank[2], prov_area[2], prov_area_rank[2], 
								 prov_capital[2], prov_cap_pop[2])
			continue
		elif x == "gd":
			print_more_info_prov(provinces[3], province_abbrev[3], province_pop[3],
								 prov_pop_rank[3], prov_area[3], prov_area_rank[3], 
								 prov_capital[3], prov_cap_pop[3])
			continue
		elif x == "gx":
			print_more_info_autreg(autregions[0], aut_abbrev[0], autregion_pop[0], autregion_pop_rank[0],
								   autregion_area[0], autregion_area_rank[0], autregion_cap[0],
								   autregion_cap_pop[0])
			continue
		elif x == "gz":
			print_more_info_prov(provinces[4], province_abbrev[4], province_pop[4],
								 prov_pop_rank[4], prov_area[4], prov_area_rank[4], 
								 prov_capital[4], prov_cap_pop[4])
			continue
		elif x == "hi":
			print_more_info_prov(provinces[5], province_abbrev[5], province_pop[5],
								 prov_pop_rank[5], prov_area[5], prov_area_rank[5], 
								 prov_capital[5], prov_cap_pop[5])
			continue
		elif x == "he":
			print_more_info_prov(provinces[6], province_abbrev[6], province_pop[6],
								 prov_pop_rank[6], prov_area[6], prov_area_rank[6], 
								 prov_capital[6], prov_cap_pop[6])
			continue
		elif x == "hl":
			print_more_info_prov(provinces[7], province_abbrev[7], province_pop[7],
								 prov_pop_rank[7], prov_area[7], prov_area_rank[7], 
								 prov_capital[7], prov_cap_pop[7])
			continue
		elif x == "ha":
			print_more_info_prov(provinces[8], province_abbrev[8], province_pop[8],
								 prov_pop_rank[8], prov_area[8], prov_area_rank[8], 
								 prov_capital[8], prov_cap_pop[8])
			continue
		elif x == "hk":
			print_more_info_admreg(admregions[0], adm_abbrev[0], admregion_pop[0],
								   admregion_pop_rank[0], admregion_area[0], 
								   admregion_area_rank[0], admregion_capital[0], 
								   admregion_pop[0])
			continue
		elif x == "hb":
			print_more_info_prov(provinces[9], province_abbrev[9], province_pop[9],
								 prov_pop_rank[9], prov_area[9], prov_area_rank[9], 
								 prov_capital[9], prov_cap_pop[9])
			continue
		elif x == "hn":
			print_more_info_prov(provinces[10], province_abbrev[10], province_pop[10],
								 prov_pop_rank[10], prov_area[10], prov_area_rank[10], 
								 prov_capital[10], prov_cap_pop[10])
			continue
		elif x == "nm":
			print_more_info_autreg(autregions[1], aut_abbrev[1], autregion_pop[1], 
								   autregion_pop_rank[1], autregion_area[1], 
								   autregion_area_rank[1], autregion_cap[1], autregion_cap_pop[1])
			continue	
		elif x == "js":
			print_more_info_prov(provinces[11], province_abbrev[11], province_pop[11],
								 prov_pop_rank[11], prov_area[11], prov_area_rank[11], 
								 prov_capital[11], prov_cap_pop[11])
			continue
		elif x == "jx":
			print_more_info_prov(provinces[12], province_abbrev[12], province_pop[12],
								 prov_pop_rank[12], prov_area[12], prov_area_rank[12], 
								 prov_capital[12], prov_cap_pop[12])
			continue
		elif x == "jl":
			print_more_info_prov(provinces[13], province_abbrev[13], province_pop[13],
								 prov_pop_rank[13], prov_area[13], prov_area_rank[13], 
								 prov_capital[13], prov_cap_pop[13])
			continue
		elif x == "ln":
			print_more_info_prov(provinces[14], province_abbrev[14], province_pop[14],
								 prov_pop_rank[14], prov_area[14], prov_area_rank[14], 
								 prov_capital[14], prov_cap_pop[14])
			continue
		elif x == "mc":
			print_more_info_admreg(admregions[1], adm_abbrev[1], admregion_pop[1],
								   admregion_pop_rank[1], admregion_area[1], 
								   admregion_area_rank[1], admregion_capital[1], admregion_pop[1])
			continue
		elif x == "nx":
			print_more_info_autreg(autregions[2], aut_abbrev[2], autregion_pop[2], 
								   autregion_pop_rank[2], autregion_area[2], 
								   autregion_area_rank[2], autregion_cap[2], autregion_cap_pop[2])
			continue
		elif x == "qh":
			print_more_info_prov(provinces[15], province_abbrev[15], province_pop[15],
								 prov_pop_rank[15], prov_area[15], prov_area_rank[15], 
								 prov_capital[15], prov_cap_pop[15])
			continue
		elif x == "sn":
			print_more_info_prov(provinces[16], province_abbrev[16], province_pop[16],
								 prov_pop_rank[16], prov_area[16], prov_area_rank[16], 
								 prov_capital[16], prov_cap_pop[16])
			continue
		elif x == "sd":
			print_more_info_prov(provinces[17], province_abbrev[17], province_pop[17],
								 prov_pop_rank[17], prov_area[17], prov_area_rank[17], 
								 prov_capital[17], prov_cap_pop[17])
			continue
		elif x == "sh":
			print_more_info_muni(municipalities[2], mun_abbrev[2], muni_pop[2], 
								 muni_pop_rank[2], muni_area[2], muni_area_rank[2], 
								 mun_capital[2], muni_cap_pop[2])
			continue
		elif x == "sx":
			print_more_info_prov(provinces[18], province_abbrev[18], province_pop[18],
								 prov_pop_rank[18], prov_area[18], prov_area_rank[18], 
								 prov_capital[18], prov_cap_pop[18])
			continue
		elif x == "sc":
			print_more_info_prov(provinces[19], province_abbrev[19], province_pop[19],
								 prov_pop_rank[19], prov_area[19], prov_area_rank[19], 
							 	 prov_capital[19], prov_cap_pop[19])
			continue
		elif x == "tw":
			print_more_info_prov(provinces[20], province_abbrev[20], province_pop[20],
								 prov_pop_rank[20], prov_area[20], prov_area_rank[20], 
								 prov_capital[20], prov_cap_pop[20])
			continue
		elif x == "tj":
			print_more_info_muni(municipalities[3], mun_abbrev[3], muni_pop[3], 
							     muni_pop_rank[3], muni_area[3], muni_area_rank[3], 
							     mun_capital[3], muni_cap_pop[3])
			continue
		elif x == "xz":
			print_more_info_autreg(autregions[3], aut_abbrev[3], autregion_pop[3], 
								   autregion_pop_rank[3], autregion_area[3], 
								   autregion_area_rank[3], autregion_cap[3],
								   autregion_cap_pop[3])
			continue
		elif x == "xj":
			print_more_info_autreg(autregions[4], aut_abbrev[4], autregion_pop[4], 
								   autregion_pop_rank[4], autregion_area[4], 
								   autregion_area_rank[4], autregion_cap[4],
								   autregion_cap_pop[4])
			continue
		elif x == "yn":
			print_more_info_prov(provinces[21], province_abbrev[21], province_pop[21],
								 prov_pop_rank[21], prov_area[21], prov_area_rank[21], 
								 prov_capital[21], prov_cap_pop[21])
			continue
		elif x == "zj":
			print_more_info_prov(provinces[22], province_abbrev[22], province_pop[22],
								 prov_pop_rank[22], prov_area[22], prov_area_rank[22], 
								 prov_capital[22], prov_cap_pop[22])
			continue
		else:
			print("Type a province abbreviation, or 'q' to quit: ")
			x = input("> ").lower()
			if x == 'q':
				print(u'\nHope you enjoyed learning about China, \u518d\u89c1!')
				exit(0)

def print_more_info_prov(p, pab, pp, ppr, pa, par, pc, pcp):
	print("\nHere is some information about %s:\n" % p)
	print("Abbreviation: %s" % pab)
	print("Population: %s (%s)" % (pp, ppr))
	print("Area: %s square km (%s)" % (pa, par))
	print("Capital: %s" % pc)
	print("Population of %s: %s" % (pc, pcp))
	print("\nType 'wiki' to read even more about %s! " % p)
	wiki = input().lower()
	if wiki == 'wiki':
		webbrowser.open("https://en.wikipedia.org/wiki/%s" % p)
		webbrowser.open("https://en.wikipedia.org/wiki/%s" % pc)
	
def print_more_info_muni(m, mab, mp, mpr, ma, mar, mc, mcp):
	print("\nHere is some information about %s:\n" % m)
	print("Abbreviation: %s" % mab)
	print("Population: %s (%s)" % (mp, mpr))
	print("Area: %s square km (%s)" % (ma, mar))
	print("Capital: %s" % mc)
	print("Population of %s: %s" % (mc, mcp))
	print("\nType 'wiki' to read even more about %s! " % m)
	wiki = input().lower()
	if wiki == 'wiki':
		webbrowser.open("https://en.wikipedia.org/wiki/%s" % m)
	
def print_more_info_autreg(aur, aurab, aurp, aurpr, aura, aurar, aurc, aurcp):
	print("\nHere is some information about %s Autonomous Region:\n" % aur)
	print("Abbreviation: %s" % aurab)
	print("Population: %s (%s)" % (aurp, aurpr))
	print("Area: %s square km (%s)" % (aura, aurar))
	print("Capital: %s" % aurc)
	print("Population of %s: %s" % (aurc, aurcp))
	print("\nType 'wiki' to read even more about %s! " % aur)
	wiki = input().lower()
	if wiki == 'wiki':
		webbrowser.open("https://en.wikipedia.org/wiki/%s" % aur)
		webbrowser.open("https://en.wikipedia.org/wiki/%s" % aurc)

def print_more_info_admreg(admr, admrab, admrp, admrpr, admra, admrar, admrc, admrcpr):
	print("\nHere is some information about %s:\n" % admr)
	print("Abbreviation: %s" % admrab)
	print("Population: %s (%s)" % (admrp, admrpr))
	print("Area: %s square km (%s)" % (admra, admrar))
	print("Capital: %s" % admrc)
	print("Population of %s: %s" % (admr, admrcpr))
	print("\nType 'wiki' to read even more about %s! " % admr)
	wiki = input().lower()
	if wiki == 'wiki':
		webbrowser.open("https://en.wikipedia.org/wiki/%s" % admr)

start()


