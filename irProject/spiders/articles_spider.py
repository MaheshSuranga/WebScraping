import scrapy
from scrapy_splash import SplashRequest 

class ArticlesSpider(scrapy.Spider):
    name = "articles"

    def start_requests(self):
        urls = [
            'https://roar.media/sinhala/main/science-tech/biggest-star-uy-scuti/',
            'https://roar.media/sinhala/main/science-tech/facts-about-planet-mercury/',
            'https://roar.media/sinhala/main/science-tech/sea-wave-power-generation/',
            'https://roar.media/sinhala/main/science-tech/india-puts-lightest-satellite-kalamsat-v2-into-orbit/',
            'https://roar.media/sinhala/main/science-tech/threefold-increase-in-asteroid-strikes/',
            'https://roar.media/sinhala/main/science-tech/life-like-robot-machines/',
            'https://roar.media/sinhala/main/science-tech/structure-of-spider-silk/',
            'https://roar.media/sinhala/main/science-tech/media-tek-yasantha-rajakarunanayake/',
            'https://roar.media/sinhala/main/science-tech/why-is-10-10-the-default-setting-for-clocks/',
            'https://roar.media/sinhala/main/science-tech/the-modern-aeroplane-engine/',
            'https://roar.media/sinhala/main/science-tech/spacex-names-first-moon-passenger-yusaku-maezawa/',
            'https://roar.media/sinhala/main/science-tech/bangalore-electronic-city-the-silicon-valley-of-india/',
            'https://roar.media/sinhala/main/science-tech/alternative-fuel-sources-instead-of-oil/',
            'https://roar.media/sinhala/main/science-tech/what-are-the-genetic-disorders/',
            'https://roar.media/sinhala/main/science-tech/copper-coins-turned-into-gold/',
            'https://roar.media/sinhala/main/science-tech/bermuda-fire-warm-beauty-of-nature/',
            'https://roar.media/sinhala/main/science-tech/discovery-of-elements-vi/',
            'https://roar.media/sinhala/main/science-tech/bennu-asteroid-would-it-hit-earth/',
            'https://roar.media/sinhala/main/science-tech/ceres-the-dwarf-planet/',
            'https://roar.media/sinhala/main/science-tech/how-elements-were-discovered-v/',
            'https://roar.media/sinhala/main/science-tech/how-elements-were-discovered-iv/',
            'https://roar.media/sinhala/main/science-tech/how-elements-were-discovered-iii/',
            'https://roar.media/sinhala/main/science-tech/how-elements-were-discovered-ii/',
            'https://roar.media/sinhala/main/science-tech/how-hydrogen-helium-lithium-was-discovered/',
            'https://roar.media/sinhala/main/science-tech/how-are-your-lithium-batteries-made/',
            'https://roar.media/sinhala/main/science-tech/oldest-surviving-planetarium-in-the-world/',
            'https://roar.media/sinhala/main/science-tech/tasmanian-tiger-rebirth-through-cloning/',
            'https://roar.media/sinhala/main/science-tech/human-chimpanzee-insemination-efforts/',
            'https://roar.media/sinhala/main/science-tech/the-iron-dorm-system-israel/',
            'https://roar.media/sinhala/main/science-tech/bioweapons-and-biological-warfare/',
            'https://roar.media/sinhala/main/science-tech/incredible-7d-hologram-technology/',
            'https://roar.media/sinhala/main/science-tech/the-famous-porsche-car/',
            'https://roar.media/sinhala/main/science-tech/the-planet-eris/',
            'https://roar.media/sinhala/main/science-tech/real-world-frankenstein-experiments/',
            'https://roar.media/sinhala/main/science-tech/99942-apophis-may-destroy-earth/',
            'https://roar.media/sinhala/main/science-tech/chernobyl-nuclear-power-station-rising/',
            'https://roar.media/sinhala/main/science-tech/how-the-qwerty-keyboard-was-born/',
            'https://roar.media/sinhala/main/science-tech/china-space-station-tiangong-1/',
            'https://roar.media/sinhala/main/science-tech/sustained-power-sources/',
            'https://roar.media/sinhala/main/science-tech/about-dark-energy/',
            'https://roar.media/sinhala/main/science-tech/inventors-who-killed-by-their-inventions/',
            'https://roar.media/sinhala/main/science-tech/makemake-the-dwarf-planet/',
            'https://roar.media/sinhala/main/science-tech/ethical-issues-in-cloning/',
            'https://roar.media/sinhala/main/science-tech/mysterious-illuminating-plants/',
            'https://roar.media/sinhala/main/science-tech/would-elon-musk-take-over-the-world/',
            'https://roar.media/sinhala/main/science-tech/how-japan-protects-buildings-against-earthquakes/',
            'https://roar.media/sinhala/main/science-tech/worlds-5th-nuke-power/',
            'https://roar.media/sinhala/main/science-tech/growing-a-ear-in-lab/',
            'https://roar.media/sinhala/main/science-tech/what-is-asgardia/',
            'https://roar.media/sinhala/main/science-tech/dark-side-of-artificial-lights/',
            'https://roar.media/sinhala/main/science-tech/2-1-2-minutes-to-worlds-end/',
            'https://roar.media/sinhala/main/science-tech/nano-technology/',
            'https://roar.media/sinhala/main/science-tech/japanese-inventions/',
            'https://roar.media/sinhala/main/science-tech/haumea-the-minor-planet/',
            'https://roar.media/sinhala/main/science-tech/projection-mapping/',
            'https://roar.media/sinhala/main/science-tech/working-at-facebook/',
            'https://roar.media/sinhala/main/science-tech/history-of-the-washing-machine/',
            'https://roar.media/sinhala/main/science-tech/history-of-the-washing-machine/',
            'https://roar.media/sinhala/main/science-tech/dna-paternity-testing/',
            'https://roar.media/sinhala/main/science-tech/nasa-new-engine/',
            'https://roar.media/sinhala/main/science-tech/benefits-of-international-space-station/',
            'https://roar.media/sinhala/main/science-tech/periodic-table-origin/',
            'https://roar.media/sinhala/main/science-tech/new-electric-truck-tesla-semi/',
            'https://roar.media/sinhala/main/science-tech/gis/',
            'https://roar.media/sinhala/main/science-tech/international-space-station/',
            'https://roar.media/sinhala/main/science-tech/panama-canal-an-engineering-marvel/',
            'https://roar.media/sinhala/main/science-tech/cicada-330/',
            'https://roar.media/sinhala/main/science-tech/colour-blindness/',
            'https://roar.media/sinhala/main/science-tech/flying-cars/',
            'https://roar.media/sinhala/main/science-tech/nasa-cassini-spacecraft/',
            'https://roar.media/sinhala/main/science-tech/sofia-and-the-effects-of-artificial-intelligence-on-mankind/',
            'https://roar.media/sinhala/main/science-tech/animal-cloning-and-dolly/',
            'https://roar.media/sinhala/main/science-tech/how-does-caffeine-affect-our-bodies/',
            'https://roar.media/sinhala/main/science-tech/blood-donation-facts-and-myths/',
            'https://roar.media/sinhala/main/science-tech/differences-between-male-and-female-minds/',
            'https://roar.media/sinhala/main/science-tech/clouds-and-the-weather-they-bring/',
            'https://roar.media/sinhala/main/science-tech/melting-ice-caps-and-sicknesses/',
            'https://roar.media/sinhala/main/science-tech/do-fish-drink-water/',
            'https://roar.media/sinhala/main/science-tech/the-international-gaming-tournament/',
            'https://roar.media/sinhala/main/science-tech/things-you-didnt-know-about-red-blood-cells/',
            'https://roar.media/sinhala/main/science-tech/undersea-cables-that-connects-sri-lanka-to-the-world/',
            'https://roar.media/sinhala/main/science-tech/eat-meat-without-killing-animals/',
            'https://roar.media/sinhala/main/science-tech/northern-lights-or-auroroas/',
            'https://roar.media/sinhala/main/science-tech/fast-telescope-the-heavenly-eye/',
            'https://roar.media/sinhala/main/science-tech/apocalypse-predictions-pt-2/',
            'https://roar.media/sinhala/main/science-tech/worlds-first-head-transplant/',
            'https://roar.media/sinhala/main/science-tech/ufo-caught-in-teslas-telescope/',
            'https://roar.media/sinhala/main/science-tech/did-nasa-fake-the-moon-landing/',
            'https://roar.media/sinhala/main/science-tech/219-new-planets-discovered/',
            'https://roar.media/sinhala/main/science-tech/concorde-still-the-fastest/',
            'https://roar.media/sinhala/main/science-tech/leader-of-onlin-shopping-amazon/',
            'https://roar.media/sinhala/main/science-tech/a-spacesuit-ready-for-space-flight/',
            'https://roar.media/sinhala/main/science-tech/oily-food/',
            'https://roar.media/sinhala/main/science-tech/10-things-about-animals/',
            'https://roar.media/sinhala/main/science-tech/how-to-grow-a-beard/',
            'https://roar.media/sinhala/main/science-tech/aeroplane/',
            'https://roar.media/sinhala/main/science-tech/all-about-x-ray/',
            'https://roar.media/sinhala/main/science-tech/ozone-layer-the-silent-guardian/',
            'https://roar.media/sinhala/main/science-tech/value-of-honey/',
            'https://roar.media/sinhala/main/science-tech/how-radar-works/'
        ]
        for url in urls:
            yield SplashRequest(url=url, callback=self.parse, args={'wait': 6})


    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'article-%s.json' % page
        author = response.css('div.name::text').get()
        self.log(author)
        # for article in response.css('div.inner-article-body'):
        #     slef.log(article)
        #     yield {
        #         'tags': article.css('*::text').getall()
        #     }
        # details =  {
        #         'url' : response.url,
        #         'title' : response.css('h1.title::text').get(),
        #         'author' : response.css('div.name::text').get(),
        #         'content': response.css('div.inner-article-body p::text').getall()
        #     }
        # self.log(details)
        # with open(filename, 'wb') as f:
        #     f.write(json.dumps(details))
        # self.log('saved file %s' % filename)
        yield {
            'url' : response.url,
            'title' : response.css('h1.title::text').get(),
            'author' : response.css('div.name::text').get(),
            'date': response.css('div#articleDate::text').get(),
            'content': response.css('div.inner-article-body p::text').getall()
        }