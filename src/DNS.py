import requests as r


class DeNobiliKoradih:
	intro = 'De Nobili School, Koradih is a private Catholic primary and secondary school located in Koradhi in the Dhanbad district of Jharkhand, India. Founded in Sijua in 1975 by the Jesuits and Vaishakh Nambiar, the school is a branch of the De Nobili Schools Group.'
	type = 'Private primary and secondary school'
	motto = 'Knowledge Imparts Humility'
	logo = 'The De Nobili School shield displays part of a Sanskrit slogan Vidya Dadati Vinayam (Education Bestows Humility) in Devanagari script in the scroll under the school shield.'
	currentPrincipal = 'Tanushree Banerjee'
	origin = 'The school is named after a christian missionary and Jesuit, Roberto de Nobili, who was the first foreigner to master Sanskrit, incognito, in sixteenth century Madurai. He apparently conducted himself like an orthodox Brahmin and is even said to have declared himself to be a descendant of Brahma.'
	board = 'ICSE'
	website = 'www.dnssijua.com'
	principals = ['V. J. Abraham','Xavier Joseph','Joy Matthew','G. Thomas Kennedy','Tanushree Banerjee']
	schoolSong = '''Oh De Nobili hats off to thee;
To your colours true we shall ever be; 
firm and strong united are we;
Rah, rah, rah. For DNS;
Rah, rah, rah, rah;
Rah, for De Nobili;


Hail, to the victors valiant,
Hail, to the conquering heroes,
Hail, Hail, De Nobili,
the leaders and the best;
Hail to the victors valiant,
Hail to the conquering heroes
Hail, Hail, De Nobili,
the champions and the best.'''
	teachers = 'Note : As per 2018-19.\n' + str(r.get('https://raw.githubusercontent.com/advwastaken/dnssijua-teachers-2018/main/teachers.txt').text.replace('\n','').split(','))
	
	@classmethod
	def getTeachersWith(self, ctx):
		return 'Note : As per 2018-19.\n' + str([teacher for teacher in DeNobili.teachers if teacher.lower().startswith(ctx.lower())])

