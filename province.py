# python 3.5; province.py
# a province class that creates instances of Chinese provinces
# info is parsed from wikipedia and is presented when the user asks for it

import requests, bs4, chinadicts

class Province:

    def __init__(self, province):
        self.province = province
        self.prov_dict = {}

    # information gathered from wikipedia, organinized into two lists, and then returned in a dictionary of
    # basic facts about the specific province
    def get_prov_info(self):
        res = requests.get('https://en.wikipedia.org/wiki/%s' % self.province)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        info_data = soup.select('.mergedrow td')
        info_head = soup.select('.mergedrow th')
        head_text = []
        data_text = []

        for each in info_head:
            entry = each.get_text()
            entry = entry.replace(u'\xa0', u'')
            entry = entry.replace(u'\u2022', u'')
            head_text.append(entry)
        for each in info_data:
            entry = each.get_text()
            entry = entry.replace(u'\xa0', u'')
            entry = entry.replace(u'/', u' ')
            entry = entry.replace(u'\n', u'; ')
            data_text.append(entry)

        zipped_list = zip(head_text, data_text)
        self.prov_dict = dict(zipped_list)
        return self.prov_dict

    # information from the info function is printed via this method
    def print_info(self):
        print('\nHere is some more information about %s Province: ' % self.province)
        print('\nName: %s' % self.prov_dict.get('Chinese'))
        print('Abbreviation: %s' % self.prov_dict.get('Abbreviation'))
        print('Capital: %s' % chinadicts.prov_cap.get(self.province))
        print('Largest City: %s' % self.prov_dict.get('Largest city'))
        print('Population: %s' % self.prov_dict.get('Total'))
        print('Population Rank: %s' % self.prov_dict.get('Rank'))
        print('Population Density: %s' % self.prov_dict.get('Density'))
        print('Population Density Rank: %s' % self.prov_dict.get('Densityrank'))
        print('Area Rank: %s' % self.prov_dict.get('Area rank'))
        print('Secretary: %s' % self.prov_dict.get('Secretary'))
        print('Governor: %s' % self.prov_dict.get('Governor'))
        print('Per Capita GDP: %s' % self.prov_dict.get(' per capita'))
        print('Ethnic Composition: %s' % self.prov_dict.get('Ethnic composition'))
        print('Languages and Dialects: %s' % self.prov_dict.get('Languages and dialects'))
        print('Divisions: %s\n' % self.prov_dict.get('Divisions'))



class AutReg(Province):

    def print_info(self):
        print('\nHere is some more information about %s Autonomous Region: ' % self.province)
        print('\nName: %s' % self.prov_dict.get('Chinese'))
        print('Abbreviation: %s' % self.prov_dict.get('Abbreviation'))
        print('Capital: %s' % chinadicts.prov_cap.get(self.province))
        print('Largest City: %s' % self.prov_dict.get('Largest city'))
        print('Population: %s' % self.prov_dict.get('Total'))
        print('Population Rank: %s' % self.prov_dict.get('Rank'))
        print('Population Density: %s' % self.prov_dict.get('Density'))
        print('Population Density Rank: %s' % self.prov_dict.get('Densityrank'))
        print('Area Rank: %s' % self.prov_dict.get('Area rank'))
        print('Secretary: %s' % self.prov_dict.get('Secretary'))
        print('Governor: %s' % self.prov_dict.get('Governor'))
        print('Per Capita GDP: %s' % self.prov_dict.get(' per capita'))
        print('Ethnic Composition: %s' % self.prov_dict.get('Ethnic composition'))
        print('Languages and Dialects: %s' % self.prov_dict.get('Languages'))
        print('Divisions: %s\n' % self.prov_dict.get('Divisions'))


class AdmReg(Province):
    
    def print_info(self):
        print('\nHere is some more information about %s Administrative Region: ' % self.province)
        print('\nName: %s' % self.prov_dict.get('Chinese'))
        print('Abbreviation: %s' % self.prov_dict.get('Abbreviation'))
        print('Capital: %s' % chinadicts.prov_cap.get(self.province))
        print('Largest City: %s' % self.prov_dict.get('Largest city'))
        print('Population: %s' % self.prov_dict.get('Total'))
        print('Population Rank: %s' % self.prov_dict.get('Rank'))
        print('Population Density: %s' % self.prov_dict.get('Density'))
        print('Population Density Rank: %s' % self.prov_dict.get('Densityrank'))
        print('Area Rank: %s' % self.prov_dict.get('Area rank'))
        print('Secretary: %s' % self.prov_dict.get('Secretary'))
        print('Governor: %s' % self.prov_dict.get('Governor'))
        print('Per Capita GDP: %s' % self.prov_dict.get(' per capita'))
        print('Ethnic Composition: %s' % self.prov_dict.get('Ethnic composition'))
        print('Languages and Dialects: %s' % self.prov_dict.get('Languages'))
        print('Divisions: %s\n' % self.prov_dict.get('Divisions'))


prov = input("Choose a province: ")
x = AdmReg(prov)
x.get_prov_info()
x.print_info()



