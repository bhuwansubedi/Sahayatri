from re import L
from this import d
from unicodedata import name
from django.core.management.base import BaseCommand
from ...models import Municipality,District,Province

class Command(BaseCommand):
    new_address = [
    {
        "province": "Province 1",
        "district": [
            {"name": "Taplejung", "municipalities": ["Phungling","Aathrai Tribeni","Sidingwa","Phaktanglung","Mikkwakhola","Meringden","Maiwakhola","Pathibhara Yangwarak","Sirijangha"]},
            {"name": "Panchthar", "municipalities": ["Phidim", "Phalelung", "Phalgunanda", "Hilihang", "Kummayak", "Miklajung", "Tumbewa", "Yangawarak"]},
            {"name": "Ilam", "municipalities": ["Ilam", "Deumai", "Mai", "Suryodaya", "Phakphokthum", "Chulachuli", "Mai Jogmai", "Mangsebung", "Rong", "Sandakpur"]},
            {"name": "Jhapa", "municipalities": ["Mechinagar", "Damak", "Kankai", "Bhadrapur", "Arjundhara", "Shivasatakshi", "Gauradaha", "Birtamod", "Kamal", "Gaurigunj", "Barhadashi", "Jhapa", "Buddhashanti", "Haldibari", "Kachankawal"]},
            {"name": "Morang", "municipalities": ["Biratnagar", "Belbari", "Letang", "Pathari-Sanischare", "Rangeli", "Ratuwamai", "Sunbarshi", "Urlabari", "SundarHaraicha", "Budiganga", "Dhanpalthan", "Gramthan", "Jahada", "Kanepokhari", "Katahari", "Kerabari", "Miklajung"]},
            {"name": "Sunsari", "municipalities": ["Itahari", "Dharan", "Inaruwa", "Duhabi", "Ramdhuni", "Barahachhetra", "Dewanganj", "Koshi", "Barju", "Bhokraha Narashingh", "Harinagara"]},
            {"name": "Dhankuta", "municipalities": ["Pakhribas", "Dhankuta", "Mahalaxmi", "Sangurigadhi", "Sahidbhumi", "Chhathar Jorpati", "Chaubise"]},
            {"name": "Tehrathum", "municipalities": ["Myanglung", "Laligurans", "Aathrai", "Chhathar", "Phedap", "Menchayam"]},
            {"name": "Sankhuwasabha", "municipalities": ["Chainpur", "Dharmadevi", "Khandbari", "Madi", "Panchkhapan", "Bhotkhola", "Chichila", "Makalu", "Savapokhari", "Silichong"]},
            {"name": "Bhojpur", "municipalities": ["Bhojpur", "Shadanand", "Temkemaiyung", "Ramprasad Rai", "Arun", "Pauwadungma", "Salpasilichho", "Aamchok", "Hatuwagadhi"]},
            {"name": "Solukhumbu", "municipalities": ["Solududhkunda", "Mapya Dudhkoshi", "Khumbu Pasanglhamu", "Thulung Dudhkosi", "Necha Salyan", "Maha Kulung", "Likhu Pike", "Sotang"]},
            {"name": "Okhakdhunga", "municipalities": ["Siddhicharan", "Khijiidemba", "Champadevi", "Chisankhugadhi", "Manebhanjyang", "Molung", "Likhu", "Sunkoshi"]},
            {"name": "Khotang", "municipalities": ["Halesi Tuwachung","Diktel Rupakot Majhuwagadhi","Aiselukharka","Rawabesi","Jantedhunga","Khotehang","Kepilasgadhi","Diprung","Saakela","Barahpokhari"]},
            {"name": "Udayapur", "municipalities": ["Katari","Belaka","Triyuga","Chaudandigadhi","Udayapurgadhi","Taapli","Rautamai","Limchungbung"]}
        ]
    },
    {
        "province": "Province 2",
        "district": [
            {"name": "Saptari", "municipalities": ["Rajbiraj","Kanchanrup","Dakneshwori","Bodebarsain", "Khadak", "Sambhunath", "Surunga", "Hanumannagar Kankalini", "Saptakoshi", "Agnisaira Krishnasavaran", "Chhinnamasta", "Mahadeva", "Tirhut", "Tilathi Koiladi", "Rupani", "Rajgadh", "Bishnupur", "Balan-Bihul"]},
            {"name": "Siraha", "municipalities": ["Lahan","Dhangadhimai","Siraha","Golbazar", "Mirchaiya", "Kalyanpur", "Karjanha", "Sukhipur", "Bhagwanpur", "Aurahi", "Bishnupur", "Bariyarpatti", "Lakshmipur Patari", "Naraha", "Sakhuwanankar Katti", "Arnama", "Navarajpur"]},
            {"name": "Dhanusha", "municipalities": ["Janakpur", "Chhireshwarnath", "Ganeshman Charanath", "Dhanusadham", "Nagarain", "Bideha", "Mithila", "Sahidnagar", "Sabaila", "Kamala", "Mithila Bihari", "Hansapur", "Janaknandani", "Bateshwar", "Mukhiyapatti Musharniya", "Lakshminya", "Aurahi", "Dhanauji"]},
            {"name": "Mahottari", "municipalities": ["Jaleshwor", "Bardibas", "Gaushala", "Loharpatti", "Ramgopalpur", "Manara Shiswa", "Matihani", "Bhangaha", "Balawa", "Aurahi", "Ekdara", "Sonama", "Samsi", "Mahottari", "Pipara"]},
            {"name": "Sarlahi", "municipalities": ["Ishworpur", "Malangwa", "Lalbandi", "Haripur", "Haripurwa", "Harion", "Barahathwa", "Balara", "Godaita", "Bagmati", "Kabilasi", "Chakraghatta", "Chandranagar", "Dhankaul", "Brahampuri", "Ramnagar", "Bishnu", "Kaudena", "Parsa", "Basbariya"]},
            {"name": "Rautahat", "municipalities": ["Chandrapur", "Garuda", "Gaur", "Baudhimai", "Brindaban", "Dewahi Gonahi", "Gadhimai", "Gujara", "Katahariya", "Madhav Narayan", "Maulapur", "Phatuwa Bijayapur", "Ishanath", "Paroha", "Rajpur", "Rajdevi", "Durga Bhagwati", "Yamunamai"]},
            {"name": "Bara", "municipalities": ["Kalaiya", "Jeetpur Simara", "Kolhabi", "Nijgadh", "Mahagadhimai", "Simraungadh", "Pacharauta", "Adarsh Kotwal", "Karaiyamai", "Devtal", "Parwanipur", "Prasauni", "Pheta", "Baragadhi", "Suwarna", "Bishrampur"]},
            {"name": "Parsa", "municipalities": ["Birgunj", "Pokhariya", "Bahudarmai", "Parsagadhi", "Thori", "Jagarnathpur", "Dhobini", "Chhipaharmai", "Pakaha Mainpur", "Bindabasini", "Sakhuwa Prasauni", "Paterwa Sugauli", "Kalikamai", "Jirabhawani"]}
        ]
    },
    {
        "province": "Bagmati Pradesh",
        "district": [
            {"name": "Sindhuli", "municipalities": ["Kamalamai","Dudhauli","Golanjor","Ghyanglekh","Tinpatan","Phikkal","Marin","Sunkoshi","Hariharpur Gadhi"]},
            {"name": "Ramechhap", "municipalities": ["Manthali","Ramechhap","Umakunda","Khandadevi", "Gokulganga", "Doramba", "Likhu Tamakoshi", "Sunapati"]},
            {"name": "Dolakha", "municipalities": ["Jiri", "Bhimeswor", "Kalinchok", "Gaurishankar", "Tamakoshi", "Melung", "Bigu", "Baiteshwor", "Sailung"]},
            {"name": "Sindhupalchok", "municipalities": ["Chautara", "Bahrabise", "Melamchi", "Indrawati", "Jugal", "Panchpokhari Thangpal", "Balephi", "Bhotekoshi", "Lisankhu Pakhar", "Sunkoshi", "Helambu", "Tripurasundari"]},
            {"name": "Kavrepalanchok", "municipalities": ["Dhulikhel", "Banepa", "Panauti", "Panchkhal", "Namobuddha", "Mandandeupur", "Khani Khola", "Chauri Deurali", "Temal", "Bethanchok", "Bhumlu", "Mahabharat", "Roshi"]},
            {"name": "Lalitpur", "municipalities": ["Lalitpur Maha", "Godawari", "Mahalaxmi", "Konjyoson", "Bagmati", "Mahankal"]},
            {"name": "Bhaktapur", "municipalities": ["Changunarayan", "Bhaktapur", "Madhyapur Thimi", "Suryabinayak"]},
            {"name": "Kathmandu", "municipalities": ["Kathmandu", "Kageshwari Manohara", "Kirtipur", "Gokarneshwar", "Chandragiri", "Tokha", "Tarakeshwar", "Dakshinkali", "Nagarjun", "Budanilkantha", "Shankharapur"]},
            {"name": "Nuwakot", "municipalities": ["Bidur", "Belkotgadhi", "Kakani", "Kispang", "Tadi", "Tarkeshwar", "Dupcheshwar", "Panchakanya", "Likhu", "Myagang", "Shivapur", "Suryagadhi"]},
            {"name": "Rasuwa", "municipalities": ["Uttargaya", "Kalika", "Gosaikunda", "Naukunda", "Aama Chhodingmo"]},
            {"name": "Dhading", "municipalities": ["Dhunibeshi", "Nilkantha", "Khaniyabas", "Gajuri", "Galchhi", "Gangajamuna", "Jwalamukhi", "Thakre", "Netrawati Dabjong", "Benighat Rorang", "Rubi Valley", "Siddhalek", "Tripurasundar"]},
            {"name": "Makwanpur", "municipalities": ["Hetauda", "Thaha", "Indrasarowar", "Kailash", "Bakaiya", "Bagmati", "Bhimphedi", "Makawanpurgadhi", "Manahari", "Raksirang"]},
            {"name": "Chitwan", "municipalities": ["Bharatpur", "Kalika", "Khairahani", "Madi", "Ratnanagar", "Rapti", "Ichchhakamana"]}
        ]
    },
    {
        "province": "Gandaki Pradesh",
        "district": [
            {"name": "Gorkha", "municipalities": ["Gorkha","Palungtar", "Sulikot", "Siranchok", "Ajirkot", "Aarughat", "Gandaki", "Chum Nubri", "Dharche", "Bhimsen", "Sahid Lakhan"]},
            {"name": "Lamjung", "municipalities": ["Besisahar","Madhya Nepal","Rainas","Sundarbazar", "Kwhlosothar", "Dudhpokhari", "Dordi", "Marsyandi"]},
            {"name": "Tanahun", "municipalities": ["Bhanu", "Bhimad", "Byas", "Shuklagandaki", "Anbu Khaireni", "Rhishing", "Ghiring", "Devghat", "Myagde", "Bandipur"]},
            {"name": "Syangja", "municipalities": ["Galyang", "Chapakot", "Putalibazar", "Bheerkot", "Waling", "Arjun Chaupari", "Aandhikhola", "Kaligandaki", "Phedikhola", "Biruwa", "Harinas"]},
            {"name": "Kaski", "municipalities": ["Pokhara", "Annapurna", "Machhapuchchhre", "Madi", "Rupa"]},
            {"name": "Manang", "municipalities": ["Chame", "Narpa Bhumi", "Nason", "Manang Ngisyang"]},
            {"name": "Mustang", "municipalities": ["Gharpajhong", "Thasang", "Lo-ghekar Damodarkund", "Lomanthang", "Barhagaun Muktichhetra"]},
            {"name": "Myagdi", "municipalities": ["Beni", "Annapurna", "Dhaulagiri", "Mangala", "Malika", "Raghugang"]},
            {"name": "Parbat", "municipalities": ["Kusma", "Phalewas", "Jaljala", "Paiyun", "Mahashila", "Modi", "Bihadi"]},
            {"name": "Baglung", "municipalities": ["Baglung", "Galkot", "Jaimuni", "Dhorpatan", "Bareng", "Kathekhola", "Tamankhola", "Tarakhola", "Nisikhola", "Badigad"]},
            {"name": "Nawalparasi", "municipalities": ["Kawasoti", "Gaidakot", "Devachuli", "Madhyabindu", "Baudikali", "Bulingtar", "Binayee Triveni", "Hupsekot"]}
        ]
    },
    {
        "province": "Province No. 5",
        "district": [
            {"name": "Gulmi", "municipalities": ["Musikot", "Resunga", "Isma", "Kaligandaki", "Gulmi Durbar", "Satyawati", "Chandrakot", "Ruruchhetra", "Chatrakot", "Dhurkot", "Madane", "Malika"]},
            {"name": "Palpa", "municipalities": ["Rampur", "Tansen", "Nisdi", "Purbakhola", "Rambha", "Mathagadi", "Tinahu", "Bagnaskali", "Ripdikot", "Rainadevi Chhahara"]},
            {"name": "Rupandehi", "municipalities": ["Butwal", "Devdaha", "Lumbini Sanskritik", "Sainamaina", "Siddharthnagar", "Tilottama", "Gaidahawa", "Kanchan", "Kotahimai", "Marchwari", "Mayadevi", "Omsatiya", "Rohini", "Sammarimai", "Siyari", "Suddodhan"]},
            {"name": "Kapilvastu", "municipalities": ["Kapilvastu", "Banganga", "Shivaraj", "Maharajgunj", "Krishnanagar", "Banaganga", "Mayadevi", "Yashodhara", "Suddhodhan", "Bijaynagar"]},
            {"name": "Arghakhanchi", "municipalities": ["Sandhikharka", "Sitganga", "Bhumikasthan", "Chhatradev", "Panini", "Malarani"]},
            {"name": "Pyuthan", "municipalities": ["Pyuthan", "Swargadwari", "Gaumukhi", "Mandavi", "Sarumarani", "Mallarani", "Naubahini", "Jhimruk", "Airawati"]},
            {"name": "Rolpa", "municipalities": ["Rolpa", "Triveni", "Paribartan", "Madi", "Runtigadi", "Lungri", "Gangadev", "Sunchahari", "Sunil Smriti", "Thawang"]},
            {"name": "Dang", "municipalities": ["Tulsipur", "Ghorahi", "Lamahi", "Banglachuli", "Dangisharan", "Gadhawa", "Rajpur", "Rapti", "Shantinagar", "Babai"]},
            {"name": "Banke", "municipalities": ["Nepalgunj", "Kohalpur", "Narainapur", "Rapti-Sonari", "Baijanath", "Khajura", "Duduwa", "Janaki"]},
            {"name": "Bardiya", "municipalities": ["Gulariya", "Madhuwan", "Rajapur", "Thakurbaba", "Basgadhi", "Barbardiya", "Badhaiyatal", "Geruwa"]},
            {"name": "Nawalparasi", "municipalities": ["Bardaghat", "Ramgram", "Sunwal", "Susta", "Palhi Nandan", "Pratappur", "Sarawal"]},
            {"name": "Rukum", "municipalities": ["Putha Uttarganga", "Bhume", "Sisne"]}
        ]
    },
    {
        "province": "Karnali Pradesh",
        "district": [
            {"name": "Salyan", "municipalities": ["Shaarda", "Bagchaur", "Bangad Kupinde", "Kalimati", "Tribeni", "Kapurkot", "Chatreshwari", "Siddha Kumakh", "Kumakh", "Darma"]},
            {"name": "Surkhet", "municipalities": ["Birendranagar", "Bheriganga", "Gurbha Kot", "Panchapuri", "Lekbesi", "Chaukune", "Barahatal", "Chingad", "Simta"]},
            {"name": "Dailekh", "municipalities": ["Narayan", "Dullu", "Chamunda Bindrasaini", "Aathbis", "Bhagawatimai", "Gurans", "Dungeshwar", "Naumule", "Mahabu", "Bhairabi", "Thantikandh"]},
            {"name": "Jajarkot", "municipalities": ["Bheri", "Chhedagad", "Nalgad", "Barekot", "Kushe", "Junichande", "Shivalaya"]},
            {"name": "Dolpa", "municipalities": ["Thuli Bheri", "Tripurasundari", "Dolpo Buddha", "Shey Phoksundo", "Jagadulla", "Mudkechula", "Kaike", "Chharka Tangsong"]},
            {"name": "Jumla", "municipalities": ["Chandannath", "Kankasundari", "Sinja", "Hima", "Tila", "Guthichaur", "Tatopani", "Patarasi"]},
            {"name": "Kalikot", "municipalities": ["Khandachakra", "Raskot", "Tilagufa", "Pachaljharana", "Sanni Triveni", "Narharinath", "Shubha Kalika", "Mahawai", "Palata"]},
            {"name": "Mugu", "municipalities": ["Chhayanath Rara", "Mugum Karmarong", "Soru", "Khatyad"]},
            {"name": "Humla", "municipalities": ["Simkot", "Namkha", "Kharpunath", "Sarkegad", "Chankheli", "Adanchuli", "Tajakot"]},
            {"name": "Rukum", "municipalities": ["Musikot", "Chaurjahari", "Aathbiskot", "Banphikot", "Tribeni", "Sani Bheri"]}
        ]
    },
    {
        "province": "Sudurpashchim Pradesh",
        "district": [
            {"name": "Bajura", "municipalities": ["Badimalika", "Triveni", "Budhiganga", "Budhinanda", "Gaumul", "Jagnnath", "Swamikartik", "Chhededaha", "Himali"]},
            {"name": "Bajhang", "municipalities": ["Jaya Prithvi", "Bungal", "Talkot", "Masta", "Khaptadchhanna", "Thalara", "Bitthadchir", "Surma", "Chhabispathiver", "Durgathali", "Kedarsyu", "Kanda"]},
            {"name": "Achham", "municipalities": ["Mangalsen", "Kamalbazar", "Sanphebagar", "Panchadewal Binayak", "Chaurpati", "Mellekh", "Bannigadi Jayagad", "Ramaroshan", "Dhakari", "Turmakhand"]},
            {"name": "Doti", "municipalities": ["Dipayal Silgadhi", "Shikhar", "Purbichauki", "Badikedar", "Jorayal", "Sayal", "Aadarsha", "KI Singh", "Bogatan"]},
            {"name": "Kailali", "municipalities": ["Dhangadhi", "Tikapur", "Ghodaghodi", "Lamki Chuha", "Bhajani", "Godawari", "Gauriganga", "Janaki", "Bardagoriya", "Mohanyal", "Kailari", "Joshipur", "Chure"]},
            {"name": "Kanchanpur", "municipalities": ["Bhimdatta", "Punarbas", "Bedkot", "Mahakali", "Shuklaphanta", "Belauri", "Krishnapur", "Beldandi", "Laljhadi"]},
            {"name": "Dadeldhura", "municipalities": ["Amargadhi", "Parshuram", "Aalital", "Bhageshwor", "Navadurga", "Ajayameru", "Ganyapadhura"]},
            {"name": "Baitadi", "municipalities": ["Dasharathchand", "Patan", "Melauli", "Purchaudi", "Sunarya", "Sigas", "Shivanath", "Pancheshwor", "Dogdakedar", "Dilasaini"]},
            {"name": "Darchula", "municipalities": ["Mahakali", "Shailyasikhar", "Malikarjun", "Apihimal", "Duhun", "Naugadh", "Marma", "Lekam", "Vyans"]}
        ]
    }
]
    for i in new_address:        
            prov=Province.objects.create(name=i['province'])
            for j in i['district']:
                dist=District.objects.create(name=j['name'],province=prov)
                for k in j['municipalities']:                    
                    muni=Municipality.objects.create(name=k,district=dist)
                muni.save()
            dist.save()
    prov.save()