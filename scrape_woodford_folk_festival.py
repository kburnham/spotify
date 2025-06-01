from bs4 import BeautifulSoup

def scrape_titles_from_file(file_path):
    # Open and read the HTML content from the local file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all div elements with the class "pse-title"
    titles = soup.find_all('div', class_='pse-title')

    # Extract and return the text content of each title
    return [title.get_text(strip=True) for title in titles]

# Path to the local HTML file
file_path = "/Users/kevin/Desktop/view-source_https___woodfordfolkfestival.com_programme_.html"  # Replace with the path to your file

# Call the function and print the results
titles = scrape_titles_from_file(file_path)
print("\n".join(titles))



with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

titles = soup.find_all('div', class_='pse-title')




from bs4 import BeautifulSoup
import html

# Input HTML text
html_text = """
<li>23 Skidoo &amp; the Secret Agency</li>
<li>A Good Catch</li>
<li>a hop and a skip</li>
<li>Adam Spencer</li>
<li>Aerborn</li>
<li>Alan Kelly</li>
<li>Alana Rain</li>
<li>Alex The Astronaut</li>
<li>Alieta Belle</li>
<li>Allie Ng-Lee</li>
<li>Allora</li>
<li>Ally Palmer</li>
<li>Aly de Groot</li>
<li>Amaidí</li>
<li>Amanda Rheaume</li>
<li>Amazing Fun for Kids</li>
<li>Amelie Ecology</li>
<li>Amiria-Jade Art</li>
<li>Ampe-Kenhe Ahelhe Band</li>
<li>Andrea Kirwin and The Yama-Nui Social Club</li>
<li>Andrew Hull</li>
<li>Andy Copeman Medicine Man Music feat. Laurel Bay Tree</li>
<li>Angela Peita</li>
<li>Angeline Wynter</li>
<li>Angkana Whiley</li>
<li>Angus Hamill</li>
<li>Anisa Nandaula</li>
<li>Anousha Victoire</li>
<li>Anya Anastasia</li>
<li>Anya and Stef of West End Yoga</li>
<li>arís</li>
<li>Arna Baartz</li>
<li>Artfolk</li>
<li>Arzu Ünel-Cleary</li>
<li>Ash Grunwald</li>
<li>Ash Morse</li>
<li>Asleep at the Reel</li>
<li>Auburn in Love</li>
<li>Aura The Fairy and Friends</li>
<li>AURUS</li>
<li>Auslan For Everyone</li>
<li>Ayesha Blanco</li>
<li>Aysanabee</li>
<li>Backbone Youth Arts</li>
<li>Bailey Judd</li>
<li>Baker Boy</li>
<li>Ball Mania</li>
<li>Ball Park Music</li>
<li>Bare Knees</li>
<li>Batbox Super Hero</li>
<li>Beach Volleyball</li>
<li>Beccy Cole</li>
<li>Begonia</li>
<li>Belinda Chellingworth</li>
<li>Belinda Tucker</li>
<li>Ben Hunter</li>
<li>Bethany Woodman</li>
<li>Bhangra Dance</li>
<li>Bianca Bond</li>
<li>Biannka Brannigan</li>
<li>Bic Runga</li>
<li>Billie Weston &#8211; JUNGLE JUICE</li>
<li>Birren</li>
<li>Blues Arcadia</li>
<li>BOOF</li>
<li>BOOM Shanko</li>
<li>Breandán an Píobaire</li>
<li>Breathe with Bansuri</li>
<li>Brenna Quinlan</li>
<li>Brisbane AcroYoga</li>
<li>Broken Creek</li>
<li>Bromham</li>
<li>Brotherhood of the Wordless</li>
<li>Bunky and Grandma</li>
<li>Caliko</li>
<li>Calypso Cora</li>
<li>Caravãna Sun</li>
<li>Cardboard Creations</li>
<li>Carol Wilmot</li>
<li>Caroline Cowley</li>
<li>Cate McQuillen</li>
<li>Catherine Conaty</li>
<li>Centre for Disability Research and Policy, The University of Sydney</li>
<li>Charlotte Connell</li>
<li>Children Of Yoga</li>
<li>Chloe Matharu</li>
<li>Chris &#8216;Sese&#8217; Cobb</li>
<li>Chris Ah Gee</li>
<li>Church of the Clitori</li>
<li>Circus in the Clouds</li>
<li>Cirque Hot Club</li>
<li>CJ Shaw</li>
<li>Claire Evelynn</li>
<li>Claudio Rabe</li>
<li>Clermont&#8217;s Clinic</li>
<li>Cocoloco</li>
<li>Conspiracy of One</li>
<li>Corner Pocket Swing</li>
<li>Costa Georgiadis</li>
<li>Cracked Anvil Forge</li>
<li>Craig Madden</li>
<li>Craig Walsh</li>
<li>Cuban Dance Company</li>
<li>Damian Callinan</li>
<li>Dan Sultan</li>
<li>Dande and The Lion</li>
<li>Darren Hanlon</li>
<li>David Hallett</li>
<li>Deejaye Katch</li>
<li>Dennis Comino</li>
<li>Diana Z Diaz &#8220;Mexicanera&#8221;</li>
<li>Dianne Conroy</li>
<li>Digging Roots</li>
<li>Dillion James</li>
<li>dirtgirlworld</li>
<li>Djuelu The Village Scribe</li>
<li>Dream Collectors</li>
<li>DUB ZOO</li>
<li>Duckie Darling</li>
<li>East of West</li>
<li>Echoes of Cirque</li>
<li>Eils &amp; The Drip</li>
<li>Elana Stone</li>
<li>Elemental Journeys</li>
<li>Elephant Sessions</li>
<li>Elischa Swan</li>
<li>Elissa Farrow</li>
<li>Elliot Leach</li>
<li>Em Niwa</li>
<li>Embellysh Photography</li>
<li>Emily Loe</li>
<li>Emma Wilson and Seamus Kirkpatrick</li>
<li>Erin Lee &amp; Shivam Rath</li>
<li>Eumundi School of Music</li>
<li>Fairytale Flow</li>
<li>Felicity Dowd</li>
<li>Flame and Pickle</li>
<li>Flamenco House</li>
<li>Folkaphonic Youth Orchestra</li>
<li>FOOLS</li>
<li>Formidable Vegetable</li>
<li>Forro Brisbane</li>
<li>Forrobodoz</li>
<li>Forward Kwenda and Velvet Pesu</li>
<li>Francesca Carpenter</li>
<li>Frank Yamma</li>
<li>From The Flame Trees</li>
<li>Future Destin</li>
<li>Gallivanting Gastropod</li>
<li>Geoff Wood</li>
<li>Geoffrey Le Goaziou</li>
<li>Geordie Williamson</li>
<li>Gina Chick</li>
<li>Good Guy Hank</li>
<li>Good Tunes</li>
<li>Grigoryan Brothers</li>
<li>Gubbi Gubbi Dance</li>
<li>Gypsy Cats</li>
<li>Hannaka Zakachard</li>
<li>Happy Bears</li>
<li>Harding&#8217;s House</li>
<li>Harley Breen</li>
<li>Hayden Hack</li>
<li>He Huang</li>
<li>Headphones Jones</li>
<li>Heart Breath Awakening</li>
<li>Heather Price</li>
<li>Helen Schwencke</li>
<li>High School Folk n Roll</li>
<li>Homebru</li>
<li>HOTMESS- In the Flesh</li>
<li>Humarimba</li>
<li>Husky</li>
<li>Ian Lowe</li>
<li>Imogen Kelly</li>
<li>Ingrid Johnson</li>
<li>Iontach</li>
<li>Isabella Ferroni</li>
<li>Isobel Knight</li>
<li>J-MILLA</li>
<li>Jack Raymond</li>
<li>Jaga Band</li>
<li>Jaguar Jonze</li>
<li>Jane Michele &amp; The Consortium</li>
<li>Jane Richens</li>
<li>Janty Blair</li>
<li>Jason Murphy</li>
<li>Jason Roweth</li>
<li>Jay Wymarra</li>
<li>JaZZella</li>
<li>Jeff Hansen</li>
<li>Jen Mize &amp; The Rough n Tumble</li>
<li>Jennifer Andrews</li>
<li>Jenny Newell</li>
<li>Jeremy Staples</li>
<li>Jessie Carson</li>
<li>JFDR</li>
<li>Jinibara Dance Group</li>
<li>Jinibara Speaks</li>
<li>Joe H Henry</li>
<li>Joe Hallenstein</li>
<li>Jordie Lane</li>
<li>Josh Pyke</li>
<li>Kankawa Nagarra</li>
<li>Karma Dance Inc.</li>
<li>Karma Dives</li>
<li>Karul Projects</li>
<li>Karungkarni Art and Culture</li>
<li>Katy Steele</li>
<li>Kerri Gill</li>
<li>Kerryn Fields</li>
<li>Kevin Kropinyeri</li>
<li>Kids Are Great</li>
<li>King Stingray</li>
<li>Kinship</li>
<li>Kirsty Bishop-Fox</li>
<li>Kristal West</li>
<li>Kristin Kelly</li>
<li>Kundalini Yoga Spirit Journeys</li>
<li>Laura Cortese &amp; the Dance Cards</li>
<li>Laureen &amp; Friends</li>
<li>Lee Hardisty</li>
<li>Lenka</li>
<li>Lettering House</li>
<li>LightnUp Inc</li>
<li>Like a Photon</li>
<li>Lilliahna Rogers</li>
<li>Lindy Edwards</li>
<li>Linsey Pollak</li>
<li>Liquorice Bufo</li>
<li>Lisa Iselin &#8211; Sundog Craft</li>
<li>Lisa Johnson</li>
<li>Lisa Raquel Cowan</li>
<li>Little Quirks</li>
<li>Little Wing Puppets</li>
<li>Liz Skitch</li>
<li>Lonely Boot Creations</li>
<li>Lucy Wise</li>
<li>Luke Wright</li>
<li>Mad Dance House</li>
<li>Mad Scrabblers</li>
<li>Malo&#8217;</li>
<li>Mandala House &#8211; The Architecture of Awakening</li>
<li>Manoa</li>
<li>Manoeuvre &#8211; Roving Stilt Performers</li>
<li>Maria Almonacid</li>
<li>Mary Frances</li>
<li>Matt Sier</li>
<li>Matt The Electrician</li>
<li>Meg Washington</li>
<li>Melbourne Céilí Band</li>
<li>Melbourne Ska Orchestra</li>
<li>Memetica</li>
<li>Merpire</li>
<li>Merryn Penington &#8211; Structural Energetics</li>
<li>Michelle Freeman</li>
<li>Mickey &amp; Michelle</li>
<li>Middar</li>
<li>Midnight Chicken</li>
<li>Mike McClellan</li>
<li>Milk Crate Circus</li>
<li>Mimi O&#8217;Bonsawin</li>
<li>Minou Duval</li>
<li>Miss Bubbles</li>
<li>Miss Kaninna</li>
<li>Miss Radida</li>
<li>Monique Clare</li>
<li>Monks of Tibet</li>
<li>Montz Matsumoto and Voicestrings</li>
<li>Moran Wiesel</li>
<li>Morrigan &amp; Wilding</li>
<li>Mt Ninderry Art House</li>
<li>Mundy-Turner</li>
<li>Mz Mally Moo&#8217;s Music 4 Minis</li>
<li>Nathan Beretta Band</li>
<li>Nathan Cavaleri</li>
<li>Natureweavers</li>
<li>Nearly Normal Norman</li>
<li>New Earth Metta Breathwork</li>
<li>Newbury Fog</li>
<li>Ngaiire and Paul Grabowsky</li>
<li>Nick Grivas</li>
<li>Nicola Ossher</li>
<li>Niki Roy</li>
<li>Nikki Britton</li>
<li>Nikolaine Martin</li>
<li>Niq Reefman</li>
<li>Noel Gardner &amp; The Party Faithful</li>
<li>Ocean in Motion</li>
<li>Oh My Goat</li>
<li>Oliver Roweth</li>
<li>Olivia Rosebery</li>
<li>Oscar Serrallach</li>
<li>Pan &amp; Boo</li>
<li>PanAlchemy</li>
<li>Papa Fire &amp; Mr Beatz</li>
<li>Paris Martine</li>
<li>Parnian Zanganeh</li>
<li>Pendragon Shoes</li>
<li>Penny Davies</li>
<li>Peter Gresshoff</li>
<li>Peter Vadiveloo</li>
<li>Phil Barlow</li>
<li>Phil Smart</li>
<li>Pipin</li>
<li>Pixie</li>
<li>Play with Clay</li>
<li>Potters of Woodfordia</li>
<li>Queensland XR Hub</li>
<li>Queensland Youth Folk Orchestra</li>
<li>QUT Digital Media Research Centre</li>
<li>Rachele Wilson</li>
<li>Rainbow Endz</li>
<li>Rhoda Roberts</li>
<li>Richie LeStrange</li>
<li>Richie Merzian</li>
<li>Riley Catherall</li>
<li>Rising Waves</li>
<li>Rizal Hadi &amp; Folk</li>
<li>Rob Carlton</li>
<li>Robin Clayfield and The Sacred Union Labyrinth</li>
<li>Robyn Martin</li>
<li>Rory Kelly</li>
<li>Rosie Waters</li>
<li>Round Mountain Girls</li>
<li>Rubatuba</li>
<li>Ruby Stone</li>
<li>Rutherford Jazz Trio</li>
<li>Sacred Union Labyrinth Band</li>
<li>Sai Galaxy</li>
<li>Sam Lee</li>
<li>Sampology</li>
<li>Sandpoppy Weaving</li>
<li>Sarah Howells</li>
<li>Sarah Pye</li>
<li>Sex On Toast</li>
<li>Shmoné</li>
<li>Silli-Mulli Cultural Group from Enga Province</li>
<li>SING</li>
<li>Skillz FJ</li>
<li>Slowmango</li>
<li>SOLUA</li>
<li>Sophie Banister</li>
<li>Soraya Fewquandie</li>
<li>Soula</li>
<li>Sounds of India</li>
<li>Spaghetti Circus</li>
<li>Spencer Hitchen</li>
<li>Splash Mob Theatre</li>
<li>Stay Cool &#8211; Play Chess</li>
<li>Strike and String</li>
<li>String Beings</li>
<li>SUB-TRIBE</li>
<li>Suitable Circus</li>
<li>Sunni Holden</li>
<li>Sunny Days &#8211; Rise, Nourish &amp; Thrive</li>
<li>Susan O&#8217;Neill</li>
<li>Tahlia Connie</li>
<li>Tanya Davis</li>
<li>Tenzin Choegyal</li>
<li>Tenzin Kunsang</li>
<li>TESSA DEVINE</li>
<li>The Backyard Banjo Club</li>
<li>The Bad Dad Orchestra</li>
<li>The Between</li>
<li>The Bower</li>
<li>The Bubble Bower Birds</li>
<li>The Burning Hell</li>
<li>The Fairy Green</li>
<li>The Good Behaviours</li>
<li>The Great Band Competition</li>
<li>The Hanging Tree</li>
<li>The High Street Drifters</li>
<li>The Hillbilly Skank</li>
<li>The Hoodlum Ballet</li>
<li>The Insecurity Guards</li>
<li>The Joy</li>
<li>The Korean Traditional Performers Group Hanmadang Inc.</li>
<li>The Mad Mariachi</li>
<li>The Maestro</li>
<li>The Mobile Jewellery Tudor</li>
<li>The Moving Stills</li>
<li>The Museum of Interactive Effigies</li>
<li>The Mushroom Whisperers</li>
<li>The Seamstresses</li>
<li>The Seven of Ska</li>
<li>The Slims</li>
<li>The Squeaking Tribe</li>
<li>Thirty Years of Tabla</li>
<li>This New Light</li>
<li>Those Folk</li>
<li>Tia Gostelow</li>
<li>Tie Dye Magic</li>
<li>Tim Scanlan &amp; Mana Okubo</li>
<li>Tjaka</li>
<li>Toko-ton Taiko and Friends</li>
<li>Tracey Miller</li>
<li>Tracy Lewis Art</li>
<li>Transylvanian Gypsy Kings</li>
<li>Tuck Shop Ladies</li>
<li>TYDE</li>
<li>Uncle Kenny Murphy</li>
<li>Uncle Noel Blair</li>
<li>Vardos</li>
<li>Victor Steffensen</li>
<li>Vihor &#8211; A Balkan Whirlwind</li>
<li>VJ Harvey</li>
<li>Wahoo Business</li>
<li>Weaving is Healing</li>
<li>Wild Yeast Zoo</li>
<li>Wildhouse Circus</li>
<li>Woodford Morris Dancers</li>
<li>Yarraka and Quaden Bayles</li>
<li>Yi-jung Hsien</li>
<li>Yothu Yindi</li>
<li>Ysé</li>
<li>Ziggy Ramo</li>
<li>Zimmi Forest</li>
<li>ZoBo &amp; Dingo</li>
<li>Zoe Kean</li>
"""

# Parse the HTML content
soup = BeautifulSoup(html_text, 'html.parser')

# Extract text and unescape HTML entities
cleaned_text = [html.unescape(li.get_text(strip=True)) for li in soup.find_all('li')]

# Output as a newline-separated list
print("\n".join(cleaned_text))